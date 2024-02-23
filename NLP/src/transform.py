from pydantic import RootModel
from file_handler import file_handler
from models.JsonForms.Fields import StringField, DateField, BooleanField, EnumField, IntegerField
from models.JsonForms.Schema import Schema
from models.Intermediate.Labels import Labels
from models.JsonForms.UiSchema import UiSchema, Ele
from Extractive import Extractive
from rich import print

class transform:
    schema_path     = "../jsonforms-react-seed/src/schema.json"
    ui_schema_path  = "../jsonforms-react-seed/src/uischema.json"
    questions_path  = "./src/questions/questions.json"
    # context         = "Create me a form component with four text fields, with labels of Username and Confirm Password and Password and Email Address. Arrange them in a vertical layout."
    # context         = "Create a form with three text fields labelled Username, Confirm Password and Password and a date field with the label Due Date. Arrange them in a vertical layout."
    properties      = {}
    questions       = {}

    def __init__(self, context):
        self.file_handler   = file_handler(
            questions_path  = self.questions_path,
            schema_path     = self.schema_path,
            ui_schema_path  = self.ui_schema_path
        )
        self.context       = context
        self.questions     = self.file_handler.read_questions()
        self.extractive    = Extractive(context=self.context, queries=self.questions["extractive"])

        self.compute()

    def get_orientation(self, layout):
        if layout == "vertical":
            return "VerticalLayout"
        else: 
            return "HorizontalLayout"
        
    """Method for creating the layout schema"""
    def create_layout(self, labels, orientation):
        layoutObj       = UiSchema("", [])
        layoutObj.type  = self.get_orientation(orientation)

        elements = []
        all_labels = labels.string_labels + labels.date_labels + labels.boolean_labels
        for _, value in enumerate(all_labels):
            label       = f"{value}" 
            ele         = Ele(label=value, type="Control", scope="#/properties/" + label.lower())
            elements.append(ele)

        layoutObj.elements = elements
        return layoutObj
    
    def create_string_field(self, label):
        return StringField()

    def create_date_field(self, label):
        return DateField()

    def splitList(self, list_of_lables):
        list_of_lables = list_of_lables.replace(' and', ',')
        list_of_lables = list_of_lables.split(',')
        return [string.replace(' ', '') for string in list_of_lables]

    """Method for creating the field schema"""
    def create_field_schema(self, labels):
        properties={}
        for _, value in enumerate(labels.string_labels):
            properties[value.lower()] = StringField()

        for _, value in enumerate(labels.date_labels):
            properties[value.lower()] = DateField()

        for _, value in enumerate(labels.boolean_labels):
            properties[value.lower()] = BooleanField()

        for _, value in enumerate(labels.enum_labels):
            properties[value.lower()] = EnumField()

        for _, value in enumerate(labels.integer_labels):
            properties[value.lower()] = IntegerField()
        
        return properties

    def generate_UI(self, labels, orientation): 
        prop            = self.create_field_schema(labels)
        fieldsJSON      = Schema(type="object", properties=prop)
        uiJSON          = self.create_layout(labels, orientation)

        self.file_handler.write_schema(RootModel[Schema](fieldsJSON).model_dump_json(indent=4), self.schema_path)
        self.file_handler.write_schema(RootModel[UiSchema](uiJSON).model_dump_json(indent=4), self.ui_schema_path)

    def compute(self):
        text_field_labels = self.extractive.get_text_field_labels()
        date_field_labels = self.extractive.get_date_field_labels()
        # enum_field_labels = self.extractive.get_enum_field_labels()
        boolean_field_labels = self.extractive.get_boolean_field_labels()
        # integer_field_labels = self.extractive.get_integer_field_labels()
        # get_all_labels    = self.extractive.get_all_labels()
        # number_of_fields  = self.extractive.get_number_of_fields()
        string_labels = self.splitList(text_field_labels)
        date_labels = self.splitList(date_field_labels)
        # enum_labels=self.splitList(enum_field_labels)
        boolean_labels=self.splitList(boolean_field_labels)
        # integer_labels=self.splitList(integer_field_labels)

        labels = Labels(
            string_labels=string_labels, 
            date_labels=date_labels,
            integer_labels=[],
            enum_labels=[],
            boolean_labels=boolean_labels
            )
        print(labels)
        orientation        = self.extractive.get_orientation()

        # print(labels)
        # component_type     = self.extractive.query_context(self.questions["component_type"])['answer']
        # labels             = self.extractive.query_context(self.questions["list_labels"])['answer']
        self.generate_UI(labels, orientation=orientation)

def main():
    user_input = input("Enter a string: ")

    transform(user_input)

if __name__ == "__main__":
    main()