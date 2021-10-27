import json
import string


class Fields:
    id = 'bus_id'
    stop_id = 'stop_id'
    stop_name = 'stop_name'
    next_stop = 'next_stop'
    stop_type = 'stop_type'
    a_time = 'a_time'
    required = (id, stop_id, stop_name, next_stop, a_time)


class DataValidation:
    def __init__(self):
        self.json_text = ''
        self.json_data = None
        self.errors = {}

    def read(self):
        self.json_text = input()
        self.json_data = json.loads(self.json_text)

    def initialize_errors(self):
        self.errors[Fields.id] = 0
        self.errors[Fields.stop_id] = 0
        self.errors[Fields.stop_name] = 0
        self.errors[Fields.next_stop] = 0
        self.errors[Fields.stop_type] = 0
        self.errors[Fields.a_time] = 0

    def validate(self):
        self.initialize_errors()
        for item in self.json_data:
            self.validate_item(item)

    def validate_item(self, item):
        self.validate_integer(item, Fields.id)
        self.validate_integer(item, Fields.stop_id)
        self.validate_integer(item, Fields.next_stop)
        self.validate_name(item, Fields.stop_name)
        self.validate_time(item, Fields.a_time)
        self.validate_char(item, Fields.stop_type)

    def validate_required(self, item, field_name):
        if field_name in Fields.required:
            if item[field_name] == '':
                self.errors[field_name] += 1

    def validate_integer(self, item, field_name):
        if not isinstance(item[field_name], int):
            self.errors[field_name] += 1

    def validate_char(self, item, field_name):
        if not isinstance(item[field_name], str) or item[field_name] not in string.ascii_letters:
            self.errors[field_name] += 1
        self.validate_required(item, field_name)

    def validate_name(self, item, field_name):
        if not isinstance(item[field_name], str):
            self.errors[field_name] += 1
        self.validate_required(item, field_name)

    def validate_time(self, item, field_name):
        value = item[field_name]
        if not isinstance(value, str):
            self.errors[field_name] += 1
            return
        self.validate_required(item, field_name)
        if ':' not in value:
            return
        hour, minute = value.split(':')

        try:
            hour = int(hour)
            if hour > 24 or hour < 0:
                self.errors[field_name] += 1
        except ValueError:
            self.errors[field_name] += 1

        try:
            minute = int(minute)
            if minute > 59 or minute < 0:
                self.errors[field_name] += 1
        except ValueError:
            self.errors[field_name] += 1

    def print(self):
        print(f"Type and required field validation: {sum(self.errors.values())} errors")
        for key, value in self.errors.items():
            print(f"{key}: {value}")


validation = DataValidation()
validation.read()
validation.validate()
validation.print()
