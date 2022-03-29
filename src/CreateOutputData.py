from src.Request import Request
from src.ControlPanel import GLOBAL_OUTPUT_FILE_PATH_ONE
from src.ControlPanel import GLOBAL_OUTPUT_FILE_PATH_TWO

from src.NodeObj import NodeObj

REQUEST_NEEDS_CALCULATING = 0
REQUEST_ONGOING = 1
REQUEST_DENIED = 2
REQUEST_APPROVED = 3

AUTO_FAIL = [5, 6, 13, 19]


#@Nvm it works as intended, Path one type paths will map on failed nodes and just be failed after while type two will avoid failed nodes completely.

def fail_unavailable_paths():
    for req in Request.STATIC_TOTAL_REQUEST_LIST:
        if req.requestStatus[0] == REQUEST_APPROVED:
            current_route = req.PATH_ONE.route
            for node in current_route:
                if node in AUTO_FAIL:
                    req.requestStatus[0] = REQUEST_DENIED
                    req.PATH_ONE = None


def get_average_data_PATH_ONE():
    delays = []
    costs = []
    fails = []
    lens = []

    total_approved = 0
    total_denied = 0

    delay = 0
    cost = 0
    fail = 0
    lngth = 0

    num_nodes = 20
    num_links = 30

    cpu = 0
    ram = 0
    pbs = 0

    bw = 0

    for req in Request.STATIC_TOTAL_REQUEST_LIST:
        if req.requestStatus[0] == REQUEST_APPROVED:
            total_approved += 1
            obj = req.PATH_ONE
            delays.append(obj.DELAY)
            costs.append(obj.COST)
            fails.append(obj.return_failure_probability())
            lens.append(len(obj.route))
        else:
            total_denied += 1

    for node in NodeObj.StaticNodeList:
        n = node.nodeResources
        cpu += n[0]
        ram += n[1]
        pbs += n[2]

    for lnk in NodeObj.StaticLinkList:
        bw += lnk.linkBW

    for d in delays:
        delay += d

    for c in costs:
        cost += c

    for f in fails:
        fail += f

    for l in lens:
        lngth += l

    delay_average = delay / total_approved
    cost_average = cost / total_approved
    fail_average = fail / total_approved
    route_average = lngth / total_approved

    cpu = cpu / num_nodes
    ram = ram / num_nodes
    pbs = pbs / num_nodes

    bw = bw / num_links

    return total_approved, total_denied, delay_average, cost_average, fail_average, route_average, [cpu, ram, pbs], bw


def get_average_data_PATH_TWO():
    delays = []
    costs = []
    fails = []
    lens = []

    total_approved = 0
    total_denied = 0

    delay = 0
    cost = 0
    fail = 0
    lngth = 0

    num_nodes = 20
    num_links = 30

    cpu = 0
    ram = 0
    pbs = 0

    bw = 0

    for req in Request.STATIC_TOTAL_REQUEST_LIST:
        if req.requestStatus[1] == REQUEST_APPROVED:
            total_approved += 1
            obj = req.PATH_TWO
            delays.append(obj.DELAY)
            costs.append(obj.COST)
            fails.append(obj.return_failure_probability())
            lens.append(len(obj.route))
        else:
            total_denied += 1

    for node in NodeObj.StaticNodeList:
        n = node.nodeResources
        cpu += n[0]
        ram += n[1]
        pbs += n[2]

    for lnk in NodeObj.StaticLinkList:
        bw += lnk.linkBW

    for d in delays:
        delay += d

    for c in costs:
        cost += c

    for f in fails:
        fail += f

    for l in lens:
        lngth += l

    delay_average = delay / total_approved
    cost_average = cost / total_approved
    fail_average = fail / total_approved
    route_average = lngth / total_approved

    cpu = cpu / num_nodes
    ram = ram / num_nodes
    pbs = pbs / num_nodes

    bw = bw / num_links

    return total_approved, total_denied, delay_average, cost_average, fail_average, route_average, [cpu, ram, pbs], bw


def output_file_PATH_ONE():
    fail_unavailable_paths() # This will fail all paths that have a failed node in its route
    with open(GLOBAL_OUTPUT_FILE_PATH_ONE, 'w') as fp:
        main_header = "DATASET=TEST_A,TYPE=WITHOUT_FAULT_TOLERANCE,NODES=42,LINKS=63,REQUESTS=100\n"
        average_header = "REQUEST PASSED, REQUESTS FAILED, AVERAGE REQUEST DELAY, AVERAGE REQUEST COST, AVERAGE FAILURE PROBABILITY, AVERAGE LENGTH OF PATHS, MEAN NODE [CPU, RAM, PBS], MEAN LINK BANDWIDTH\n"
        p, f, avd, avc, FAIL, route, resources, bw = get_average_data_PATH_ONE()
        avg = "{},{},{},{},{}%,{},{},{}\n".format(p, f, avd, avc, FAIL, route, resources, bw)
        request_header = "REQUEST STATUS,REQUEST ID,PATH ID,FAILURE PROBABILITY,DELAY,COST,FUNCTIONS,PATH\n"
        fp.write(main_header)
        fp.write(average_header)
        fp.write(avg)
        fp.write(request_header)

        for req in Request.STATIC_TOTAL_REQUEST_LIST:
            current_path = req.PATH_ONE
            if req.requestStatus[0] == REQUEST_APPROVED:
                fp.write("APPROVED,{},{},{}%,{},{},{},{}\n".format(req.requestID, current_path.pathID,
                                                                   current_path.FAILURE_PROBABILITY, current_path.DELAY,
                                                                   current_path.COST, req.requestedFunctions,
                                                                   current_path.route))
            else:
                fp.write("DENIED,{},NONE,NONE,0,0,{},src={}, dest={}\n".format(req.requestID, req.requestedFunctions,
                                                                               req.source, req.destination))


def output_file_PATH_TWO():
    with open(GLOBAL_OUTPUT_FILE_PATH_TWO, 'w') as fp:
        main_header = "DATASET=TEST_A,TYPE=WITH_FAULT_TOLERANCE,NODES=42,LINKS=63,REQUESTS=100\n"
        average_header = "REQUEST PASSED, REQUESTS FAILED, AVERAGE REQUEST DELAY, AVERAGE REQUEST COST, AVERAGE FAILURE PROBABILITY, AVERAGE LENGTH OF PATHS, MEAN NODE [CPU, RAM, PBS], MEAN LINK BANDWIDTH\n"
        p, f, avd, avc, FAIL, route, resources, bw = get_average_data_PATH_TWO()
        avg = "{},{},{},{},{}%,{},{},{}\n".format(p, f, avd, avc, FAIL, route, resources, bw)
        request_header = "REQUEST STATUS,REQUEST ID,PATH ID,FAILURE PROBABILITY,DELAY,COST,FUNCTIONS,PATH\n"
        fp.write(main_header)
        fp.write(average_header)
        fp.write(avg)
        fp.write(request_header)

        for req in Request.STATIC_TOTAL_REQUEST_LIST:
            current_path = req.PATH_TWO
            if req.requestStatus[1] == REQUEST_APPROVED:
                fp.write("APPROVED,{},{},{}%,{},{},{},{}\n".format(req.requestID, current_path.pathID, current_path.FAILURE_PROBABILITY, current_path.DELAY, current_path.COST, req.requestedFunctions, current_path.route))
            else:
                fp.write("DENIED,{},NONE,NONE,0,0,{},src={}, dest={}\n".format(req.requestID, req.requestedFunctions, req.source, req.destination))