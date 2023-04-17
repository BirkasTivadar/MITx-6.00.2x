"""
Exercise 2
Consider our representation of permutations of students in a line from Exercise 1. (The teacher only swaps the positions of two students that are next to each other in line.) Let's consider a line of three students, Alice, Bob, and Carol (denoted A, B, and C). Using the Graph class created in the lecture, we can create a graph with the design chosen in Exercise 1: vertices represent permutations of the students in line; edges connect two permutations if one can be made into the other by swapping two adjacent students.
We construct our graph by first adding the following nodes:
"""

from graphTest import *

nodes = []
nodes.append(Node("ABC"))  # nodes[0]
nodes.append(Node("ACB"))  # nodes[1]
nodes.append(Node("BAC"))  # nodes[2]
nodes.append(Node("BCA"))  # nodes[3]
nodes.append(Node("CAB"))  # nodes[4]
nodes.append(Node("CBA"))  # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)

for i in range(len(nodes) - 1):
    for j in range(i + 1, len(nodes)):
        if nodes[i].getName()[0] == nodes[j].getName()[0] or nodes[i].getName()[2] == nodes[j].getName()[2]:
            g.addEdge(Edge(nodes[i], nodes[j]))

for i in range(len(nodes)):
    edges = g.childrenOf(nodes[i])
    print('Children of nodes[{}]:'.format(str(i)))
    for node in edges:
        print(node.getName())
    print()
