
class StorageService:
    def __init__(self):
        pass

    def save_file(self, filename, file_data):
        raise NotImplementedError

    def list_dir(self, root_dir):
        raise NotImplementedError

    def get_file(self, filename):
        raise NotImplementedError

    def delete_file(self, filename):
        raise NotImplementedError
