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

    print("\nTopological Search")
    t = Topological(graph.returnGraph())
    print(t.topologicalSort())

    print("\nTopological Search with Cycle")
    graphCycle = Graph()
    graphCycle.addEdge(0, 1)
    graphCycle.addEdge(1, 2)
    graphCycle.addEdge(2, 3)
    graphCycle.addEdge(4, 3)
    graphCycle.addEdge(3, 1)
    tc = Topological(graphCycle.returnGraph())
    print(tc.topologicalSort())

main()
