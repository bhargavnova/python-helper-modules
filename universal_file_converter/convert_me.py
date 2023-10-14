import importlib.util
import os, json
import argparse
import sys
import inspect
import yaml

""" importing all the modules and config data to execute without modifying this script """
#well might have still don't know yet!
#anyway hope you use this script often and it can be useful for you.

"""
    if you are reading this, you don't have to modify anything here
    just make sure you add function in format (covert_{ext1}_to_{ext2}) with the same name folder
    other wise either the function will not run, or script will break haha (well that's not good, I will have to check what when worng if that happens)
"""

def _exec_modules():
    #import all the function dynamically
    #do not modify thi function

    for dir in os.listdir(utils_dir):
        if not dir.endswith('.py'):
            module_files = [f for f in os.listdir(os.path.join(utils_dir, dir)) if 'convert_' in f and f.endswith('.py')]
            if module_files:
                file_name = module_files[0]
                module_name = os.path.splitext(file_name)[0]
                spec = importlib.util.spec_from_file_location(module_name, os.path.join(utils_dir, dir, file_name))
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                modules[module_name] = module

def _load_configs():
    global configs
    with open(config_file) as cf:
        configs = yaml.safe_load(cf)

class ListFunctions(argparse.Action):
    #just to print dynamic list of all the function outside from the script.
    #trying to avoid modification of this script :)
    def __call__(self, parser, namespace, values, option_string=None):
        print("Listing all supported functions:")
        with open(func_txt, 'r') as r_f:
            help_text = r_f.read() + '\n\n'
        print(help_text)
        setattr(namespace, self.dest, values)

def get_user_args():
    parser = argparse.ArgumentParser(description="Single script to convert different types of file.")
    parser.add_argument('-f', '--function', type=str, help='Enter Conversation Function Name Format {ext1}-{ext2}, (EX: srt-lrc)')
    parser.add_argument('-i', '--input', type=str, help='input file path , file.ext1')
    parser.add_argument('-o', '--output', type=str, help='output file path, file.ext2')
    parser.add_argument('-l', '--list', type=str, nargs=0, action=ListFunctions, help='list all supported functions')
    args = parser.parse_args()
    return args

if __name__ == "__main__":

    """do not modify this variables"""
    main_utils = '_my_utils'
    config_file = os.path.join(main_utils, 'config.yml')
    utils_dir = os.path.join(main_utils, '_utils')
    func_txt = os.path.join(main_utils, 'func_list.txt')
    modules = {}
    configs = None

    args = get_user_args()
    funtion_name = args.function
    input_path = args.input
    output_path = args.output

    if (funtion_name and input_path and output_path):
        #process further

        #check input and output file
        if (input_path == output_path):
            print('[+] input/ouput file cannot be same...')
            sys.exit()

        #check function name and it's existance.
        try:
            search_function = f'convert_{funtion_name.split("-")[0]}_to_{funtion_name.split("-")[1]}'
        except:
            print('[+] please enter valid function name, {ext1}-{ext2}')
            sys.exit()

        #load modules (exec all the modules dynamically)
        _exec_modules()
        if not modules.get(search_function):  #check if function exists in modules
            print('[+] added function does not exists ....')
            sys.exit()

        _load_configs() #(load config file from the .json)

        module_name = configs.get(search_function) #check if funtion exists in config
        if not module_name:
            print('[+] Function does not exists in config .....')
            sys.exists()

        #get class or function in valibale called unknown (hahaha because we still have to figure that out)
        unknown = getattr(modules.get(search_function), module_name)
        
        #let's find what we are dealing with (function or class)
        if not inspect.isfunction(unknown):

            #it's class
            #for class now i will have to get main method from it, which is the search_function, 
            #which is provided by the user in format {ext1}-{ext2}
            obj = unknown(input_path, output_path)
            func = getattr(obj, search_function)
            func() #call the main function (method) from class
        else:

            #it's function
            #then it's simple just called he unkown function and parse the input and output file path
            #and see the magic happens.
            unknown(input_path, output_path)