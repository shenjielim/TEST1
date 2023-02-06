import time

from truck_delivery_problem.setup import setup
import numpy as np
from sklearn.cluster import KMeans


# Write your answer here
def get_shortest_distance(number_of_trucks, locations):
    # Modify code below
    X = np.array(locations)
    kmeans = KMeans(number_of_trucks, n_init="auto").fit(X)
    locations_dict = {}
    for i in range(len(locations)):
        if kmeans.labels_[i] not in locations_dict.keys():
            locations_dict[kmeans.labels_[i]] = [locations[i]]
        else:
            locations_dict[kmeans.labels_[i]] += [locations[i]]

    distance_dict = {}
    for cluster_num in locations_dict.keys():
        distance_dict[cluster_num] = calculate_distance(locations_dict[cluster_num])
    print(distance_dict)

    return [x for x in locations_dict.values()]
    # Code ends here




def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            current_k = arr[k - 1]
            if i + j == 0:
                arr[k] = R[j]
                j += 1
            elif vector_distance(L[i], current_k) <= vector_distance(R[j], current_k):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def calculate_distance(coordinates):
    mergeSort(coordinates)
    distance = 0
    for location_num in range(len(coordinates) - 1):
        distance += vector_distance(coordinates[location_num], coordinates[location_num + 1])
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
        print(f'Time taken: {toc - tic:0.4f}s')
        print()
        # Pass contents as arguments for test functions
        return None
