import logging
import json

logging.basicConfig(level=logging.INFO, format='%(message)s')
log = logging.getLogger()
log.name = 'default'

# List of text files
files = []


def read_file(file_name: str) -> list:
    try:
        log.info(f'Reading {file_name}.')

        with open(file_name) as f:
            return [x.replace('\n', '') for x in f.readlines()]

    except (IOError, FileNotFoundError) as e:
        log.error(f'File read failed:\n{e}', exc_info=True)


def output_json(file_name: str, content: list) -> None:
    try:
        log.info(f'Writing {file_name}.')

        with open(file_name, 'w') as f:
            json.dump(content, f)

    except (IOError, FileNotFoundError) as e:
        log.error(f'Unable to write file:\n{e}', exc_info=True)


def convert_title(file_name: str) -> list:
    try:
        log.info(f'Reading {file_name}.')

        with open(file_name) as f:
            return [x.title() for x in json.load(f)]

    except (IOError, FileNotFoundError) as e:
        log.error(f'Unable to read file:\n{e}', exc_info=True)


if __name__ == '__main__':
    # for f in files:
    #     output_json(f'{f.split(".")[0]}.json', read_file(f))

    # output_json('last-names.json', convert_title('last-names.json'))
    # output_json(f'{"street-names.txt".split(".")[0]}.json', read_file("street-names.txt"))
