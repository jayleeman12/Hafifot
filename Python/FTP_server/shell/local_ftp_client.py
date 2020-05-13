from services.ftp_core.storage_service import StorageService


class LocalFtpClient:
    def __init__(self, service: StorageService):
        self.storage_service = service

    def save_file(self, source_file: str, output_filename: str):
        with open(source_file, 'rb') as f:
            data = f.read()

        self.storage_service.save_file(output_filename, data)

    def get_dir_content(self, path: str):
        return self.storage_service.list_dir(path)

    def get_file_content(self, path: str):
        return self.storage_service.get_file(path).decode('utf-8')

    def delete_file(self, path: str):
        return self.storage_service.delete_file(path)
