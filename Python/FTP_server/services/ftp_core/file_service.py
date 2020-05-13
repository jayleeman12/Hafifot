import os
from ftp_core.file_controller import FileController


class FileService(FileController):
    def __init__(self, source_dir):
        source_dir = os.path.abspath(source_dir)
        super().__init__(source_dir)
        if not os.path.isdir(source_dir):
            os.makedirs(source_dir)

    def save_file(self, filename, file_data):
        file_path = os.path.join(self.source_dir, filename)
        file_dir = os.path.split(file_path)[0]
        if not os.path.isdir(file_dir):
            os.makedirs(file_dir)
        with open(file_path, 'wb') as f:
            f.write(file_data)

    def list_dir(self, root_dir='.'):
        if root_dir:
            file_path = os.path.join(self.source_dir, root_dir)
        else:
            file_path = self.source_dir
        return os.listdir(os.path.abspath(file_path))

    def get_file(self, filename):
        file_path = os.path.join(self.source_dir, filename)
        with open(file_path, 'rb') as f:
            data = f.read()
        return data

    def delete_file(self, filename):
        os.remove(filename)
