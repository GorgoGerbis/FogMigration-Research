import os
import numpy as np
import matplotlib.pyplot as plt

# plt.rcParams.update({'font.size':15}) @todo need to play with this

baseFolder = r"C:\Users\jacks\Desktop\Research Project\Research-Project---Siasi-"
resourcesFolder = os.path.join(baseFolder, "resources")
outputFolder = os.path.join(baseFolder, "output")

single_pathOne_passed_avgs = [56.0, 57.2, 56.5, 53.8, 57.4, 39.8, 23.5]
single_pathTwo_passed_avgs = [60.0, 62.4, 60.7, 59.4, 63.1, 57.4, 35.1]
# single_pathOne_passed_avgs = [40.0, 40.85, 40.35, 38.42, 41.0, 28.45, 16.8, 14.87, 11.78]
# single_pathTwo_passed_avgs = [42.85, 44.57, 43.41, 42.42, 45.07, 41.04, 25.08, 22.77, 17.82]

multi_pathOne_passed_avgs = [52.0, 50.4, 49.84666666666667, 47.6, 37.0, 25.979333333333336, 15.080000000000002]
multi_pathTwo_passed_avgs = [59.2, 60.4, 59.45333333333333, 57.6, 60.7, 54.126, 36.52]
# multi_pathOne_passed_avgs = [37.14, 36.0, 35.6, 34.0, 26.42, 18.54, 10.77, 10.02, 09.42]
# multi_pathTwo_passed_avgs = [42.28, 43.14, 42.45, 41.14, 43.35, 38.66, 26.08, 23.67, 18.82]

single_pathOne_delays_avgs = [7.444462121212121, 7.73031504785537, 7.940273255813952, 8.013576079093319, 8.28550501369413, 8.423558963642336, 8.38850070397439]
single_pathTwo_delays_avgs = [7.568021708683473, 7.886717505514921, 8.054352109142025, 8.092062874392592, 8.243049855120466, 8.53561906609489, 8.60511108521712]

multi_pathOne_delays_avgs = [11.251718614718616, 11.800574189095931, 11.594331515551028, 12.04327269503546, 11.975647440881616, 11.791071670986058, 12.055551891251184]
multi_pathTwo_delays_avgs = [11.529142857142856, 12.368131499726328, 12.195257966211454, 12.456184883252144, 13.01288587114016, 13.131399130471655, 12.981323493890011]

single_pathOne_costs_avgs = [32.65660173160173, 33.12028092874867, 35.304995973019224, 34.61352660111281, 36.775303952824025, 37.79436290103598, 37.52941678204836]
single_pathTwo_costs_avgs = [33.31967787114846, 33.936820379492794, 35.791579942000105, 35.28086393665057, 36.301227607095015, 38.762391551678874, 39.43912973341258]

multi_pathOne_costs_avgs = [42.981601731601735, 44.69564067172763, 44.854705738998426, 45.73088247213779, 46.8954954332929, 46.60959714509029, 47.40501358860098]
multi_pathTwo_costs_avgs = [43.77464985994398, 46.6744708994709, 46.383398743601205, 47.154488955964624, 50.5402330707591, 53.80636657827874, 54.57688614228107]


def create_bar_graph_COMBO_PASSED(path_one_data_single, path_two_data_single, path_one_data_multi, path_two_data_multi):
    N = 7 # was 5 before figuring out what it does
    ind = np.arange(N)
    width = 0.2
    ax1 = plt.bar(ind, path_one_data_single, width, label='Single Conventional Scheme')
    ax2 = plt.bar(np.add(ind, width), path_two_data_single, width, label='Single Fault-Aware Scheme')

    ax3 = plt.bar(ind+0.4, path_one_data_multi, width, label='Multi Conventional Scheme')
    ax4 = plt.bar(np.add(ind+0.4, width), path_two_data_multi, width, label='Multi Fault-Aware Scheme')

    plt.ylabel('Successful Requests')
    plt.xlabel('Incoming Requests')
    plt.title('Success rates: Conventional mapping Vs. Fault-Aware mapping')

    plt.xticks(ind + width+0.1, ('25 REQ', '50 REQ', '75 REQ', '100 REQ', '200 REQ', '300 REQ', '500 REQ'))
    plt.ylim([0, 100])
    plt.legend(loc='best')

    for bar in ax1:
        height = bar.get_height()
        plt.text(x=bar.get_x() + bar.get_width() / 2, y=height + .10, s="{:.2f}%".format(height), ha='center')

    for bar in ax2:
        height = bar.get_height()
        plt.text(x=bar.get_x() + bar.get_width() / 2, y=height + .10, s="{:.2f}%".format(height), ha='center')

    for bar in ax3:
        height = bar.get_height()
        plt.text(x=bar.get_x() + bar.get_width() / 2, y=height + .10, s="{:.2f}%".format(height), ha='center')

    for bar in ax4:
        height = bar.get_height()
        plt.text(x=bar.get_x() + bar.get_width() / 2, y=height + .10, s="{:.2f}%".format(height), ha='center')

    plt.show()


def create_bar_graph_COMBO_DELAYS(path_one_data_single, path_two_data_single, path_one_data_multi, path_two_data_multi):
    N = 7 # was 5 before figuring out what it does
    ind = np.arange(N)
    width = 0.2
    ax1 = plt.bar(ind, path_one_data_single, width, label='Single Conventional Scheme')
    ax2 = plt.bar(np.add(ind, width), path_two_data_single, width, label='Single Fault-Aware Scheme')

    ax3 = plt.bar(ind+0.4, path_one_data_multi, width, label='Multi Conventional Scheme')
    ax4 = plt.bar(np.add(ind+0.4, width), path_two_data_multi, width, label='Multi Fault-Aware Scheme')

    plt.ylabel('Request Delays')
    plt.xlabel('Incoming Requests')
    plt.title('Average request delays: Conventional mapping Vs. Fault-Aware mapping')

    plt.xticks(ind + width+0.1, ('25 REQ', '50 REQ', '75 REQ', '100 REQ', '200 REQ', '300 REQ', '500 REQ'))
    plt.ylim([0, 20])
    plt.legend(loc='best')

    for bar in ax1:
        height = bar.get_height()
        plt.text(x=bar.get_x() + bar.get_width() / 2, y=height + .10, s="{:.2f}".format(height), ha='center')

    for bar in ax2:
        height = bar.get_height()
        plt.text(x=bar.get_x() + bar.get_width() / 2, y=height + .10, s="{:.2f}".format(height), ha='center')

    for bar in ax3:
        height = bar.get_height()
        plt.text(x=bar.get_x() + bar.get_width() / 2, y=height + .10, s="{:.2f}".format(height), ha='center')

    for bar in ax4:
        height = bar.get_height()
        plt.text(x=bar.get_x() + bar.get_width() / 2, y=height + .10, s="{:.2f}".format(height), ha='center')

    plt.show()


def create_bar_graph_COMBO_COSTS(path_one_data_single, path_two_data_single, path_one_data_multi, path_two_data_multi):
    N = 7 # was 5 before figuring out what it does
    ind = np.arange(N)
    width = 0.2
    ax1 = plt.bar(ind, path_one_data_single, width, label='Single Conventional Scheme')
    ax2 = plt.bar(np.add(ind, width), path_two_data_single, width, label='Single Fault-Aware Scheme')

    ax3 = plt.bar(ind+0.4, path_one_data_multi, width, label='Multi Conventional Scheme')
    ax4 = plt.bar(np.add(ind+0.4, width), path_two_data_multi, width, label='Multi Fault-Aware Scheme')

    plt.ylabel('Request Costs')
    plt.xlabel('Incoming Requests')
    plt.title('Average request costs: Conventional mapping Vs. Fault-Aware mapping')

    plt.xticks(ind + width+0.1, ('25 REQ', '50 REQ', '75 REQ', '100 REQ', '200 REQ', '300 REQ', '500 REQ'))
    plt.ylim([0, 70])
    plt.legend(loc='best')

    for bar in ax1:
        height = bar.get_height()
        plt.text(x=bar.get_x() + bar.get_width() / 2, y=height + .10, s="{:.2f}".format(height), ha='center')

    for bar in ax2:
        height = bar.get_height()
        plt.text(x=bar.get_x() + bar.get_width() / 2, y=height + .10, s="{:.2f}".format(height), ha='center')

    for bar in ax3:
        height = bar.get_height()
        plt.text(x=bar.get_x() + bar.get_width() / 2, y=height + .10, s="{:.2f}".format(height), ha='center')

    for bar in ax4:
        height = bar.get_height()
        plt.text(x=bar.get_x() + bar.get_width() / 2, y=height + .10, s="{:.2f}".format(height), ha='center')

    plt.show()


# def create_bar_graph_SINGLE(path_one_data, path_two_data):
#     N = 7 # was 5 before figuring out what it does
#     ind = np.arange(N)
#     width = 0.35
#     ax1 = plt.bar(ind, path_one_data, width, label='Conventional Scheme')
#     ax2 = plt.bar(np.add(ind, width), path_two_data, width, label='Fault-Aware Scheme')
#     plt.ylabel('Successful Requests')
#     plt.title('Single-Mapping success rates: Conventional mapping Vs. Fault-Aware mapping')
#
#     plt.xticks(ind + width / 2, ('25 REQ', '50 REQ', '75 REQ', '100 REQ', '200 REQ', '300 REQ', '500 REQ'))
#     plt.ylim([0, 100])
#     plt.legend(loc='best')
#
#     for bar in ax1:
#         height = bar.get_height()
#         plt.text(x=bar.get_x() + bar.get_width() / 2, y=height + .10, s="{}%".format(height), ha='center')
#
#     for bar in ax2:
#         height = bar.get_height()
#         plt.text(x=bar.get_x() + bar.get_width() / 2, y=height + .10, s="{}%".format(height), ha='center')
#
#     plt.show()
#
#
# def create_bar_graph_MULTI(path_one_data, path_two_data):
#     N = 7 # was 5 before figuring out what it does
#     ind = np.arange(N)
#     width = 0.35
#     ax1 = plt.bar(ind, path_one_data, width, label='Conventional Scheme')
#     ax2 = plt.bar(np.add(ind, width), path_two_data, width, label='Fault-Aware Scheme')
#     plt.ylabel('Successful Requests')
#     plt.title('Multi-Mapping success rates: Conventional mapping Vs. Fault-Aware mapping')
#
#     plt.xticks(ind + width / 2, ('25 REQ', '50 REQ', '75 REQ', '100 REQ', '200 REQ', '300 REQ', '500 REQ'))
#     plt.ylim([0, 100])
#     plt.legend(loc='best')
#
#     for bar in ax1:
#         height = bar.get_height()
#         plt.text(x=bar.get_x() + bar.get_width() / 2, y=height + .10, s="{}%".format(height), ha='center')
#
#     for bar in ax2:
#         height = bar.get_height()
#         plt.text(x=bar.get_x() + bar.get_width() / 2, y=height + .10, s="{}%".format(height), ha='center')
#
#     plt.show()


if __name__ == '__main__':
    create_bar_graph_COMBO_PASSED(single_pathOne_passed_avgs, single_pathTwo_passed_avgs, multi_pathOne_passed_avgs, multi_pathTwo_passed_avgs)
    create_bar_graph_COMBO_DELAYS(single_pathOne_delays_avgs, single_pathTwo_delays_avgs, multi_pathOne_delays_avgs, multi_pathTwo_delays_avgs)
    create_bar_graph_COMBO_COSTS(single_pathOne_costs_avgs, single_pathTwo_costs_avgs, multi_pathOne_costs_avgs, multi_pathTwo_costs_avgs)