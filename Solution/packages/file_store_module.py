"""File Store module"""
import os
from Hafifot.Solution.packages.error_module import AlreadyExistsError
from Hafifot.Solution.packages.file_module import *


class FileStore(object):
    """Base class for File Store in this module."""
    def __init__(self):
        self.dict_of_files = {}

    # Save a new file in the store
    def store_file(self, file):
        if file.get_name() in self.dict_of_files:
            raise AlreadyExistsError('File Already Exists')
        self.dict_of_files[file.get_name()] = file

    # Getters & Setters
    def get_dict_of_files(self):
        return self.dict_of_files

    def set_dict_of_files(self, dict_of_files: dict):
        self.dict_of_files = dict_of_files

    # Find a specific file in the store by file name
    def get_file(self, file_name: str):
        return self.dict_of_files[file_name]

    # Delete a file from the store
    def delete_file(self, file_name: str):
        del self.dict_of_files[file_name]

    # Read file from store function prototype
    def read_file(self):
        pass


class OSFileStore(FileStore):
    """OS File Store class, inherits from FileStore"""
    def __init__(self, file_store_path: str):
        super().__init__()
        self.path = file_store_path
        os.mkdir(file_store_path)

    # Save a new file in the store
    def store_file(self, file: TextIO, file_path: str):
        new_file = OSFile(file.name, 'OS', f'{self.path}/{file_path}')
        try:
            super().store_file(new_file)
            new_file.write(file)
        except AlreadyExistsError as e:
            print(e.message)

    # Getters & Setters
    def get_dict_of_files(self):
        return super().get_dict_of_files()

    def set_dict_of_files(self, dict_of_files: dict):
        super().set_dict_of_files(dict_of_files)

    def get_file_store_path(self):
        return self.path

    def set_file_store_path(self, file_store_path: str):
        self.path = file_store_path

    # Find a specific file in the store by file name
    def get_file(self, file_name: str):
        return super().get_file(file_name)

    # Print a file content from the store
    def read_file(self, file_name: str):
        self.get_file(file_name).read()

    # Delete a file from the store
    def delete_file(self, file_name: str):
        os.remove(self.get_file(file_name).get_file_path())
        super().delete_file(file_name)
