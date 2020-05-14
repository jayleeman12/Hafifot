
class FileResponse:
    def __init__(self, filename, data=None):
        self.filename = filename
        self.data = data

    def get_response(self):
        result = {
            "filename": self.filename,
        }

        if self.data:
            result["data"] = self.data

        return result
