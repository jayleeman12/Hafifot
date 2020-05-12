from os import path as p
from core.file_controller import FileController


class LocalFtpClient:
    def __init__(self, controller: FileController):
        self.file_controller = controller

    def save_file(self, file_path, filename):
        with open(file_path, 'rb') as f:
            data = f.read()

        self.file_controller.save_file(filename, data)

    def get(self, path):
        if p.isdir(path):
            self.file_controller.get_all_files(path)
        else:
            self.file_controller.get_file(path)
