import json
from fields import Fields
from type_validation import TypeValidation
from format_validation import FormatValidation


class BusLinesReader:
    @staticmethod
    def read():
        json_text = input()
        return json.loads(json_text)


class DataValidation:
    def __init__(self):
        self.type_errors = TypeValidation()
        self.format_errors = FormatValidation()

    def validate_type_required(self):
        data = BusLinesReader.read()
        self.type_errors.validate(data)
        self.type_errors.print()

    def validate_format(self):
        data = BusLinesReader.read()
        self.format_errors.validate(data)
        self.format_errors.print()


class BusLines:
    def __init__(self):
        self.lines = {}

    def process(self):
        json_data = BusLinesReader.read()
        for item in json_data:
            self.process_line(item)

    def process_line(self, item):
        line_id = item[Fields.id]
        if line_id not in self.lines:
            self.lines[line_id] = 0

        self.lines[line_id] += 1

    def print(self):
        print(f"Line names and number of stops:")
        for key, value in self.lines.items():
            print(f"bus_id: {key}, stops: {value}")


bus_lines = BusLines()
bus_lines.process()
bus_lines.print()
