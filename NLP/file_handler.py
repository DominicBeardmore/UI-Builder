import json

class file_handler:
    def __init__(self, questions_path, ui_schema_path, schema_path):
        self.questions_path = questions_path
        self.ui_schema_path = ui_schema_path
        self.schema_path = schema_path

    def read_questions(self):
        with open(self.questions_path, 'r') as file:
            return json.load(file)

    def write_schema(self, json, path):
        f = open(path, "w")
        f.write(json)
        f.close()
