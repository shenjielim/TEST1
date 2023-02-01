import os
import time


# Write your answer here
def calculate_revenue(items_list, number_of_customers):
    # Modify code below
    mergeSort(items_list)
    max_quantity = items_list[0]
    revenue = 0
    current_index = 0
    for customer_num in range(number_of_customers):
        current_item = items_list[current_index]
        if current_item < max_quantity:
            current_index = 0
            current_item = items_list[current_index]
            max_quantity = current_item
        revenue += current_item

        # Post purchase
        items_list[current_index] = current_item - 1
        current_index += 1

    return revenue
    # Code ends here


# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr)//2

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
            if L[i] >= R[j]:
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




class app:
    def __init__(self):
        self.path = "."

    def run(self):
        # For loop each test case and read contents
        for test_folder in os.listdir(os.curdir):
            if os.path.isdir(test_folder) and test_folder.startswith("test_"):
                test_path = test_folder + "/" + test_folder + ".txt"
                f = open(test_path, "r")
                lines = f.readlines()
                items_list = [int(x) for x in lines[0].strip().split(",")]
                number_of_customers = int(lines[1])
                print("Executing " + test_folder)
                print(f"List of items start: {items_list}")
                result = calculate_revenue(items_list, number_of_customers)
                print(f"List of items end: {items_list}")
                print("Number of customers: " +  str(number_of_customers))
                print("Returned result: " + str(result))
                print()
                f.close()
        # Pass contents as arguments for test functions
        return None
