from flask import request, jsonify
from flask_restful import Resource
from services.ftp_core import StorageService
from models.file_response import FileResponse


class Files(Resource):
    def __init__(self, storage_service: StorageService, **kwargs):
        self.logger = kwargs.get('logger')
        self.storage = storage_service

    def get(self):
        return self.storage.list_dir()

    def post(self):
        f = request.files['file']
        file_name = f.filename
        data = f.read()
        self.storage.save_file(file_name, data)
        return jsonify(FileResponse(file_name).get_response())
