from collections import defaultdict

class ReverseGraph(object):

    def __init__(self, graph):
        self.graph = graph

    def reverseGraph(self) -> dict:
        newGraph = defaultdict(list)
        for src, dest in self.graph.items():
            for node in dest:
                newGraph[node].append(src)
        return newGraph