from fields import Fields
import re


class FormatValidation:
    def __init__(self):
        self.json_data = None
        self.errors = {}

    def initialize_errors(self):
        self.errors[Fields.stop_name] = 0
        self.errors[Fields.stop_type] = 0
        self.errors[Fields.a_time] = 0

    def validate(self, json_data):
        self.initialize_errors()
        self.json_data = json_data
        for item in self.json_data:
            self.validate_item(item)

    def validate_item(self, item):
        self.validate_stop_name(item)
        self.validate_stop_type(item)
        self.validate_time(item)

    def validate_stop_name(self, item):
        value = item[Fields.stop_name]
        name_pattern = "^([A-Z][a-zA-Z]+ )+(Avenue|Road|Boulevard|Street)$"
        is_match = re.search(name_pattern, value)
        if not is_match:
            self.errors[Fields.stop_name] += 1

    def validate_stop_type(self, item):
        value = item[Fields.stop_type]
        type_pattern = "^(S|O|F)$"
        is_match = re.search(type_pattern, value)
        if value != "" and not is_match:
            self.errors[Fields.stop_type] += 1

    def validate_time(self, item):
        value = item[Fields.a_time]
        time_pattern = "^(([0-1][0-9])|(2[0-4])):([0-5][0-9])$"
        is_match = re.search(time_pattern, value)
        if not is_match:
            self.errors[Fields.a_time] += 1

    def print(self):
        print(f"Format validation: {sum(self.errors.values())} errors")
        for key, value in self.errors.items():
            print(f"{key}: {value}")
