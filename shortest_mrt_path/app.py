import time
import json


# Write your answer here
def get_shortest_mrt_path(start_mrt, end_mrt, mrt_lines):
    # Modify code below
    stations = objectify_mrt(mrt_lines)

    train = Train(start_mrt, end_mrt, stations)
    train.construct_path_with()
    return list(map(lambda stat: stat.name, train.route))
    # Code ends here


class Train:

    def __init__(self, start_mrt, end_mrt, stations):
        self.start_mrt = start_mrt
        self.end_mrt = end_mrt
        self.stations = stations
        self.route = []
        for station in self.stations:
            if station.name == self.start_mrt:
                self.route.append([station])
                self.start_mrt = station
            if station.name == self.end_mrt:
                self.end_mrt = station

    def construct_path_with(self):
        future_route = []
        for station in self.route[-1]:
            for next_station in station.connected_to:
                if self.not_in_route(next_station, self.route):
                    future_route.append(next_station)
                if self.end_mrt == next_station:
                    correct_route = self.mark_route(self.end_mrt)
                    self.route = correct_route
                    return None
        self.route.append(future_route)
        self.construct_path_with()

    def not_in_route(self, next_station, route):
        for step in route:
            if next_station in step:
                return False
        return True

    def mark_route(self, end_mrt):
        marked_route = []
        marked_route.append(end_mrt)
        for i in range(len(self.route)):
            for connected_station in end_mrt.connected_to:
                if connected_station in self.route[-i]:
                    marked_route.append(connected_station)
                    end_mrt = connected_station
                    break
        marked_route.append(self.start_mrt)
        self.route = []
        return  list(reversed(marked_route))


class Station:

    def __init__(self, name, color):
        self.name = name
        self.color = [color]
        self.connected_to = []

    def toJson(self):
        return json.dumps(self.print_objects(), sort_keys=True, indent=4)

    def connect(self, station):
        self.connected_to.append(station)

    def print_objects(self):
        return {
            'name': self.name,
            'color': self.color,
            'connected_to': list(map(lambda station: station.name, self.connected_to))
        }


def objectify_mrt(mrt_lines):
    stations = []
    # Creating station objects
    for color, color_stations in mrt_lines.items():
        for station in color_stations:
            station_exists = False
            for station_obj in stations:
                if station == station_obj.name:
                    station_exists = True
                    station_obj.color.append(color)
            if not station_exists:
                stations.append(Station(station, color))

    # forming links between station objects
    for color, color_stations in mrt_lines.items():
        for station_num in range(len(color_stations)):
            for station_obj in stations:
                if color_stations[station_num] == station_obj.name:

                    # Add previous station
                    if station_num != 0:
                        for previous_station in stations:
                            if previous_station.name == color_stations[station_num - 1]:
                                station_obj.connect(previous_station)

                    # Add next station
                    if station_num != len(color_stations) - 1:
                        for next_station in stations:
                            if next_station.name == color_stations[station_num + 1]:
                                station_obj.connect(next_station)

    return stations


class App:
    def __init__(self, test_name, start_mrt, end_mrt, mrt_lines):
        self.test_name = test_name
        self.start_mrt = start_mrt
        self.end_mrt = end_mrt
        self.mrt_lines = mrt_lines

    def run(self):
        # For loop each test case and read contents
        print("Executing " + self.test_name)
        print(f"Start: {self.start_mrt} --> End: {self.end_mrt}")
        print(f"Mrt lines: {', '.join(self.mrt_lines.keys())}")
        tic = time.perf_counter()
        result = get_shortest_mrt_path(self.start_mrt, self.end_mrt, self.mrt_lines)
        toc = time.perf_counter()
        print(f"Returned result: {' -> '.join(result)}")
        print(f'Time taken: {toc - tic:0.4f}s')
        print()
        # Pass contents as arguments for test functions
        return None
