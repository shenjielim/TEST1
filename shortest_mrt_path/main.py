from app import App
from config import *


def main():
    app1 = App(test_name_1, start_mrt_1, end_mrt_1, mrt_lines_1)
    app2 = App(test_name_2, start_mrt_2, end_mrt_2, mrt_lines_2)
    app3 = App(test_name_3, start_mrt_3, end_mrt_3, mrt_lines_3)
    app1.run()
    app2.run()
    app3.run()


if __name__ == "__main__":
    main()
