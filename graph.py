from collections import defaultdict
from breadthfs import BFS
from depthfs import DFS
from topological import Topological

class Graph(object):
    def __init__(self):
        self.graphDict = defaultdict(list)

    def addEdge(self, src, dest):
        self.graphDict[src].append(dest)

    def displayGraph(self):
        print(self.graphDict)

    def returnGraph(self):
    	return self.graphDict

def main():
    graph = Graph()
    graph.addEdge(5, 2)
    graph.addEdge(5, 0)
    graph.addEdge(4, 0)
    graph.addEdge(4, 1)
    graph.addEdge(2, 3)
    graph.addEdge(3, 1)
    graph.displayGraph()

    print("\nBreadth-First Search")
    b = BFS(graph.returnGraph())
    print(b.bfs(5))

    print("\nDepth-First Search")
    d = DFS(graph.returnGraph())
    print(d.dfs(5))

    print("\nTopological Sort Kahn's Algorithm")
    tGraph = Graph()
    vertices = 6
    tGraph.addEdge(4, 0)
    tGraph.addEdge(4, 1)
    tGraph.addEdge(5, 2)
    tGraph.addEdge(5, 0)
    tGraph.addEdge(2, 3)
    tGraph.addEdge(3, 1)
    tc = Topological(tGraph.returnGraph(), vertices)
    print(tc.topologicalSort())

    print("\nTopological Sort Kahn's Algorithm - Cycle")
    graphCycle = Graph()
    vertices2 = 3
    graphCycle.addEdge(0, 1)
    graphCycle.addEdge(1, 2)
    graphCycle.addEdge(2, 0)
    tc2 = Topological(graphCycle.returnGraph(), vertices2)
    print(tc2.topologicalSort())

main()
