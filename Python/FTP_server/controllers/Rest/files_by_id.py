from flask import request
from flask_restful import Resource


class FilesById(Resource):
    def post(self):
        f = request.files['file']
        file_name = f.filename


