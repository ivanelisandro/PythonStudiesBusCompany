import json


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

    def validate_stops(self):
        start = sum(1 for stop in self.stops if stop.stop_type == "S")
        final = sum(1 for stop in self.stops if stop.stop_type == "F")
        if start < 1 or final < 1:
            return f"There is no start or end stop for the line: {self.line_id}."
        if start > 1 or final > 1:
            return f"There are too many start or end stops for the line: {self.line_id}."
        return None
