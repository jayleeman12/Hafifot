from flask import Flask
from flask_restful import Api
from controllers.Rest import files, files_by_id
from services.ftp_core import FileService


def create_app():
    file_service = FileService('../data')

    flask_app = Flask(__name__)

    api = Api(flask_app)
    api.add_resource(files.Files, '/files', resource_class_args=[file_service])
    api.add_resource(files_by_id.FilesById, '/files/<string:file_id>')

    return flask_app


if __name__ == '__main__':
    app = create_app()
    app.run()
