import os
import random
import config


class Setup:

    def __init__(self):
        self.path = os.getcwd()
        self.max_items = config.MAX_ITEMS
        self.max_quantity = config.MAX_QUANTITY

    def create_test(self, test_path, test_number):
        os.makedirs(test_path)

    def setup_test(self, number_of_tests=5):
        for i in range(1, number_of_tests):
            test_path = self.path + "/test_" + str(i)
            print(f'created directory {test_path}')
            exist = os.path.exists(test_path)
            if not exist:
                self.create_test(test_path, i)

            if not os.path.exists(test_path + "/test_" + str(i) + ".py"):
                self.create_random_test_case(i)

    def create_random_test_case(self, test_number):
        test_name = "/test_" + str(test_number)
        f = open(self.path + str(test_name) * 2 + ".txt", "a")
        random_items = random.randint(1, self.max_items)
        store = []
        for i in range(random_items):
            random_quantity = random.randint(1, self.max_quantity)
            store.append(random_quantity)
        lines = [",".join([str(x) for x in store]) + "\n", str(random.randint(1, sum(store)))]
        f.writelines(lines)
        f.close()


setup = Setup()
setup.setup_test()
