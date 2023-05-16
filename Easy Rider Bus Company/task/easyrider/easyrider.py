from fields import Fields
from type_validation import TypeValidation
from format_validation import FormatValidation
from bus_entities import BusLinesReader, BusStop, BusLine


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
        for line in self.lines.values():
            validation = line.validate_stops()
            if validation:
                print(validation)
                return False
        return True

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

    def get_stops_by_type(self, stop_type: str):
        for line in self.lines.values():
            for stop in line.stops:
                if stop.stop_type == stop_type:
                    yield stop.name

    def get_transfers(self):
        stops_count = {}

        for line in self.lines.values():
            for stop in line.stops:
                if stop.stop_id not in stops_count:
                    stops_count[stop.stop_id] = 0
                stops_count[stop.stop_id] += 1

                if stops_count[stop.stop_id] > 1:
                    yield stop.name

    def print_stops_grouped(self):
        start_stops = set(self.get_stops_by_type("S"))
        transfer_stops = set(self.get_transfers())
        end_stops = set(self.get_stops_by_type("F"))
        print(f"Start stops: {len(start_stops)} {sorted(start_stops)}")
        print(f"Transfer stops: {len(transfer_stops)} {sorted(transfer_stops)}")
        print(f"End stops: {len(end_stops)} {sorted(end_stops)}")

    def print_stops_number(self):
        print(f"Line names and number of stops:")
        for key, value in self.lines.items():
            print(f"bus_id: {key}, stops: {len(value.stops)}")


easy_rider = EasyRider()
if easy_rider.process():
    easy_rider.print_stops_grouped()
