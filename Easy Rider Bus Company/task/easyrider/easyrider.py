import json
from type_validation import TypeValidation
from format_validation import FormatValidation


class DataValidation:
    def __init__(self):
        self.json_text = ''
        self.json_data = None
        self.type_errors = TypeValidation()
        self.format_errors = FormatValidation()

    def read(self):
        self.json_text = input()
        self.json_data = json.loads(self.json_text)

    def validate_type_required(self):
        self.read()
        self.type_errors.validate(self.json_data)
        self.type_errors.print()

    def validate_format(self):
        self.read()
        self.format_errors.validate(self.json_data)
        self.format_errors.print()


validation = DataValidation()
validation.validate_format()
