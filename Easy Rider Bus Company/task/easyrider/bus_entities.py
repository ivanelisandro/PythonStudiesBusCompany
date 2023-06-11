import json
from fields import Fields


class BusStopFilter:
    @staticmethod
    def by_types(lines, stop_types):
        for line in lines:
            for stop in line.stops:
                if stop.stop_type != "" and stop.stop_type in stop_types:
                    yield stop.name

    @staticmethod
    def only_transfers(lines):
        stops_count = {}

        for line in lines:
            for stop in line.stops:
                if stop.stop_id not in stops_count:
                    stops_count[stop.stop_id] = 0
                stops_count[stop.stop_id] += 1

                if stops_count[stop.stop_id] > 1:
                    yield stop.name


class LinesValidation:
    @staticmethod
    def has_error_start_end(lines):
        for line in lines:
            error = line.find_error_start_end()
            if error:
                print(error)
                return False
        return True

    @staticmethod
    def validate_starts_ends(lines):
        if LinesValidation.has_error_start_end(lines):
            LinesValidation.print_stops_grouped(lines)

    @staticmethod
    def print_stops_grouped(lines):
        start_stops = set(BusStopFilter.by_types(lines, "S"))
        transfer_stops = set(BusStopFilter.only_transfers(lines))
        end_stops = set(BusStopFilter.by_types(lines, "F"))
        print(f"Start stops: {len(start_stops)} {sorted(start_stops)}")
        print(f"Transfer stops: {len(transfer_stops)} {sorted(transfer_stops)}")
        print(f"End stops: {len(end_stops)} {sorted(end_stops)}")

    @staticmethod
    def validate_times(lines):
        errors = []
        for line in lines:
            error = line.find_error_time()
            if error:
                errors.append(error)
        LinesValidation.print_times(errors)

    @staticmethod
    def print_times(time_errors):
        print(f"Arrival time test:")
        if time_errors:
            print(*time_errors, sep='\n')
        else:
            print("OK")

    @staticmethod
    def validate_ondemand_stops(lines):
        on_demand = set(BusStopFilter.by_types(lines, "O"))
        start_end = set(BusStopFilter.by_types(lines, "SF"))
        start_end_transfer = start_end.union(BusStopFilter.only_transfers(lines))
        invalid = on_demand.intersection(start_end_transfer)
        LinesValidation.print_invalid_ondemand(invalid)

    @staticmethod
    def print_invalid_ondemand(invalid_stops):
        print(f"On demand stops test:")
        if invalid_stops:
            print(f"Wrong stop type: {sorted(list(invalid_stops))}")
        else:
            print("OK")


class BusLinesReader:
    @staticmethod
    def read():
        json_text = input()
        return json.loads(json_text)


class BusStop:
    def __init__(self, stop_id, name, next_stop, stop_type, time):
        self.stop_id = stop_id
        self.name = name
        self.next_stop = next_stop
        self.stop_type = stop_type
        self.time = time


class BusLine:
    def __init__(self, line_id):
        self.line_id = line_id
        self.stops = []

    def get_stop(self, stop_id):
        for stop in self.stops:
            if stop.stop_id == stop_id:
                return stop
        return None

    def find_error_start_end(self):
        start_count = sum(1 for stop in self.stops if stop.stop_type == "S")
        end_count = sum(1 for stop in self.stops if stop.stop_type == "F")
        if start_count < 1 or end_count < 1:
            return f"There is no start or end stop for the line: {self.line_id}."
        if start_count > 1 or end_count > 1:
            return f"There are too many start or end stops for the line: {self.line_id}."
        return None

    def find_error_time(self):
        for stop in self.stops:
            if stop.stop_type == "F":
                continue
            next_stop = self.get_stop(stop.next_stop)
            if stop.time > next_stop.time:
                return f"{Fields.id} line {self.line_id}: wrong time on station {next_stop.name}"
        return None
