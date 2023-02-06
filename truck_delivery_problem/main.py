from app import App
from config import *


def main():
    app1 = App(
        TEST_NAME_1,
        NUMBER_OF_TRUCKS_1,
        NUMBER_OF_LOCATIONS_1)
    app1.run()

    app2 = App(
        TEST_NAME_2,
        NUMBER_OF_TRUCKS_2,
        NUMBER_OF_LOCATIONS_2)
    app2.run()

    app3 = App(
        TEST_NAME_3,
        NUMBER_OF_TRUCKS_3,
        NUMBER_OF_LOCATIONS_3)
    app3.run()

    # app4 = App(
    #     TEST_NAME_4,
    #     NUMBER_OF_TRUCKS_4,
    #     NUMBER_OF_LOCATIONS_4)
    # app4.run()

if __name__ == "__main__":
    main()
