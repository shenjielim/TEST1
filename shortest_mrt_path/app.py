import time


# Write your answer here
def get_shortest_mrt_path(mrt_lines, start_mrt, end_mrt):
    # Modify code below
    return []
    # Code ends here


class App:
    def __init__(self, test_name, start_mrt, end_mrt, mrt_lines):
        self.test_name = test_name
        self.start_mrt = start_mrt
        self.end_mrt = end_mrt
        self.mrt_lines = mrt_lines

    def run(self):
        # For loop each test case and read contents
        print("Executing " + self.test_name)
        print(f"Start: {self.start_mrt} --> End: {self.end_mrt}")
        print(f"Mrt lines: {', '.join(self.mrt_lines.keys())}")
        tic = time.perf_counter()
        result = get_shortest_mrt_path(self.start_mrt, self.end_mrt, self.mrt_lines)
        toc = time.perf_counter()
        print(f"Returned result: {'->'.join(result)}")
        print(f'Time taken: {toc - tic:0.4f}s')
        print()
        # Pass contents as arguments for test functions
        return None
