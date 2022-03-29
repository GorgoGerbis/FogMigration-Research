import os
import numpy as np
import matplotlib.pyplot as plt

all_fps = [r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_ONE_OUTPUT_DATA_25.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_TWO_OUTPUT_DATA_25.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_ONE_OUTPUT_DATA_50.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_TWO_OUTPUT_DATA_50.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_ONE_OUTPUT_DATA_75.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_TWO_OUTPUT_DATA_75.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_ONE_OUTPUT_DATA_100.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_TWO_OUTPUT_DATA_100.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_ONE_OUTPUT_DATA_200.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_TWO_OUTPUT_DATA_200.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_ONE_OUTPUT_DATA_300.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_TWO_OUTPUT_DATA_300.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_ONE_OUTPUT_DATA_500.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_TWO_OUTPUT_DATA_500.csv",

           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_ONE_OUTPUT_DATA_25.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_TWO_OUTPUT_DATA_25.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_ONE_OUTPUT_DATA_50.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_TWO_OUTPUT_DATA_50.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_ONE_OUTPUT_DATA_75.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_TWO_OUTPUT_DATA_75.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_ONE_OUTPUT_DATA_100.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_TWO_OUTPUT_DATA_100.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_ONE_OUTPUT_DATA_200.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_TWO_OUTPUT_DATA_200.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_ONE_OUTPUT_DATA_300.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_TWO_OUTPUT_DATA_300.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_ONE_OUTPUT_DATA_500.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_TWO_OUTPUT_DATA_500.csv"]

all_fps_multi = [r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_ONE_OUTPUT_DATA_25.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_TWO_OUTPUT_DATA_25.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_ONE_OUTPUT_DATA_50.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_TWO_OUTPUT_DATA_50.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_ONE_OUTPUT_DATA_75.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_TWO_OUTPUT_DATA_75.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_ONE_OUTPUT_DATA_100.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_TWO_OUTPUT_DATA_100.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_ONE_OUTPUT_DATA_200.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_TWO_OUTPUT_DATA_200.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_ONE_OUTPUT_DATA_300.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_TWO_OUTPUT_DATA_300.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_ONE_OUTPUT_DATA_500.csv",
           r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\MULTI_PATH_TWO_OUTPUT_DATA_500.csv"]

all_fps_single = [
    r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_ONE_OUTPUT_DATA_25.csv",
    r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_TWO_OUTPUT_DATA_25.csv",
    r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_ONE_OUTPUT_DATA_50.csv",
    r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_TWO_OUTPUT_DATA_50.csv",
    r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_ONE_OUTPUT_DATA_75.csv",
    r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_TWO_OUTPUT_DATA_75.csv",
    r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_ONE_OUTPUT_DATA_100.csv",
    r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_TWO_OUTPUT_DATA_100.csv",
    r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_ONE_OUTPUT_DATA_200.csv",
    r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_TWO_OUTPUT_DATA_200.csv",
    r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_ONE_OUTPUT_DATA_300.csv",
    r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_TWO_OUTPUT_DATA_300.csv",
    r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_ONE_OUTPUT_DATA_500.csv",
    r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-\output\SINGLE_PATH_TWO_OUTPUT_DATA_500.csv"]

baseFolder = r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-"
resourcesFolder = os.path.join(baseFolder, "resources")
outputFolder = os.path.join(baseFolder, "output")

fail_multi_p1_5 = []
fail_multi_p2_5 = []


def process_input_data(filePath, c):
    num_reqs = [25, 25, 50, 50, 75, 75, 100, 100, 200, 200, 300, 300, 500, 500]

    with open(filePath) as fp:
        name = filePath[73:]
        fp.readline()
        fp.readline()
        avg = fp.readline()
        averages = avg.split(',')
        num_passed = averages[0]
        avg_delay = averages[2]
        avg_cost = averages[3]
        avg_fail = averages[4]

        #print("{} | num passed = {} | avg delay = {} | avg cost = {} | avg fail prob = {}\n".format(name, num_passed, avg_delay, avg_cost, avg_fail))
        fp.close()
        return int(num_passed) / num_reqs[c], float(avg_delay), float(avg_cost)


if __name__ == '__main__':
    single_p1_passed = []
    single_p2_passed = []

    multi_p1_passed = []
    multi_p2_passed = []

    single_p1_delays = []
    single_p2_delays = []

    multi_p1_delays = []
    multi_p2_delays = []

    single_p1_costs = []
    single_p2_costs = []

    multi_p1_costs = []
    multi_p2_costs = []

    count = 0
    zap = 0

    for f in all_fps_single:
        current_num_passed, avg_delay, avg_cost = process_input_data(f, count)

        if count == 0:
            single_p1_passed.append(current_num_passed)
            single_p1_delays.append(avg_delay)
            single_p1_costs.append(avg_cost)
        elif count % 2 == 0:
            single_p1_passed.append(current_num_passed)
            single_p1_delays.append(avg_delay)
            single_p1_costs.append(avg_cost)
        else:
            single_p2_passed.append(current_num_passed)
            single_p2_delays.append(avg_delay)
            single_p2_costs.append(avg_cost)

        count += 1

    for f in all_fps_multi:
        current_num_passed, avg_delay, avg_cost = process_input_data(f, zap)

        if zap == 0:
            multi_p1_passed.append(current_num_passed)
            multi_p1_delays.append(avg_delay)
            multi_p1_costs.append(avg_cost)
        elif zap % 2 == 0:
            multi_p1_passed.append(current_num_passed)
            multi_p1_delays.append(avg_delay)
            multi_p1_costs.append(avg_cost)
        else:
            multi_p2_passed.append(current_num_passed)
            multi_p2_delays.append(avg_delay)
            multi_p2_costs.append(avg_cost)

        zap += 1

    print("two_single_p1_passed = {}\n".format(single_p1_passed))
    print("two_single_p2_passed = {}\n".format(single_p2_passed))

    print("two_single_p1_delays = {}\n".format(single_p1_delays))
    print("two_single_p2_delays = {}\n".format(single_p2_delays))

    print("two_single_p1_costs = {}\n".format(single_p1_costs))
    print("two_single_p2_costs = {}\n".format(single_p2_costs))

    print("----------------------------------------------------------------------\n")

    print("two_multi_p1_passed = {}\n".format(multi_p1_passed))
    print("two_multi_p2_passed = {}\n".format(multi_p2_passed))

    print("two_multi_p1_delays = {}\n".format(multi_p1_delays))
    print("two_multi_p2_delays = {}\n".format(multi_p2_delays))

    print("two_multi_p1_costs = {}\n".format(multi_p1_costs))
    print("two_multi_p2_costs = {}\n".format(multi_p2_costs))