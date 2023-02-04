import time

from truck_delivery_problem.setup import setup


# Write your answer here
def get_shortest_distance(number_of_trucks, locations):
    # Modify code below
    return []
    # Code ends here


class App:
    def __init__(self, test_name, number_of_trucks, number_of_locations):
        self.test_name = test_name
        self.number_of_trucks = number_of_trucks
        self.number_of_locations = number_of_locations

    def run(self):
        # For loop each test case and read contents
        print("Executing " + self.test_name)
        print(f"Number of trucks: {self.number_of_trucks}" )
        print(f"Number of locations: {self.number_of_locations}")
        print(f"Coordinates: {setup.locations[:self.number_of_locations]}")
        tic = time.perf_counter()
        result = get_shortest_distance(self.number_of_trucks, setup.locations[:self.number_of_locations])
        toc = time.perf_counter()
        print(f"Returned result: {'->'.join(result)}")
        print(f'Time taken: {toc - tic:0.4f}s')
        print()
        # Pass contents as arguments for test functions
        return None
