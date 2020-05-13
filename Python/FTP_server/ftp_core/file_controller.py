
class FileController:
    def __init__(self, source_dir):
        self.source_dir = source_dir

    def save_file(self, filename, file_data):
        raise NotImplementedError

    def get_all_files(self, root_dir):
        raise NotImplementedError

    def get_file(self, filename):
        raise NotImplementedError
