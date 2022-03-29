# CPSC 420 Midterm code
# Given an adjacency matrix and a list of edges p.
# Return True if the set P represents a path between two nodes in the graph, with NO cycles
import networkx as nx
from matplotlib import pyplot as plt


class Edge:

    def __init__(self, p1, p2):
        self.end1 = p1
        self.end2 = p2

    def isItPath(self, g, p):
        return True

    def __str__(self):
        return "EDGE {} -> {}".format(self.end1, self.end2)


# Variables to set up graph for network
GRAPH = nx.Graph()
edges = []
nodes = []


def set_edges(Edges):
    visited_links = []

    for link in Edges:
        u = link[0]
        v = link[1]
        temp = [u, v]
        new_edge = Edge(u, v)
        print("Created edge: {}\n".format(str(new_edge)))

        if link not in visited_links:
            edges.append(temp)
            visited_links.append(link)


def set_nodes(Vertices):
    visited_nodes = []

    for node in Vertices:
        if node not in visited_nodes:
            nodes.append(node)
            visited_nodes.append(node)


def create_graph(Edges):
    set_edges(Edges)
    GRAPH.add_edges_from(edges)


if __name__ == '__main__':
    global_edges = [[0, 3], [3, 2], [2, 7], [7, 3], [3, 8], [0, 3], [3, 5], [2, 7], [7, 8], [0, 3], [3, 5], [5, 7], [7, 8]]

    path_1 = [[0, 3], [3, 2], [2, 7], [7, 3], [3, 8]]  # return true
    path_2 = [[0, 3], [3, 5], [2, 7], [7, 8]]  # return false
    path_3 = [[0, 3], [3, 5], [5, 7], [7, 8]]  # return true

    create_graph(global_edges)
    nx.draw(GRAPH, with_labels=True, font_weight='bold')
    plt.show()  # ToDo Need to figure out why I need this in order to stop the graph from disappearing
