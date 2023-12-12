from transformers import pipeline
from models import StrEle

class Interrogate:
    model_name = "deepset/tinyroberta-squad2"
    nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
    questionsPath="./questions.json"
    
    def __init__(self, context):
        self.context =  context

    def query_context(self, question):
        QA_input = {
            'question': question,
            'context': self.context
        }
        res = self.nlp(QA_input)
        return res

    def get_number_of_fields(self):
        question = "How many string fields are there in this request?"
        return self.query_context(question)

    def get_type_of_component(self):
        question = "What kind of component do they want?"
        return self.query_context(question)

    def get_field_labels(self):
        question = "List the labels for each of fields in the prompt?"
        return self.query_context(question)

    def get_field_layout(self):
        question = "How do they want the form laid out? Vertically or Horizontally?"
        return self.query_context(question)
    
    def get_str_ele(self):
        return StrEle(type="string", minLength=1)

    def get_orientation(self, layout):
        if layout == "vertical":
            return "VerticalLayout"
        else: 
            return "HorizontalLayout"