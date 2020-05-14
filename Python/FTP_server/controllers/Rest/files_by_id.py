from flask import request
from flask_restful import Resource
from services.ftp_core import StorageService
from models.file_response import FileResponse


class FilesById(Resource):
    def __init__(self, storage_service: StorageService, **kwargs):
        self.logger = kwargs.get('logger')
        self.storage = storage_service

    def get(self, file_id):
        data = self.storage.get_file(file_id)
        for encoding in ['utf-8', 'latin-1', 'ascii']:
            try:
                decoded_data = data.decode(encoding)
                return FileResponse(file_id, decoded_data).get_response()
            except UnicodeDecodeError:
                self.logger.error(f"Failed to decode {encoding} data of: {file_id}")
        return f"Server can't decode file data: {file_id}", 500

    def put(self, file_id):
        data = request.files['file'].read()
        self.storage.save_file(file_id, data)
        return FileResponse(file_id).get_response()

    def delete(self, file_id):
        try:
            self.storage.delete_file(file_id)
            return FileResponse(file_id)
        except FileNotFoundError as err:
            self.logger.error(err)
            result = FileResponse(file_id).get_response()
            result['error'] = str(err)
            return result, 404
