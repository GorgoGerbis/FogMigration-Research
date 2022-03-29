one_multi_p1_passed = [64, 56, 54.6, 47, 39.5, 26.6, 14.6]
one_multi_p2_passed = [64, 64, 68, 53, 61, 54.3, 38]

two_multi_p1_passed = [48, 54, 49.3, 48, 40, 24.3, 13.2]
two_multi_p2_passed = [68, 58, 58.6, 61, 63, 55, 36.4]

three_multi_p1_passed = [56, 46, 44, 50, 37, 30, 16.6]
three_multi_p2_passed = [56, 56, 49.3, 57, 59, 57, 35.8]

four_multi_p1_passed = [44, 42, 49.3, 42, 33, 24.6, 14.6]
four_multi_p2_passed = [48, 54, 57.3, 51, 59.5, 50, 36.2]

five_multi_p1_passed = [48, 54, 52, 51, 35.5, 24.33, 16.4]
five_multi_p2_passed = [60, 70, 64, 66, 61, 54.33, 36.2]

def average_data(one, two, three, four, five):
    output = []
    for i in range(7):
        current = one[i] + two[i] + three[i] + four[i] + five[i]
        current = current / 5
        output.append(current)

    return output


if __name__ == '__main__':
    print("Averaging out number of graphs passed\n")
    p1_passed_avgs = average_data(one_multi_p1_passed, two_multi_p1_passed, three_multi_p1_passed, four_multi_p1_passed, five_multi_p1_passed)
    p2_passed_avgs = average_data(one_multi_p2_passed, two_multi_p2_passed, three_multi_p2_passed, four_multi_p2_passed, five_multi_p2_passed)
    print("multi_p1_passed_avgs = {}\n".format(p1_passed_avgs))
    print("multi_p2_passed_avgs = {}\n".format(p2_passed_avgs))