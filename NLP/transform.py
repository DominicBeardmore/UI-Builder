import dataclasses
from transformers import pipeline
from pydantic.dataclasses import dataclass
from pydantic import RootModel
from rich import print
import json


schemaPath="./jsonforms-react-seed/src/schema.json"
uiSchemaPath="./jsonforms-react-seed/src/uischema.json"
model_name = "deepset/tinyroberta-squad2"
context = "Create me a form component with four text fields, with labels of Username and Email and Password and Confirmation Password. Arrange them in a vertical layout."
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
properties = {}

@dataclass
class StrEle:
    type: str ="string"
    minLength: int = 1

@dataclass
class Schema:
    type: str = "object"
    properties: dict[str, StrEle] = None

@dataclass
class Ele:
    type: str = "x"
    scope: str = "x"
    label: str = "x"

@dataclass
class Layout:
    type: str = "VerticalLayout"
    elements: list[Ele] = dataclasses.field(default_factory=lambda: [0])

def interograte(question, context):
    QA_input = {
        'question': question,
        'context': context
    }
    res = nlp(QA_input)
    return res

def numberOfFields():
    question = "How many string fields are there in this request?"
    return interograte(question, context)

def typeOfComponent():
    question = "What kind of component do they want?"
    return interograte(question, context)

def fieldLabels():
    question = "List the labels for each of fields in the prompt?"
    return interograte(question, context)

def fieldLayout():
    question = "How do they want the form laid out? Vertically or Horizontally?"
    return interograte(question, context)

def getStrEle():
    return StrEle(type="string", minLength=1)

def getOrientation(layout):
    if layout == "vertical":
        return "VerticalLayout"
    else: 
        return "HorizontalLayout"

def createLayout(numOfFields, componentType, labels, layout):
    layoutObj = Layout("", [])
    layoutObj.type = getOrientation(layout)

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

def createPropertiesArray(labels):
    for index, value in enumerate(labels):
        label = f"{value}"  # Dynamic label based on index
        properties[label.lower()] = StrEle()

    return properties

def generateUI(numOfFields, componentType, labels, layout): 
    labels = labels.split(' and ')
    propertiesDict = createPropertiesArray(labels)
    fieldsJSON = Schema(type="object", properties=propertiesDict)
    uiJSON = createLayout(numOfFields, componentType, labels, layout)

    writeToFile(RootModel[Schema](fieldsJSON).model_dump_json(indent=4), schemaPath)
    writeToFile(RootModel[Layout](uiJSON).model_dump_json(indent=4), uiSchemaPath)

def writeToFile(json, file):
    f = open(file, "w")
    f.write(json)
    f.close()

def compute():
    numOfFields = numberOfFields()['answer']
    componentType = typeOfComponent()['answer']
    labels = fieldLabels()['answer']
    layout = fieldLayout()['answer']

    generateUI(numOfFields, componentType, labels, layout)

compute()