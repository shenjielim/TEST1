import os
import re


# Write your answer here
def calculate_revenue(items_list, number_of_customers):
    # Modify code below
    return 1
    # Code ends here


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
                result = calculate_revenue(items_list, number_of_customers)
                print(f"List of items: {items_list}")
                print("Number of customers: " +  str(number_of_customers))
                print("Returned result: " + str(result))
                print()
                f.close()
        # Pass contents as arguments for test functions
        return None
