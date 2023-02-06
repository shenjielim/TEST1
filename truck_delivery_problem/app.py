import time

from truck_delivery_problem.setup import setup


# Write your answer here
def get_shortest_distance(number_of_trucks, locations):
    # Modify code below
    return [[(1, 1), (2, 2)], [(1, 1), (2, 2)]]
    # Code ends here


def calculate_total_distance(coordinates_list):
    distance = 0
    for location_num in range(len(coordinates_list)):
        for index in range(len(coordinates_list[location_num]) - 1):
            distance += vector_distance(coordinates_list[location_num][index],
                                        coordinates_list[location_num][index + 1])
    return distance


def vector_distance(l, r):
    x_diff = (l[0] - r[0])
    y_diff = (l[1] - r[1])
    return (x_diff ** 2 + y_diff ** 2) ** 0.5


class App:
    def __init__(self, test_name, number_of_trucks, number_of_locations):
        self.test_name = test_name
        self.number_of_trucks = number_of_trucks
        self.number_of_locations = number_of_locations

    def run(self):
        # For loop each test case and read contents
        print("Executing " + self.test_name)
        print(f"Number of trucks: {self.number_of_trucks}")
        print(f"Number of locations: {self.number_of_locations}")
        print(f"Coordinates: {setup.locations[:self.number_of_locations]}")
        tic = time.perf_counter()
        result = get_shortest_distance(self.number_of_trucks, setup.locations[:self.number_of_locations])
        toc = time.perf_counter()
        for i in range(len(result)):
            print(f"Returned truck path {i + 1}: {' -> '.join([str(x) for x in result[i]])}")
        print(f'Total distance : {calculate_total_distance(result)}')
        print(f'Time taken: {toc - tic:0.4f}s')
        print()
        # Pass contents as arguments for test functions
        return None
