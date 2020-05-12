from os import path as p
from core.file_controller import FileController


class LocalFtpClient:
    def __init__(self, controller: FileController):
        self.file_controller = controller

    def save_file(self, file_path: str, filename: str):
        with open(file_path, 'rb') as f:
            data = f.read()

        self.file_controller.save_file(filename, data)

    def get_dir_content(self, path: str):
        return self.file_controller.get_all_files(path)

    def get_file_content(self, path: str):
        return self.file_controller.get_file(path).decode('utf-8')
