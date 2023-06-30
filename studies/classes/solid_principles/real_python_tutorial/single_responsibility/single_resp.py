#!/usr/bin/env python

import logging
from pathlib import Path
from zipfile import ZipFile

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


class FileManager:
    def __init__(self, file_name):
        self.path = Path(file_name)

    def read(self, encoding='utf-8'):
        return self.path.read_text(encoding)

    def write(self, data, encoding='utf-8'):
        self.path.write_text(data, encoding)

    def append(self, data, encoding='utf-8'):
        with self.path.open('a') as f:
            f.write(f'\n{data}')


class ZipFileManager:
    def __init__(self, file_name=None, file_list=None, archive_name=None):
        self.path = Path(file_name) if file_name else None
        self.file_list = [Path(x) for x in file_list] if file_list else None
        self.archive_name = archive_name if archive_name else None

    def compress(self):
        with ZipFile(self.path.with_suffix('.zip'), mode='w') as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix('.zip'), mode='r') as archive:
            archive.extractall()

    def compress_many(self):
        with ZipFile(self.archive_name.with_suffix('.zip'), mode='w') as archive:
            for file in self.file_list:
                archive.write(file)


if __name__ == '__main__':
    # file_manager = FileManager('some_file.txt')
    #
    # file_manager.write('this is some test data')
    # file_manager.append('this is some appended text.')

    zip_file_manager = ZipFileManager(
        archive_name='test',
        file_list=['file_1.txt', 'file_2.txt', 'file_3.txt']
    )

    zip_file_manager.compress()