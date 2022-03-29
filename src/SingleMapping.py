from src.NodeObj import NodeObj
from src.PathObj import PathObj
from src.FuncObj import FuncObj
from src.LinkObj import LinkObj
from src.Request import Request

from ControlPanel import GLOBAL_REQUEST_DELAY_THRESHOLD
from ControlPanel import GlOBAL_FAILURE_THRESHOLD
from ControlPanel import GLOBAL_FAILURE_RATE

"""
@author: Jackson Walker
Path resources: [CPU, RAM, Physical buffer size]

Essentially an extension of the request class. Made so that
I can keep track of things specific to a path.

In order to differentiate paths from each-other I am adding specific states that give information on where
the path ranks in usefulness and in the hierarchy of all paths for a specific request.

The criteria for a paths success is the following...
1) Travers-ability
2) Resources capability
3) Within delay threshold
4) within failure threshold
5) Processing

Once the path state is determined the paths are then able to be sorted and used.

PATH_STATE:

OPTIMAL = The best most optimal path for this request. Path that will be mapped.
BACKUP = Path meets all criteria for success but is not the most optimal.
FLUNK = Meets all criteria for success EXCEPT does NOT meet failure threshold.
TURTLE = Meets all criteria for success EXCEPT, delay threshold.
POOR = Path is traversable but does not have enough resources.
STATE_UNKNOWN = The state of the path has yet to be determined.
"""

FAIL_RATE = GLOBAL_FAILURE_RATE
REQUEST_DELAY_THRESHOLD = GLOBAL_REQUEST_DELAY_THRESHOLD
FAILURE_THRESHOLD = GlOBAL_FAILURE_THRESHOLD
OPTIMAL_PATH_SET = False

# Path Object States
STATE_UNKNOWN = 0
POOR = 1
TURTLE = 2
FLUNK = 3
BACKUP = 4
OPTIMAL = 5

AUTO_FAIL = [5, 6, 13, 19]


def check_fail(path_obj):

    # AUTO_FAIL = [5, 6, 13, 19]

    for step in path_obj.route:
        if step in AUTO_FAIL:
            path_obj.state = POOR
            return False
    return True


# @Todo need to remember to clear BACKUP_PATHS when finished processing request
def set_path_state_PATH_ONE(path_obj):  # <-- This one DOES NOT use failure probability
    # Given a path must then determine and set the state of the path
    if path_obj.state == STATE_UNKNOWN:
        if calculate_path_resources_PATH_ONE(path_obj):
            if calculate_path_speed(path_obj, REQUEST_DELAY_THRESHOLD):
                path_obj.state = BACKUP
                PathObj.BACKUP_PATHS.append(path_obj)
            else:
                path_obj.state = TURTLE
                print("PATH {} DELAY {} | PATH IS TOO SLOW!".format(path_obj.pathID, path_obj.DELAY))
        else:
            path_obj.state = POOR
            print("PATH {} DOES NOT HAVE ENOUGH RESOURCES!".format(path_obj.pathID))


# @Todo need to remember to clear BACKUP_PATHS when finished processing request
def set_path_state_PATH_TWO(path_obj):  # <-- This one DOES NOT use failure probability
    # Given a path must then determine and set the state of the path
    if path_obj.state == STATE_UNKNOWN:
        if calculate_path_resources_PATH_TWO(path_obj):
            if calculate_path_failure(path_obj, FAILURE_THRESHOLD):
                if calculate_path_speed(path_obj, REQUEST_DELAY_THRESHOLD):
                    path_obj.state = BACKUP
                    PathObj.BACKUP_PATHS.append(path_obj)
                else:
                    path_obj.state = TURTLE
                    print("PATH {} DELAY {} | PATH IS TOO SLOW!".format(path_obj.pathID, path_obj.DELAY))
            else:
                path_obj.state = FLUNK
                print("PATH {} FAILURE {}% | FAILURE PROBABILITY IS TOO HIGH!".format(path_obj.pathID, path_obj.FAILURE_PROBABILITY))
        else:
            path_obj.state = POOR
            print("PATH {} DOES NOT HAVE ENOUGH RESOURCES!".format(path_obj.pathID))


def calculate_path_resources_PATH_ONE(path_obj):
    """
    We can exit the loop and return something when we either:
    1) Know that the path DOES have enough resources, return True.
    2) Know that for whatever reason our functions CANNOT be mapped to the nodes on the path, return False.

    RETURN TRUE: Path has proven that it is able to map every function.
    RETURN FALSE: Destination has been reached before all functions have been mapped.

    :param path_obj: an object of the PathObj class
    :return: Boolean
    """
    fused_path = PathObj.create_fusion_obj_list(path_obj.route)
    req_info = path_obj.REQ_INFO
    funcs_to_map = req_info[0].copy()  # ToDo need to be COPYING LISTS OTHERWISE WE ARE DIRECTLY REFERENCING THEM!
    requested_bandwidth = int(req_info[2])
    end_node = fused_path[-1]
    end_link = fused_path[-2]

    enough_bw = False
    all_mapped = False

    funcs_mapped = []
    func_count = 0

    for step in fused_path:
        if all_mapped and enough_bw:
            return True
        if type(step) == LinkObj:   # If its a link
            # print("Link ID: {} Src: {} Dest: {}".format(step.linkID, step.linkSrc, step.linkDest))
            check_bw = step.check_enough_resources(requested_bandwidth)
            if not check_bw:
                path_obj.state = POOR
                return False
            elif step.linkID == end_link.linkID:
                enough_bw = True
        else:   # if its a node
            if all_mapped:
                continue
            else:
                current_node = step  # First we must determine if mapping is even possible

                if current_node.status == 'O':
                    # print("MAPPING ON NODE {} IS NOT POSSIBLE NODE IS OFFLINE".format(current_node.nodeID))
                    NodeObj.AUTO_FAIL.append(current_node.nodeID)
                    path_obj.state = POOR
                    return False
                elif current_node.status == 'R':
                    continue
                else:  # Next we need to determine if a node has enough resources for mapping and how many it can handle
                    if len(funcs_to_map) == 0:
                        all_mapped = True
                        continue
                    else:
                        current_mappable_functions = current_node.how_many_functions_mappable(funcs_to_map)  # LOOK AT THIS

                        if current_mappable_functions == [] and step.nodeID == end_node.nodeID and len(funcs_to_map) > 0:
                            path_obj.state = POOR
                            return False
                        elif current_mappable_functions == []:
                            continue
                        else:
                            for i in range(len(current_mappable_functions)):
                                f = current_mappable_functions[i]
                                funcs_mapped.append(current_mappable_functions[i])
                                path_obj.MAPPING_LOCATION.append([current_node, f])
                                funcs_to_map.pop(0)
                                func_count += 1
                            continue


def calculate_path_resources_PATH_TWO(path_obj):
    """
    We can exit the loop and return something when we either:
    1) Know that the path DOES have enough resources, return True.
    2) Know that for whatever reason our functions CANNOT be mapped to the nodes on the path, return False.

    RETURN TRUE: Path has proven that it is able to map every function while being at a stable rate of failure.
    RETURN FALSE: Destination has been reached before all functions have been mapped and/or failure probability is too high.

    :param path_obj: an object of the PathObj class
    :return: Boolean
    """
    fused_path = PathObj.create_fusion_obj_list(path_obj.route)
    req_info = path_obj.REQ_INFO
    funcs_to_map = req_info[0].copy()
    requested_bandwidth = int(req_info[2])
    end_node = fused_path[-1]
    end_link = fused_path[-2]

    enough_bw = False
    all_mapped = False

    funcs_mapped = []
    func_count = 0

    for step in fused_path:
        if all_mapped and enough_bw:
            return True
        if type(step) == LinkObj:
            # print("Link ID: {} Src: {} Dest: {}".format(step.linkID, step.linkSrc, step.linkDest))
            # NOTE: In HvW Protocol if a link doesnt have enough BW the path fails
            check_bw = step.check_enough_resources(requested_bandwidth)
            if not check_bw:
                path_obj.state = POOR
                return False
            elif step.linkID == end_link.linkID:
                enough_bw = True
        else:
            current_node = step

            if current_node.failure_probability >= 0.55:
                NodeObj.AUTO_FAIL_PATH_TWO.append(current_node.nodeID)
                path_obj.state = POOR
                return False
            # Determining the status of a node and if it has failed
            elif current_node.get_status == 'O':
                # print("MAPPING ON NODE {} IS NOT POSSIBLE NODE IS OFFLINE".format(current_node.nodeID))
                NodeObj.AUTO_FAIL_PATH_TWO.append(current_node.nodeID)
                path_obj.state = POOR
                return False
            elif current_node.status == 'R':
                # print("MAPPING ON NODE {} IS NOT POSSIBLE, RELAY TO NEXT NODE IN PATH".format(current_node.nodeID))
                continue
            else:  # Next we need to determine if a node has enough resources for mapping and how many it can handle
                if len(funcs_to_map) == 0:
                    all_mapped = True
                    continue
                else:
                    current_mappable_functions = current_node.how_many_functions_mappable(funcs_to_map)  # LOOK AT THIS

                    if current_mappable_functions == [] and step.nodeID == end_node.nodeID and len(funcs_to_map) > 0:
                        path_obj.state = POOR
                        return False
                    elif not current_mappable_functions:
                        continue
                    else:
                        for i in range(len(current_mappable_functions)):
                            f = current_mappable_functions[i]
                            print(f)
                            funcs_mapped.append(current_mappable_functions[i])
                            path_obj.MAPPING_LOCATION.append([current_node, f])
                            funcs_to_map.pop(0)
                            func_count += 1
                        continue


def calculate_path_speed(path_obj, delay_threshold):
    """
    Method that is responsible for predicting and calculating the time it would take for a request to be
    processed on a particular path. This method also calculates and sets the values of DELAY and COST for
    each PathObj.

    At this stage every path being processed through this function and beyond meets at least the minimum
    requirements for resources and node mapping.

    RETURN TRUE: Path has proven that it is able to fully process its request within the delay threshold.
    RETURN FALSE: Path is unable to process its request without exceeding the delay threshold.

    1) Need to retrieve needed data from all nodes with mapped functions
    2) Need to retrieve needed data from all links being used
    3) Just have to add it up and make sure its within the threshold

    Things that need to be calculated:
    PATH_COST = node_cost + link_cost
    PATH_DELAY = node_processing_delay + link_edge_delay

    PATH_DELAY <= delay_threshold

    1) Link EdgeDelay
    2) Link EdgeCost
    3) Node Processing Delay for nodes with functions mapped to them
    4) Node cost

    :param path_obj: an object of the PathObj class
    :param delay_threshold: The numerical value representing the window of time to fulfill a request before failure.
    :return: Boolean
    """
    fused_list = PathObj.create_fusion_obj_list(path_obj.route)
    mapping_list = path_obj.MAPPING_LOCATION

    # @ToDo remember that when a function is mapped to a node the delay for that node is: processingDelay + (processingDelay x num_funcs_mapped)
    for mapping_location in mapping_list:
        used_node = mapping_location[0]
        func = mapping_location[1]
        path_obj.DELAY += used_node.processingDelay

    for step in fused_list:
        if type(step) == LinkObj:
            path_obj.DELAY += step.linkED
            path_obj.COST += step.linkEC
        elif type(step) == NodeObj:
            path_obj.DELAY += step.processingDelay
            path_obj.COST += step.nodeCost

    if path_obj.DELAY <= delay_threshold:
        return True
    else:
        return False


def calculate_path_failure(path_obj, failure_threshold):
    failure_rate = path_obj.return_failure_probability()
    if failure_rate <= failure_threshold:
        return True
    else:
        path_obj.state = FLUNK
        print("PATH {} = {} FAILURE PROBABILITY IS TOO HIGH!".format(path_obj.pathID, path_obj.FAILURE_PROBABILITY))
        return False


def calculate_optimal_PATH_ONE():
    """
    Compares every single path that meets all the other specified criteria and finds
    the shortest one WITHOUT the least failure probability.
    """
    if not OPTIMAL_PATH_SET:
        current_best_path = PathObj.BACKUP_PATHS[0]

        for obj in PathObj.BACKUP_PATHS:
            if obj.DELAY < current_best_path.DELAY:
                current_best_path = obj
            elif obj.DELAY == current_best_path.DELAY:
                if obj.COST < current_best_path.COST:
                    current_best_path = obj

        current_best_path.state = 5
        PathObj.OPTIMAL_PATH_SET = True


def calculate_optimal_PATH_TWO():
    """
    Compares every single path that meets all the other specified criteria and finds
    the shortest one WITH the least failure probability.
    """
    if not OPTIMAL_PATH_SET:
        current_best_path = PathObj.BACKUP_PATHS[0]

        for obj in PathObj.BACKUP_PATHS:
            if current_best_path.FAILURE_PROBABILITY < current_best_path.FAILURE_PROBABILITY:
                current_best_path = obj
            elif current_best_path.FAILURE_PROBABILITY == current_best_path.FAILURE_PROBABILITY:
                if obj.COST < current_best_path.COST:
                    current_best_path = obj
                elif obj.COST == current_best_path.COST:
                    if obj.DELAY < current_best_path.DELAY:
                        current_best_path = obj

        current_best_path.state = 5
        PathObj.OPTIMAL_PATH_SET = True


def map_path_ONE(path_obj):
    if path_obj.state == OPTIMAL:  # Checks to make sure we are mapping the optimal path
        print("MAPPING PATH {}\n".format(path_obj.pathID))
        fused_list = PathObj.create_fusion_obj_list(path_obj.route)
        mapping_list = path_obj.MAPPING_LOCATION
        requested_bandwidth = int(path_obj.REQ_INFO[2])

        for mapping_location in mapping_list:
            node_used = mapping_location[0]
            func = mapping_location[1]
            node_used.map_function_obj(func)

        for element in fused_list:
            if type(element) == LinkObj:
                link = element
                link.map_request(requested_bandwidth)

    node_avg = 0
    link_avg = 0

    for node in NodeObj.StaticNodeList:
        node_avg += node.nodeResources[0]

    for link in NodeObj.StaticLinkList:
        link_avg += link.linkBW

    NodeObj.StaticNodeResources_PATHONE.append(node_avg / 20)
    NodeObj.StaticLinkResources_PATHONE.append(link_avg / 30)
    print("PATH MAPPED")


def map_path_TWO(path_obj):
    if path_obj.state == OPTIMAL:  # Checks to make sure we are mapping the optimal path
        print("MAPPING PATH {}\n".format(path_obj.pathID))
        fused_list = PathObj.create_fusion_obj_list(path_obj.route)
        mapping_list = path_obj.MAPPING_LOCATION
        requested_bandwidth = int(path_obj.REQ_INFO[2])

        for mapping_location in mapping_list:
            node_used = mapping_location[0]
            func = mapping_location[1]
            node_used.map_function_obj(func)

        for element in fused_list:
            if type(element) == LinkObj:
                link = element
                link.map_request(requested_bandwidth)

    node_avg = 0
    link_avg = 0

    for node in NodeObj.StaticNodeList:
        node_avg += node.nodeResources[0]

    for link in NodeObj.StaticLinkList:
        link_avg += link.linkBW

    NodeObj.StaticNodeResources_PATHTWO.append(node_avg / 20)
    NodeObj.StaticLinkResources_PATHTWO.append(link_avg / 30)
    print("PATH MAPPED")


def RUN_PATH_ONE_SINGLE_MAPPING(req):
    for path in PathObj.current_request_paths_list:
        set_path_state_PATH_ONE(path)
        if path.state < 3:
            del path

    if len(PathObj.BACKUP_PATHS) == 0:
        req.requestStatus[0] = 2   # Fail current request if no paths
        Request.STATIC_DENIED_REQUEST_LIST.append(req)

    else:
        req.requestStatus[0] = 3
        Request.STATIC_APPROVED_REQUEST_LIST.append(req)

        calculate_optimal_PATH_ONE()
        optimal_path = PathObj.returnOptimalPath(PathObj.BACKUP_PATHS)
        PathObj.StaticOptimalPathsList.append(optimal_path)
        map_path_ONE(optimal_path)
        req.PATH_ONE = optimal_path

    # Data cleanup process
    PathObj.BACKUP_PATHS.clear()
    PathObj.current_request_paths_list.clear()
    PathObj.current_path_failures.clear()


def RUN_PATH_TWO_SINGLE_MAPPING(req):
    for path in PathObj.current_request_paths_list:
        set_path_state_PATH_TWO(path)
        if path.state != 5:     # need to reconsider why I need these two lines
            del path

    if len(PathObj.BACKUP_PATHS) == 0:
        req.requestStatus[1] = 2  # Fail current request if no paths
        Request.STATIC_DENIED_REQUEST_LIST.append(req)

    else:
        req.requestStatus[1] = 3
        Request.STATIC_APPROVED_REQUEST_LIST.append(req)

        calculate_optimal_PATH_TWO()
        optimal_path = PathObj.returnOptimalPath(PathObj.BACKUP_PATHS)
        PathObj.StaticOptimalPathsList.append(optimal_path)
        map_path_TWO(optimal_path)
        req.PATH_TWO = optimal_path

    # Data cleanup process
    PathObj.BACKUP_PATHS.clear()
    PathObj.current_request_paths_list.clear()
    PathObj.current_path_failures.clear()
