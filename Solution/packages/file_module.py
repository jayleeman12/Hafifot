"""File module"""
from typing import TextIO


class File:
    """Base class for file module"""
    def __init__(self, name: str, file_type: str):
        self.name = name
        self.type = file_type

    # Getters & Setters
    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_type(self):
        return self.type

    def set_type(self, file_type: str):
        self.type = file_type

    # Read file function prototype
    def read(self):
        pass

    # Write file function prototype
    def write(self):
        pass


class OSFile(File):
    """OS File class. inherits from File"""
    def __init__(self, name: str, file_type: str, file_path: str):
        super().__init__(name, file_type)
        self.file_path = file_path

    # Getters & Setters
    def get_name(self):
        return super().get_name()

    def set_name(self, name: str):
        super().set_name(name)

    def get_type(self):
        return super().get_type()

    def set_type(self, file_type: str):
        super().set_type(file_type)

    def get_file_path(self):
        return self.file_path

    def set_file_path(self, file_path: str):
        self.file_path = file_path

    # Read file function, print the content
    def read(self):
        with open(f'{self.file_path}', 'r') as file:
            for line in file:
                print(line)

    # Write a file to the FileSystem
    def write(self, file_to_write: TextIO):
        with open(f'{self.file_path}', 'w') as saved_file:
            for line in file_to_write:
                saved_file.write(line)
