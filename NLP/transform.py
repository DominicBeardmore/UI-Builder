from pydantic import RootModel
from models import Layout, Ele, StrEle, Schema
from file_handler import file_handler
from Interrogate import Interrogate

class transform:
    schema_path="./jsonforms-react-seed/src/schema.json"
    ui_schema_path="./jsonforms-react-seed/src/uischema.json"
    questions_path="./NLP/questions.json"

    context = "Create me a form component with three text fields, with labels of Username and Email and Password. Arrange them in a vertical layout."
    properties = {}
    questions = {}

    def __init__(self):
        self.interrogate = Interrogate(context=self.context)
        self.file_handler = file_handler(
            questions_path=self.questions_path,
            schema_path=self.schema_path,
            ui_schema_path=self.ui_schema_path
        )
        self.questions = self.file_handler.read_questions()
        self.compute()

    def create_layout(self, numOfFields, componentType, labels, layout):
        layoutObj = Layout("", [])
        layoutObj.type = self.interrogate.get_orientation(layout)

        elements = []
        for index, value in enumerate(labels):
            label = f"{value}" 
            ele = Ele()
            ele.label = label
            ele.type = "Control"
            ele.scope = "#/properties/" + label.lower()
            elements.append(ele)

        layoutObj.elements = elements
        return layoutObj

    def create_properties_array(self, labels):
        properties = {}
        for index, value in enumerate(labels):
            label = f"{value}"  # Dynamic label based on index
            properties[label.lower()] = StrEle()

        return properties

    def generate_UI(self, numOfFields, componentType, labels, layout): 
        labels = labels.split(' and ')
        propertiesDict = self.create_properties_array(labels)
        fieldsJSON = Schema(type="object", properties=propertiesDict)
        uiJSON = self.create_layout(numOfFields, componentType, labels, layout)

        self.file_handler.write_schema(RootModel[Schema](fieldsJSON).model_dump_json(indent=4), self.schema_path)
        self.file_handler.write_schema(RootModel[Layout](uiJSON).model_dump_json(indent=4), self.ui_schema_path)

    def compute(self):
        number_of_fields = self.interrogate.query_context(self.questions["num_of_fields"])['answer']
        component_type = self.interrogate.query_context(self.questions["component_type"])['answer']
        orientation = self.interrogate.query_context(self.questions["orientation"])['answer']
        labels = self.interrogate.query_context(self.questions["list_labels"])['answer']

        self.generate_UI(number_of_fields, component_type, labels, orientation)

transform()