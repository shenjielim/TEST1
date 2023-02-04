import os


class Setup:

    def __init__(self):
        self.path = os.getcwd()
        self.mrt_lines = {}


    def setup_mrt_lines(self):
        mrt_lines = {}
        f = open(self.path+ "/data/sg_mrt.csv", "r")
        for line in f:
            mrt_lines = self.add_lines(line, mrt_lines)
        self.mrt_lines = mrt_lines
    def add_lines(self,line,mrt_lines):
        split_line = line.strip().split(",")
        color = split_line[0]
        mrt_stations = split_line[1:]
        mrt_lines[color] = mrt_stations
        return mrt_lines

setup = Setup()
setup.setup_mrt_lines()
print(f"Useable MRT lines: {', '.join(setup.mrt_lines.keys())}")
print()
