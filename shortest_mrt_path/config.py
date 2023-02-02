from setup import setup

# MRT lines
lines = setup.mrt_lines

# Test Case 1 Params
test_name_1 = "Test case 1"
start_mrt_1 = "Khatib"
end_mrt_1 = "Ang Mo Kio"
mrt_lines_1 = {"Red": lines["Red"]}

# Test Case 2 Params
test_name_2 = "Test case 2"
start_mrt_2 = "Marina Bay"
end_mrt_2 = "Dhoby Ghaut"
mrt_lines_2 = {"Circle Extension": lines["Circle Extension"], "Orange": lines["Orange"]}

# Test Case 3 Params
test_name_3 = "Test case 3"
start_mrt_3 = "Khatib"
end_mrt_3 = "Kovan"
mrt_lines_3 = {"Circle Extension": lines["Circle Extension"], "Orange": lines["Orange"], "Red": lines["Red"], "Purple": lines["Purple"]}
