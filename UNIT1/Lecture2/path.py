from graph import *


def buildCityGraph(graphType):
    graph = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'):  # Create 7 nodes
        graph.addNode(Node(name))
    graph.addEdge(Edge(graph.getNode('Boston'), graph.getNode('Providence')))
    graph.addEdge(Edge(graph.getNode('Boston'), graph.getNode('New York')))
    graph.addEdge(Edge(graph.getNode('Providence'), graph.getNode('Boston')))
    graph.addEdge(Edge(graph.getNode('Providence'), graph.getNode('New York')))
    graph.addEdge(Edge(graph.getNode('New York'), graph.getNode('Chicago')))
    graph.addEdge(Edge(graph.getNode('Chicago'), graph.getNode('Denver')))
    graph.addEdge(Edge(graph.getNode('Denver'), graph.getNode('Phoenix')))
    graph.addEdge(Edge(graph.getNode('Denver'), graph.getNode('New York')))
    graph.addEdge(Edge(graph.getNode('Los Angeles'), graph.getNode('Boston')))
    return graph


def printPath(path: list):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result += str(path[i])
        if i != len(path) - 1:
            result += '->'
    return result


def DFS(graph, start, end, path, shortest, toPrint=False):
    """
    Assumes graph is a Digraph; start and end are nodes;
    path and shortest are lists of nodes
    Returns a shortest path from start to end in graph
    """
    path = path + [start]
    if toPrint:
        print('Current DFS path: {}'.format(printPath(path)))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:  # avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print('Already visited {}'.format(node))
    return shortest


def shortestPath(graph, start, end, toPrint=False):
    """
    Assumes graph is a Digraph; start and end are nodes
    Returns a shortest path from start to end in graph
    """
    return DFS(graph, start, end, [], None, toPrint)


def testSP(source: str, destination: str):
    graph = buildCityGraph(DirectedGraph)
    sp = shortestPath(graph, graph.getNode(source), graph.getNode(destination), toPrint=True)
    if sp != None:
        print('Shortest path from {} to {} is {}'.format(source, destination, printPath(sp)))
    else:
        print('There is no path from {} to {}'.format(source, destination))


# testSP('Chicago','Boston')
# testSP('Boston', 'Phoenix')


def BFS(graph, start, end, toPrint=False):
    """
    Assumes graph is a Digraph; start and end are nodes
    Returns a shortest path from start to end in graph
    """
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        # Get and remove oldest element in pathQueue
        tempPath = pathQueue.pop(0)
        if toPrint:
            print('Current BFS path: {}'.format(printPath(tempPath)))
        lastNode = tempPath[-1]
        if lastNode == end:
            return tempPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tempPath:
                newPath = tempPath + [nextNode]
                pathQueue.append(newPath)
    return None


def shortestPath(graph, start, end, toPrint=False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return BFS(graph, start, end, toPrint)


testSP('Boston', 'Phoenix')