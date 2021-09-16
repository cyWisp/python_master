#!/usr/bin/env python
import os, sys, argparse

def append(f, script_code):

    try:
        with open(f, 'a') as script_template:
            script_template.write(script_code)
    except:
        print('[x] Something went wrong...')
    finally:
        script_template.close()

def validate_path(target_path):

    if os.path.exists(target_path) == True:
        pass
    else:
        print('[x] Path does not exist...\n[!]Exiting...')
        sys.exit(0)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('script_name', type=str, default='new', help='Script Name')
    parser.add_argument('-t', '--target_dir', type=str, help='Target Directory...')
    args = parser.parse_args()
    
    if args.target_dir:
        validate_path(args.target_dir)
        script_path = str.join('/', (args.target_dir, args.script_name)) 
    else:
        script_path = str.join('', ('./', args.script_name))

    script_path = str.join('', (script_path, '.py'))
    create_script = 'touch {0}'.format(script_path)
    python_template = """#!/usr/bin/env python
import os, sys, argparse

def some_function():

    print("Hello, Wisp...")

if __name__ == '__main__':
        
    some_function()
"""

    os.system(create_script)
    append(script_path, python_template)

    print('[*] Created {0}...'.format(script_path))
    sys.exit(0)