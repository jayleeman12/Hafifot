from os import path as p
from ftp_core.file_controller import FileController


class LocalFtpClient:
    def __init__(self, controller: FileController):
        self.file_controller = controller

    def save_file(self, source_file: str, output_filename: str):
        with open(source_file, 'rb') as f:
            data = f.read()

        self.file_controller.save_file(output_filename, data)

    def get_dir_content(self, path: str):
        return self.file_controller.list_dir(path)

    def get_file_content(self, path: str):
        return self.file_controller.get_file(path).decode('utf-8')
