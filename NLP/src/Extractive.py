from transformers import pipeline

class Extractive:
    model_name = "deepset/tinyroberta-squad2"
    nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
    questionsPath="./questions/questions.json"
    
    def __init__(self, queries):
        self.queries = queries

    def query_context(self, question, context):
        QA_input = {
            'question': question,
            'context': context
        }
        res = self.nlp(QA_input)
        return res['answer']

    def get_text_field_labels(self, context):
        question = self.queries["text_field_labels"]
        return self.query_context(question, context)

    def get_date_field_labels(self, context):
        question = self.queries["date_field_labels"]
        return self.query_context(question, context)
    
    def get_integer_field_labels(self, context):
        question = self.queries["integer_field_labels"]
        return self.query_context(question, context)

    def get_enum_field_labels(self, context):
        question = self.queries["enum_field_labels"]
        return self.query_context(question, context)

    def get_boolean_field_labels(self, context):
        question = self.queries["boolean_field_labels"]
        return self.query_context(question, context)
    
    def get_number_of_fields(self, context):
        question = self.queries["number_of_fields"]
        return self.query_context(question, context)
    
    def get_component_type(self, context):
        question = self.queries["component_type"]
        return self.query_context(question, context)

    def get_all_labels(self):
        question = self.queries["all_labels"]
        return self.query_context(question)

    def get_orientation(self, context):
        question = self.queries["orientation"]
        resp = self.query_context(question, context)
        if resp == "vertical":
            return "VerticalLayout"
        else: 
            return "HorizontalLayout"
    
    def get_fields_to_switch(self, context):
        question = self.queries["switch_fields"]
        return self.query_context(question, context)