from src.NodeObj import NodeObj
from src.FuncObj import FuncObj
from src.LinkObj import LinkObj
from src.Request import Request
from src.ControlPanel import GLOBAL_REQUEST_DELAY_THRESHOLD
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
BACKUP = Path meets all criteria for success but is not the most optimal
FLUNK = Meets all criteria for success EXCEPT does NOT meet failure threshold
TURTLE = Meets all criteria for success EXCEPT, delay threshold. SHOULD BE NOTED THAT FAILURE THRESHOLD IS NOT CALCULATED FOR THESE PATHS
POOR = Path is traversable but does not have enough resources
STATE_UNKNOWN = The state of the path has yet to be determined.
"""

OPTIMAL_PATH_SET = False
REQUEST_DELAY_THRESHOLD = GLOBAL_REQUEST_DELAY_THRESHOLD

# Path Object States
STATE_UNKNOWN = 0
POOR = 1
TURTLE = 2
FLUNK = 3
BACKUP = 4
OPTIMAL = 5


class PathObj:
    # STATIC LIST OF ALL OPTIMAL PATHS
    StaticOptimalPathsList = []

    # These static lists all get cleared when the optimal paths are found
    BACKUP_PATHS = []
    StaticPathsList = []
    current_path_failures = []

    current_request_paths_list = []

    def __init__(self, pathID, route, state, REQ_INFO, MAPPING_LOCATION, DELAY, COST, FAILURE_PROBABILITY, PATH_TYPE):
        """
        :param pathID: path objects name Ex: "R1P87" R# = request number P# = path number
        :param route: The list that holds the nodes being traversed in this path
        :param state: Current state of the path
        :param REQ_INFO: [request.requestedFunctions, request.request_delay_threshold, request.requestedBW]
        :param MAPPING_LOCATION: [ NodeObj, [FuncObj] ]
        :param DELAY: Total delay time of PathObj
        :param COST: Total cost of PathObj
        :param FAILURE_PROBABILITY: The probability of the path failing
        :param PATH_TYPE: Just differentiates between with or without fault tolerance
        """
        self.pathID = pathID
        self.route = route
        self.state = state
        self.REQ_INFO = REQ_INFO  # List of all the relevant information needed from the request object for path sorting
        self.MAPPING_LOCATION = MAPPING_LOCATION
        self.DELAY = DELAY
        self.COST = COST
        self.FAILURE_PROBABILITY = FAILURE_PROBABILITY
        self.PATH_TYPE = PATH_TYPE

        PathObj.StaticPathsList.append(self)
        PathObj.current_request_paths_list.append(self)

    def set_failure_probability(self):
        """
        We calculate the failure probability using the rule of succession formula
        created by Pierre-Simon Laplace.

        link: https://en.wikipedia.org/wiki/Rule_of_succession

        :param self: PathObj being referenced
        :return: failure_probability: a float representing the probability of failure
        """
        fused_path = self.create_fusion_obj_list(self.route)
        link_temp = []
        node_temp = []

        overall_average = 0

        for step in fused_path:
            if type(step) == LinkObj:
                current_fail = step.calculate_failure(step.linkSrc, step.linkDest)
                link_temp.append(current_fail)
            else:
                current_fail = step.calculate_failure(step.nodeID)
                node_temp.append(current_fail)

        for step in link_temp:
            overall_average += step

        for step in node_temp:
            overall_average += step

        count = len(link_temp) + len(node_temp)

        failure_probability = overall_average / count
        failure_probability *= 100

        if failure_probability < 0:
            failure_probability *= -1

        self.FAILURE_PROBABILITY = failure_probability

    def return_failure_probability(self):
        """
        We calculate the failure probability using the rule of succession formula
        created by Pierre-Simon Laplace.

        link: https://en.wikipedia.org/wiki/Rule_of_succession

        :param self: PathObj being referenced
        :return: failure_probability: a float representing the probability of failure
        """
        fused_path = self.create_fusion_obj_list(self.route)
        link_temp = []
        node_temp = []

        overall_average = 0

        for step in fused_path:
            if type(step) == LinkObj:
                current_fail = step.calculate_failure(step.linkSrc, step.linkDest)
                link_temp.append(current_fail)
            else:
                current_fail = step.calculate_failure(step.nodeID)
                node_temp.append(current_fail)

        for step in link_temp:
            overall_average += step

        for step in node_temp:
            overall_average += step

        count = len(link_temp) + len(node_temp)

        failure_probability = overall_average / count
        failure_probability *= 100

        if failure_probability < 0:
            failure_probability *= -1

        self.FAILURE_PROBABILITY = failure_probability
        return failure_probability


    @staticmethod
    def create_fusion_obj_list(path):
        links_to_get = []
        output_list = []

        for i in range(len(path) - 1):
            src = path[i]
            dest = path[i + 1]
            link = LinkObj.returnLink(src, dest)
            links_to_get.append(link)
            i += 1

        for n in path:
            node = NodeObj.returnNode(n)
            output_list.append(node)
            if len(links_to_get) != 0:
                link = links_to_get.pop(0)
                output_list.append(link)

        return output_list

    @staticmethod
    def returnOptimalPath(backup_paths_list):
        for path in backup_paths_list:
            if path.state == OPTIMAL:
                return path

    @staticmethod
    def returnPath(id):
        for p in PathObj.StaticPathsList:
            if p.pathID == id:
                return p

    def __str__(self):
        return "Path ID: {} FAILURE PROBABILITY = {}% Route: {} State: {} REQ_FUNCTIONS: {} REQ_DELAY_THRESHOLD = {} PATH DELAY: {} PATH COST: {}\n".format(
            self.pathID, self.FAILURE_PROBABILITY, self.route, self.state, self.REQ_INFO[0], self.REQ_INFO[1],
            self.DELAY, self.COST)
        # if self.PATH_TYPE != 2:
        #     return "Path ID: {} Route: {} State: {} REQ_FUNCTIONS: {} REQ_DELAY_THRESHOLD = {} PATH DELAY: {} PATH COST: {}\n".format(self.pathID, self.route, self.state, self.REQ_INFO[0], self.REQ_INFO[1], self.DELAY, self.COST)
        # else:
        #     return "Path ID: {} FAILURE PROBABILITY = {}% Route: {} State: {} REQ_FUNCTIONS: {} REQ_DELAY_THRESHOLD = {} PATH DELAY: {} PATH COST: {}\n".format(self.pathID, self.FAILURE_PROBABILITY, self.route, self.state, self.REQ_INFO[0], self.REQ_INFO[1], self.DELAY, self.COST)