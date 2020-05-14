from flask import jsonify, request
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
                return jsonify({"filename": file_id, "data": decoded_data})
            except UnicodeDecodeError:
                self.logger.error(f"Failed to decode {encoding} data of: {file_id}")
        return "Server can't decode file data", 500

    def put(self, file_id):
        data = request.files['file'].read()
        self.storage.save_file(file_id, data)
        return jsonify(FileResponse(file_id))
