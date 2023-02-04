import os
import random

from truck_delivery_problem.config import FIELD_LIMIT, NUMBER_OF_COORDINATES


class Setup:

    def __init__(self):
        self.path_to_data = os.getcwd() + "/data/delivery_locations.csv"
        self.locations = []

    def load_coordinates(self):
        locations = []
        f = open(self.path_to_data, "r")
        for line in f:
            locations = self.add_coordinate(line, locations)
        self.locations = locations

    def add_coordinate(self, line, locations):
        split_line = line.strip().split(",")
        x = split_line[0]
        y = split_line[1]
        locations.append((x, y))
        return locations

    def generate_coordinates(self, number_of_coordinates):
        f = open(self.path_to_data, "a")
        for i in range(number_of_coordinates):
            random_x = random.randint(0,FIELD_LIMIT )+ round(random.random(),4)
            random_y = random.randint(0,FIELD_LIMIT )+ round(random.random(),4)
            f.writelines("{},{}\n".format(random_x, random_y))
        f.close()


setup = Setup()
if os.path.exists(setup.path_to_data):
    if (os.stat(setup.path_to_data).st_size == 0):
        setup.generate_coordinates(NUMBER_OF_COORDINATES)
setup.load_coordinates()
print(f"Useable coordinates: {setup.locations}")
print()
