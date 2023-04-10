class Node(object):
    def __init__(self, name: str):
        """Assumes name is a string"""
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, source: Node, destination: Node):
        """Assumes src and dest are nodes"""
        self.source = source
        self.destination = destination

    def getSource(self):
        return self.source

    def getDestination(self):
        return self.destination

    def __str__(self):
        return self.source.getName() + '->' + self.destination.getName()


class DirectedGraph(object):
    """edges is a dictionary mapping each node to a list of its children"""

    def __init__(self):
        self.edges = {}

    def addNode(self, node: Node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def addEdge(self, edge: Edge):
        source = edge.getSource()
        destination = edge.getDestination()
        if not (source in self.edges and destination in self.edges):
            raise ValueError('Node not in graph')
        self.edges[source].append(destination)

    def childrenOf(self, node: Node):
        return self.edges[node]

    def hasNode(self, node: Node):
        return node in self.edges

    def getNode(self, name: str):
        for node in self.edges:
            if node.getName() == name:
                return node
        raise NameError(name)

    def __str__(self):
        result = ''
        for source in self.edges:
            for destination in self.edges[source]:
                result = result + source.getName() + '->' + destination.getName() + '\n'
        return result[:-1]  # omit final newline


class Graph(DirectedGraph):
    def addEdge(self, edge: Edge):
        DirectedGraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        DirectedGraph.addEdge(self, rev)
