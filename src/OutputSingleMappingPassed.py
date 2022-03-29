import os
import numpy as np
import matplotlib.pyplot as plt

baseFolder = r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-"
resourcesFolder = os.path.join(baseFolder, "resources")
outputFolder = os.path.join(baseFolder, "output")

one_single_p1_passed = [64, 62, 64, 52, 59, 41, 22.8]
one_single_p2_passed = [64, 66, 68, 55, 63, 58, 35.6]

two_single_p1_passed = [60, 52, 58.6, 55, 57, 39.3, 22.8]
two_single_p2_passed = [68, 58, 60, 61, 65, 59, 34]

three_single_p1_passed = [56, 56, 46.6, 54, 57, 42.6, 23.4]
three_single_p2_passed = [56, 64, 52, 59, 62, 59, 35.8]

four_single_p1_passed = [44, 52, 57.3, 50, 55.5, 38.6, 22]
four_single_p2_passed = [48, 54, 58.6, 55, 62, 56, 35.4]

five_single_p1_passed = [56, 64, 56, 58, 58.5, 37.66, 26.6]
five_single_p2_passed = [64, 70, 65.33, 67, 63.5, 55.33, 34.8]


def average_data(one, two, three, four, five):
    output = []
    for i in range(7):
        current = one[i] + two[i] + three[i] + four[i] + five[i]
        current = current / 5
        output.append(current)

    return output


if __name__ == '__main__':
    print("Averaging out number of graphs passed\n")
    p1_passed_avgs = average_data(one_single_p1_passed, two_single_p1_passed, three_single_p1_passed, four_single_p1_passed, five_single_p1_passed)
    p2_passed_avgs = average_data(one_single_p2_passed, two_single_p2_passed, three_single_p2_passed, four_single_p2_passed, five_single_p2_passed)
    print("single_p1_passed_avgs = {}\n".format(p1_passed_avgs))
    print("single_p2_passed_avgs = {}\n".format(p2_passed_avgs))