from src.NodeObj import NodeObj
from src.ControlPanel import GLOBAL_REQUEST_DELAY_THRESHOLD
from src.ControlPanel import GLOBAL_LINK_BANDWIDTH

REQUEST_DELAY_THRESHOLD = GLOBAL_REQUEST_DELAY_THRESHOLD


class LinkObj(NodeObj):  # <-- This means its a subclass of NodeObj right?

    UNAVAILABLE = 'O'
    AVAILABLE = 'A'

    def __init__(self, linkID, linkStatus, linkSrc, linkDest, linkBW, linkED, linkEC, failure_probability):
        self.linkID = linkID
        self.linkStatus = linkStatus
        self.linkSrc = linkSrc
        self.linkDest = linkDest
        self.linkBW = linkBW
        self.linkED = linkED
        self.linkEC = linkEC
        self.failure_probability = failure_probability

        NodeObj.StaticLinkList.append(self)

    def reset_link(self):
        for pair in NodeObj.StaticLinkResources:
            if self.linkID == pair[0]:
                self.linkBW = GLOBAL_LINK_BANDWIDTH
                self.linkStatus = 'A'

    def showLinkSourceID(self):
        return self.linkSrc

    def compareBW(self, bw):
        if self.linkBW >= bw:
            return True
        else:
            return False

    def map_request(self, bw):
        self.linkBW = int(self.linkBW) - bw

    def check_enough_resources(self, req_bw):
        if self.linkBW <= 0:
            return False
        elif self.linkBW >= req_bw:
            return True


    @staticmethod
    def calculate_failure(src, dest):
        """
        calculate whether or not a node has failed.
        :param lid = linkID
        :return: True if success, False if failed
        """
        l = LinkObj.returnLink(src, dest)
        number_of_failures = REQUEST_DELAY_THRESHOLD * l.failure_probability
        fail_rate = (number_of_failures + 1) / (REQUEST_DELAY_THRESHOLD + 2)
        return fail_rate

    @staticmethod
    def returnLink(src, dest):
        for link in NodeObj.StaticLinkList:
            if (link.linkSrc == src and link.linkDest == dest) or (link.linkSrc == dest and link.linkDest == src):
                return link

    def __str__(self):
        return "LinkID {} Source {} Dest {} BandWidth {} Delay {} Cost {} Failure Probability {}".format(self.linkID, self.linkSrc, self.linkDest, self.linkBW, self.linkED, self.linkEC, self.failure_probability)
