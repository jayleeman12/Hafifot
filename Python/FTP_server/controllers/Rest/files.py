from flask import request, jsonify
from flask_restful import Resource
from services.ftp_core import file_controller


class Files(Resource):
    def __init__(self, storage_service: file_controller):
        self.storage = storage_service

    def get(self):
        return self.storage.list_dir()

    def post(self):
        f = request.files['file']
        file_name = f.filename
        data = f.read()
        self.storage.save_file(file_name, data)
        return jsonify({"filename": file_name})
