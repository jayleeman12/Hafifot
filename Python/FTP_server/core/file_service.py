from os import path, listdir, makedirs
from core.file_controller import FileController


class FileService(FileController):
    def save_file(self, filename, file_data):
        file_path = path.join(self.source_dir, filename)
        makedirs(path.split(file_path)[0])
        with open(file_path, 'wb') as f:
            f.write(file_data)

    def get_all_files(self, root_dir='.'):
        return listdir(path.join(self.source_dir, root_dir))

    def get_file(self, filename):
        file_path = path.join(self.source_dir, filename)
        with open(file_path, 'rb') as f:
            data = f.read()
        return data
