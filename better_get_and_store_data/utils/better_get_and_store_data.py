from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
from functools import partial
import threading
from pathlib import Path
import time, json, os, copy

class BetterGetAndStoreData():
    """
    Attributes:
        form_jsons : expects list of .json StringOrByte paths,                | each .json must contains list of field(dictionary)
        db_obj : database-like object (store_data/update_data/read_data/get_data).
        css_dir (optional) : from where you want to attach css files.         | default `server_utils/css`
        run_dir (optional) : in which server will create and load html files. | default `server_utils/html`

        custom_validation_func: Custom Form validation if you want to add any.
        | must return, statues and errors back.
        1. statuses and errors are list.
        2. Add <True/False> in statuses if data is invalid.
        3. Add <error message> in errors for why data is invalid.
        Template:
            def validate_custom_data(filled_data, statues, errors):
                return statues, errors
    """

    def __init__(self, form_jsons: list, db_obj, css_dir=None, run_dir=None, custom_validation_func=None, *args, **kwargs):
        self.form_jsons = form_jsons
        self.db_obj = db_obj
        self.css_dir = css_dir
        self.run_dir = run_dir
        self.custom_validation_func = custom_validation_func

        #defaults
        self.current_dir = Path(__file__).parent
        if not self.css_dir:
            self.css_dir = self.current_dir / 'server_utils' / 'css'
        if not self.run_dir:
            self.run_dir = self.current_dir / 'server_utils' / 'html'
        
        self.html_path = self.run_dir / 'better_get_and_store_data.html'
        self.form_field_prefix = 'nebulae'
        self.colors = {
            'magenta': "\033[95m", 'blue': "\033[94m", 'cyan': "\033[96m",
            'green': "\033[92m", 'yellow': "\033[93m", 'red': "\033[91m",
            'white': "\033[97m", 'reset': "\033[0m"
        }

        #will be set afterwords
        self.form_config = None

    class FormHandler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            self.index_html_file = kwargs.pop('index_html_file', None)
            self.pk = kwargs.pop('pk', None)
            self.parent = kwargs.pop('parent', None)
            super().__init__(*args, **kwargs)

        def define_file_contenttype(self, path):
            if path.endswith(".html"):
                content_type = "text/html"
            elif path.endswith(".css"):
                content_type = "text/css"
            elif path.endswith(".js"):
                content_type = "text/javascript"
            elif path.endswith(".ico"):
                content_type = "image/x-icon"
            else:
                content_type = "application/octet-stream"
            return content_type
        
        def do_GET(self):
            _ = urlparse.parse_qs(urlparse.urlparse(self.path).query)
            m_path = self.path.split('?', 1)[0]
            
            if m_path == '/':
                if not self.index_html_file.exists():
                    self.send_error(404, 'Page Not Found!')
                
                with open(self.index_html_file, 'r') as html_f:
                    send_data = html_f.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(send_data.encode())
            else:
                try:
                    # Open the static file requested and send it
                    with open(self.path, 'rb') as file:
                        self.send_response(200)
                        self.send_header('Content-type', self.define_file_contenttype(self.path))
                        self.end_headers()
                        self.wfile.write(file.read())
                except FileNotFoundError:
                    self.send_error(404, 'File Not Found: %s' % self.path)

        def shutdown_server(self):
            self.server.shutdown()
            self.server.server_close()

        def do_POST(self):
            def quit_after_save():
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(f"Data Saved! you can close this window!".encode()))

                print(f'{self.parent.colors.get("green")}[+] Yay! Data Saved{self.parent.colors.get("reset")}')

                #shutdown server
                shutdown_thread = threading.Thread(target=self.shutdown_server, daemon=True)
                shutdown_thread.start()

            if self.path == '/submit':
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length).decode('utf-8')
                parsed_data = urlparse.parse_qs(post_data)

                is_factory = False
                if self.pk and isinstance(self.pk, list):
                    is_factory = True

                if is_factory:
                    grouped_data = {}
                    for key, value in parsed_data.items():
                        p_id, key = key.split('__')

                        if not grouped_data.get(p_id):
                            grouped_data[p_id] = {}
                        grouped_data[p_id][key] = value

                    status, factory_data = self.parent.verify_form(grouped_data, pk=self.pk, factory=True)
                    if not status:
                        self.send_response(302)
                        self.send_header('Location', '/?error=1')
                        self.send_header('Content-type', 'text/html')
                        self.end_headers()
                        return
                    
                    for index, d_data in enumerate(factory_data):
                        pk = self.pk[index]
                        self.parent.create_or_edit_data(pk, data=d_data)

                else:
                    edit = False
                    if self.pk:
                        edit = True

                    status, _ = self.parent.verify_form(parsed_data, edit, pk=self.pk)
                    if not status:
                        self.send_response(302)
                        self.send_header('Location', '/?error=1')
                        self.send_header('Content-type', 'text/html')
                        self.end_headers()
                        return
                    
                    self.parent.create_or_edit_data(self.pk)

                quit_after_save()

    def create_handler(self, **kwargs):
        return partial(BetterGetAndStoreData.FormHandler, **kwargs)

    def start_http_server(self, **kwargs):
        str_name = f'server_request_{str(int(time.time()))}'
        ports=[8080, 8081, 8082]
        host = '127.0.0.1'
        for port in ports:
            try:
                server_address = (host, port)
                handler = self.create_handler(**kwargs)
                httpd = HTTPServer(server_address, handler)
                print(f'Request ID: {self.colors["yellow"]}{str_name}{self.colors["reset"]}')
                print(f'Please visit this url and add required data {self.colors["cyan"]}http://{host}:{port}{self.colors["reset"]} ...')
                print(f'If you want to quit/stop the process press ctrl+c ...')
                print(f'I am waiting :) ...')
                httpd.serve_forever()
                break
            except OSError as e:
                print(f"Port {port} is already in use, trying the next one...")
    
    def create_or_edit_data(self, pk=None, data=None):
        if not data:
            data = self.form_config
        
        data_dict = {}
        for form_dict in data:
            name = form_dict['name']
            value = form_dict['value']
            data_dict[name] = value

        if not pk:
            try:
                self.db_obj.store_data(**data_dict)
            except Exception as e:
                print(f"[-] Error occur: {e}")
                return False
        else:
            try:
                self.db_obj.update_data(search_tuple=('id', pk), **data_dict)
            except Exception as e:
                print(f"[-] Error occur: {e}")
                return False
            
        return True

    def verify_form(self, filled_data, edit=False, pk=None, factory=False):

        def verify_data(data_dict, p_id=None):
            statues = []
            errors = []
            for form_dict in self.form_config:
                required = form_dict.get('required', False)
                name = form_dict['name']
                title = form_dict['title']
                # pick value from request dict
                if isinstance(data_dict.get(name), list):
                    value = data_dict.get(name, [''])[0]
                else:
                    value = data_dict.get(name, '')

                current_pk = None
                if p_id:
                    try:
                        current_pk = pk[int(p_id) - 1]
                    except Exception:
                        current_pk = None

                #validate for unique field
                unique = form_dict.get('unique', False)
                if unique and not edit and not factory and self.db_obj.read_data(**{name: value}):
                    statues.append(False)
                    errors.append(f'Data for {title} already exists!')
                elif unique and edit and not factory:
                    searched_data = self.db_obj.read_data(**{name: value})
                    invalid = False
                    for data in searched_data:
                        if data['id'] != pk:
                            invalid = True
                    if invalid:
                        statues.append(False)
                        errors.append(f'Data for {title} already exists!')

                #for factory:
                elif unique and current_pk is not None:
                    searched_data = self.db_obj.read_data(**{name: value})
                    invalid = False
                    for data in searched_data:
                        if data['id'] != current_pk:
                            invalid = True
                    if invalid:
                        statues.append(False)
                        errors.append(f'Data for {title} already exists!')

                #verify required and it's values here
                if required and not value:
                    statues.append(False)
                    errors.append(f'{title} field is required.')
                else:
                    statues.append(True)
                
                form_dict['value'] = value

            #custom validation.
            if self.custom_validation_func:
                try:
                    statues, errors = self.custom_validation_func(filled_data, statues, errors)
                except Exception as e:
                    print('[-] Error Occur inside custom validation function ...')
                    print(e)

            return data_dict, statues, errors
        
        statues = []
        errors = []
        factory_data = []
        if factory:
            for data_key, data_dict in filled_data.items():
                data, st, er = verify_data(data_dict, data_key)

                updated_data = []
                for f_config_dict in self.form_config:
                    name = f_config_dict['name']
                    new_dict = copy.copy(f_config_dict)
                    new_dict['value'] = data[name][0] if data.get(name) else ''
                    updated_data.append(new_dict)
                factory_data.append(updated_data)
                
                statues.extend(st)
                errors.extend(er)
        else:
            _, st, er = verify_data(filled_data)

            statues.extend(st)
            errors.extend(er)

        status = all(statues)

        if not status:
            self.make_html(errors=errors, edit=edit, factory_data=factory_data)
        
        return status, factory_data

    def make_html(self, errors=[], edit=False, factory_data=None):

        def update_form_group(form_groups, form_dict, index):
            field_type = form_dict['type']
            name = form_dict['name']
            title = form_dict.get('title', name.title())

            field_id = f'{self.form_field_prefix}-{index}'

            #add kwargs for field
            kwargs = {'id': field_id, 'name': name}

            hidden = False
            if form_dict.get('required', False):
                kwargs['required'] = 'true'
            if form_dict.get('value', None):
                kwargs['value'] = form_dict['value']
            if form_dict.get('read_only', None):
                kwargs['readonly'] = 'true'
            if form_dict.get('hidden', None):
                kwargs['hidden'] = 'true'
                hidden = True
            
            style = ''
            if hidden:
                style = 'style="display: none !important;"'

            label = f'<label for="{field_id}">{title}</label>'
            field = generate_input_field(field_type=field_type, **kwargs)

            form_group = f'<div class="ne-field-group" {style}>{label}{field}</div>'
            form_groups += form_group
            return form_groups

        def generate_input_field(field_type, **kwargs):
            val = ''
            if kwargs.get('value', None) and field_type in ['textarea']:
                val = kwargs.pop('value')
            
            attributes = ' '.join(f'{key}="{value}"' for key, value in kwargs.items())
            
            if field_type == 'text':
                field = f'<input type="text" {attributes} />'
            elif field_type == 'email':
                field = f'<input type="email" {attributes} />'
            elif field_type == 'password':
                field = f'<input type="password" {attributes} />'
            elif field_type == 'number':
                field = f'<input type="number" {attributes} />'
            elif field_type == 'tel':
                field = f'<input type="tel" {attributes} />'
            elif field_type == 'url':
                field = f'<input type="url" {attributes} />'
            elif field_type == 'range':
                field = f'<input type="range" {attributes} />'
            elif field_type == 'checkbox':
                field = f'<input type="checkbox" {attributes} />'
            elif field_type == 'radio':
                field = f'<input type="radio" {attributes} />'
            elif field_type == 'file':
                field = f'<input type="file" {attributes} />'
            elif field_type == 'submit':
                field = f'<input type="submit" {attributes} />'
            elif field_type == 'button':
                field = f'<button {attributes}></button>'
            elif field_type == 'textarea':
                field = f'<textarea {attributes}>{val}</textarea>'
            elif field_type == 'select':
                options = kwargs.pop('options', [])
                selected = kwargs.pop('value', None)
                attributes2 = ' '.join(f'{key}="{value}"' for key, value in kwargs.items())
                options_html = ''.join(f'<option value="{opt}"{" selected" if str(opt)==str(selected) else ""}>{opt}</option>' for opt in options)
                field = f'<select {attributes2}>{options_html}</select>'
            else:
                field = f'<input type="{field_type}" {attributes} />'
            
            return field

        html_title = "Add Data"
        button_title = "Add"
        if edit:
            html_title = "Edit Data"
            button_title = "Update"

        form_groups = ''
        if factory_data:
            for p_index, cf_data in enumerate(factory_data, start=1):
                fr_group = ''
                for index, form_dict in enumerate(cf_data, start=1):
                    index = f'{p_index}-{index}'

                    fr_dict = copy.copy(form_dict)
                    fr_dict['name'] = f'{p_index}__{fr_dict["name"]}'

                    fr_group = update_form_group(fr_group, fr_dict, index)

                form_groups += f'<div class="ne-factory-group">{fr_group}</div>'
        else:
            for index, form_dict in enumerate(self.form_config, start=1):
                form_groups = update_form_group(form_groups, form_dict, index)

        form = f'<form method="post" action="/submit" class="nebulae-form">{form_groups} <button class="sub-btn" type="submit">{button_title}</button></form>'

        error_string = ''
        if errors:
            tp_string = ''
            for msg in errors:
                tp_string += f'<li>{msg}</li>'
            error_string = f'<ul class="nebulae-errors">{tp_string}</ul>'

        body = f'<div class="ne-body">{error_string}{form}</div>'

        # keep your inline css behavior
        style_css_list = []
        for css_f in [css_f for css_f in os.listdir(self.css_dir) if css_f.endswith('.css')]:
            with open(self.css_dir / css_f, 'r') as css_f:
                style_css_list.append(css_f.read())

        style_css = '\n'.join(style_css_list)

        html_template = f"""<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{html_title}</title>
                <style>{style_css}</style>
            </head>
            <body>
                {body}
            </body>
            </html>"""
        
        # ensure dir exists for standalone use
        self.run_dir.mkdir(parents=True, exist_ok=True)
        with open(self.html_path, 'w', encoding='utf-8') as html_f:
            html_f.write(html_template)

        return True
    
    def request_data(self, update_obj=None):

        common_json = []
        for form_j in self.form_jsons:
            try:
                with open(form_j, 'r', encoding='utf-8') as jf:
                    temp_json = json.load(jf)
            except:
                temp_json = []
            common_json.extend(temp_json)

        #for update
        pk=None
        edit=False
        if update_obj:
            for j_dict in common_json:
                if update_obj.get(j_dict['name']):
                    j_dict['value'] = update_obj.get(j_dict['name'])
            pk = update_obj['id']
            edit = True

        #important
        self.form_config = common_json

        self.make_html(edit=edit)
        self.start_http_server(index_html_file=self.html_path, pk=pk, parent=self)
    
    def get_obj(self, **kwargs):
        if not kwargs:
            print('[-] Please provide search data to update the data.')
            return
        try:
            search_obj = self.db_obj.get_data(**kwargs)
        except AttributeError as e:
            print('[-] Error occur while fetching the data, likely no match found, or invalid colomn name.')
            return
        if not search_obj:
            print(f'[-] No data found with search data ({kwargs})')
            return
        return search_obj

    def add(self):
        self.request_data()

    def update(self, **kwargs):
        search_obj = self.get_obj(**kwargs)
        if search_obj:
            self.request_data(update_obj=search_obj[0])

    def request_data_factory(self, update_objs, prefill_dict=None):

        common_json = []
        for form_j in self.form_jsons:
            try:
                with open(form_j, 'r', encoding='utf-8') as jf:
                    temp_json = json.load(jf)
            except:
                temp_json = []
            common_json.extend(temp_json)

        #for update
        filled_configs = []
        pks = []
        edit = True

        for up_key, up_obj in update_objs.items():
            pk = None
            c_j = copy.deepcopy(common_json)
            if up_obj:
                for j_dict in c_j:
                    if up_obj.get(j_dict['name']):
                        j_dict['value'] = up_obj.get(j_dict['name'])
                pk = up_obj['id']

            
            if prefill_dict and prefill_dict.get(up_key):
                p_dict = prefill_dict.get(up_key)
                for j_dict in c_j:
                    name = j_dict['name']
                    if p_dict.get(name):
                        j_dict['value'] = p_dict.get(name)

            filled_configs.append(c_j)
            pks.append(pk)

        #for update

        #important
        self.form_config = common_json

        self.make_html(edit=edit, factory_data=filled_configs)
        self.start_http_server(index_html_file=self.html_path, pk=pks, parent=self)

    def add_or_update_factory(self, search_config, prefill_data=None):
        found_data = {}
        prefill_dict = {}

        if prefill_data and not (len(prefill_data) == len(search_config)):
            print('[-] When providing prefill_data you must make it same length of search_config.')
            return

        for index, search_conf in enumerate(search_config, start=1):
            search_obj = self.get_obj(**search_conf)
            if search_obj:
                found_data[search_obj[0]['id']] = search_obj[0]
            else:
                found_data[f'NONE_{index}'] = None

            if prefill_data:
                current_prefill = prefill_data[index - 1]
                if not search_obj:
                    prefill_dict[f'NONE_{index}'] = current_prefill
        
        self.request_data_factory(found_data, prefill_dict)

    def view(self):
        #future
        pass

    def delete(self):
        #future
        pass