import json


class FileService:

    def __init__(self, file_name):
        self.file_name = file_name

    def load_from_file(self):
        try:
            return open(self.file_name, 'r').read()
        except Exception as ex:
            return None

    def save_to_file(self, data):
        try:
            return open(self.file_name, 'w').write(data)
        except Exception:
            return None


class JsonFileService(FileService):

    def __init__(self, file_name):
        super().__init__(file_name)

    def load_data(self):
        try:
            return json.loads(self.load_from_file())
        except Exception:
            return None

    def save_data(self, data):
        return self.save_to_file(json.dumps(data))
