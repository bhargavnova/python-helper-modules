from utils.better_get_and_store_data import BetterGetAndStoreData
from utils.simple_json_storage import SimpleJsonStorage
from pathlib import Path
import json
import argparse

# storage
storage_path = Path(__file__).parent / 'registered_commands.json'
db_obj = SimpleJsonStorage(storage_path)
db_obj.load()

# form config
lang_name = 'python'
current_dir = Path(__file__).parent
form_jsons = []

demo_form = current_dir / 'demo_form.json'
if not demo_form.exists():
    demo_fields = [
        {"name": "name", "title": "Name", "type": "text", "required": True, "unique": True},
        {"name": "trigger", "title": "Trigger", "type": "text", "required": True, "unique": True},
        {"name": "description", "title": "Description", "type": "textarea"},
        {"name": "tags", "title": "Tags (comma)", "type": "text"},
        {"name": "script_dir", "title": "Script Dir", "type": "text", "required": True},
        {"name": "trigger_script", "title": "Trigger Script", "type": "text", "required": True},
        {"name": "args", "title": "Args", "type": "text"}
    ]
    demo_form.write_text(json.dumps(demo_fields, indent=2), encoding='utf-8')
form_jsons = [demo_form]

# assets
css_dir = current_dir / 'server_utils' / 'css'
run_dir = current_dir / 'server_utils' / 'html'
css_dir.mkdir(parents=True, exist_ok=True)
run_dir.mkdir(parents=True, exist_ok=True)

# ui
obj = BetterGetAndStoreData(
    from_key=lang_name,
    form_jsons=form_jsons,
    db_obj=db_obj,
    css_dir=css_dir,
    run_dir=run_dir
)

# CLI
parser = argparse.ArgumentParser(description="Open local form to add/update a record")
parser.add_argument("-u", "--update", type=int, help="Update existing record by id")
args = parser.parse_args()

if args.update is not None:
    obj.update(id=args.update)
else:
    obj.add()