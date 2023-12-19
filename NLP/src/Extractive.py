from transformers import pipeline

class Extractive:
    model_name = "deepset/tinyroberta-squad2"
    nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
    questionsPath="./questions/questions.json"
    
    def __init__(self, context, queries):
        self.context =  context
        self.queries = queries

    def query_context(self, question):
        QA_input = {
            'question': question,
            'context': self.context
        }
        res = self.nlp(QA_input)
        return res['answer']

    def get_text_field_labels(self):
        question = self.queries["text_field_labels"]
        return self.query_context(question)

    def get_date_field_labels(self):
        question = self.queries["date_field_labels"]
        return self.query_context(question)
    
    def get_integer_field_labels(self):
        question = self.queries["integer_field_labels"]
        return self.query_context(question)

    def get_enum_field_labels(self):
        question = self.queries["enum_field_labels"]
        return self.query_context(question)

    def get_boolean_field_labels(self):
        question = self.queries["boolean_field_labels"]
        return self.query_context(question)
    
    def get_number_of_fields(self):
        question = self.queries["number_of_fields"]
        return self.query_context(question)
    
    def get_component_type(self):
        question = self.queries["component_type"]
        return self.query_context(question)

    def get_all_labels(self):
        question = self.queries["all_labels"]
        return self.query_context(question)

    def get_orientation(self):
        question = self.queries["orientation"]
        return self.query_context(question)