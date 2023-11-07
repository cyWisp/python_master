#!/usr/bin/env python
from configargparse import get_argument_parser
import os, sys, logging

parser = get_argument_parser(name='default')

parser.add_argument('-p', '--project-name', type=str, default='template',
                    help='Name of project.')

logging.basicConfig(
    format='%(process)d - %(asctime)s - %(levelname)s: %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO,
    handlers=[logging.StreamHandler(sys.stdout)]
)

log = logging.getLogger()

cfg, unknown = parser.parse_known_args()


class Project:
    PROJECT_DIRS = {
        'assets_folder': 'assets',
        'js_folder': 'assets/js',
        'css_folder': 'assets/css',
        'images_folder': 'assets/images'
    }

    PROJECT_FILES = {
        'index': f'''<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
        <link rel=\"stylesheet\" href=\"{os.path.join(PROJECT_DIRS["css_folder"], "style.css")}\">
    </head>
    <body>
        <p>Hello, Template!</p>
    
        <script type="text/javascript" src=\"{os.path.join(PROJECT_DIRS["js_folder"], "script.js")}\"></script>
    </body>
</html>
''',
        'script': '''\"use strict\";
    
function main () {
    console.log("Hello, World!");
}
        
document.onload = main();
''',
        'style': '''/* Styles go here. */
        
p {
    color: red;
}
'''
    }

    def __init__(self, project_name: str):
        self.project_name = project_name
        self.index_path = os.path.join(project_name, 'index.html')
        self.css_path = os.path.join(project_name, f'{self.PROJECT_DIRS["css_folder"]}/style.css')
        self.js_path = os.path.join(project_name, f'{self.PROJECT_DIRS["js_folder"]}/script.js')

    def create_project_dirs(self):
        for dir in self.PROJECT_DIRS.values():
            project_dir = os.path.join(self.project_name, dir)
            if not os.path.exists(project_dir):
                log.info(f'Creating {project_dir}')
                os.makedirs(project_dir)

    def write_file(self, file_name, content):
        try:
            log.info(f'Writing {file_name}.')

            with open(file_name, 'w') as f:
                f.write(content)

        except (FileNotFoundError, IOError) as e:
            log.setLevel(logging.ERROR)
            log.error(f'Unable to write {file_name} | {e.__class__.__name__}')

    def create_project_files(self):
        self.write_file(self.index_path, self.PROJECT_FILES['index'])
        self.write_file(self.js_path, self.PROJECT_FILES['script'])
        self.write_file(self.css_path, self.PROJECT_FILES['style'])


if __name__ == '__main__':
    log.info(f'Creating new project: {cfg.project_name}')

    new_project = Project(cfg.project_name)
    new_project.create_project_dirs()
    new_project.create_project_files()

