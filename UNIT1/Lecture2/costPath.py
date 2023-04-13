from graph import *
from path import *


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight=1):
        Edge.__init__(self, src, dest)
        self.weigth = weight

    def getWeight(self):
        return self.weigth

    def __str__(self):
        return Edge.__str__(self) + ' ({})'.format(self.weigth)


def cost(path):
    result = ''
    for i in range(len(path)):
        result += str(path[i])
        if i != len(path) - 1:
            result += '->'
    return result


def DFS(graph, start, end, path, shortest, toPrint=False):
    """Assumes graph is a Digraph; start and end are nodes;
          path and shortest are tuples containing a list of
          nodes and a cost
       Returns a shortest path from start to end in graph"""
    path = (path + [start], 0)
    if toPrint:
        print('Current DFS path:', printPath(path[0]))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:  # avoid cycles
            if shortest == None or cost(path) < cost(shortest):
                newPath = DFS(graph, node, end, path, shortest,
                              toPrint)
                if newPath != None:
                    shortest = newPath


def testSP():
    nodes = []
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'):  # Create 6 nodes
        nodes.append(Node(str(name)))
    graph = DirectedGraph()
    for n in nodes:
        graph.addNode(n)
    graph.addEdge(WeightedEdge(nodes[0], nodes[1]))
    graph.addEdge(WeightedEdge(nodes[1], nodes[2]))
    graph.addEdge(WeightedEdge(nodes[2], nodes[3]))
    graph.addEdge(WeightedEdge(nodes[2], nodes[4]))
    graph.addEdge(WeightedEdge(nodes[3], nodes[4]))
    graph.addEdge(WeightedEdge(nodes[3], nodes[5]))
    graph.addEdge(WeightedEdge(nodes[0], nodes[2], 10))
    graph.addEdge(WeightedEdge(nodes[1], nodes[0]))
    graph.addEdge(WeightedEdge(nodes[3], nodes[1]))
    graph.addEdge(WeightedEdge(nodes[4], nodes[0]))
    sp = shortestPath(graph, nodes[0], nodes[5], toPrint=True)
    print('Shortest path is', printPath(sp))
    sp = BFS(graph, nodes[0], nodes[5])
    print('Shortest path found by BFS:', printPath(sp))


testSP()
