from fields import Fields
from type_validation import TypeValidation
from format_validation import FormatValidation
from bus_entities import BusLinesReader, BusStop, BusLine, LinesValidation


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


class EasyRider:
    def __init__(self):
        self.lines = {}

    def process(self):
        json_data = BusLinesReader.read()
        for item in json_data:
            self.process_lines(item)

        LinesValidation.validate_ondemand_stops(self.lines.values())

    def process_lines(self, item):
        line_id = item[Fields.id]
        if line_id not in self.lines:
            self.lines[line_id] = BusLine(line_id)

        bus_stop = BusStop(
            item[Fields.stop_id],
            item[Fields.stop_name],
            item[Fields.next_stop],
            item[Fields.stop_type],
            item[Fields.a_time])

        self.lines[line_id].stops.append(bus_stop)

    def print_stops_number(self):
        print(f"Line names and number of stops:")
        for key, value in self.lines.items():
            print(f"bus_id: {key}, stops: {len(value.stops)}")


easy_rider = EasyRider()
easy_rider.process()
