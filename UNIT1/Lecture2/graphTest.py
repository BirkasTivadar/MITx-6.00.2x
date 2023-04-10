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


print('Graph:')
print(buildCityGraph(Graph))
print()
print('DirectedGraph:')
print(buildCityGraph(DirectedGraph))
