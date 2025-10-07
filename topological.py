from collections import defaultdict

class Topological(object):

    def __init__(self, graph, vertices):
        self.graph = graph
        self.V = vertices

    def calculateIndegrees(self):
        indegrees = defaultdict(lambda: 0)
        for key, val in self.graph.items():
            for node in val:
                indegrees[node]+=1
        return indegrees

    def topologicalSort(self):
        visited, result = [], []
        queue = [i for i in range(self.V)]
        indegrees = self.calculateIndegrees()

        for val in queue:
            if val in indegrees.keys():
                queue.remove(val)

        while queue != []:
            curr = queue.pop(0)
            print("Current node: {}".format(curr))
            if curr not in visited and indegrees[curr]==0:
                for child in self.graph[curr]:
                    queue.append(child)
                    print("Reduce indegree for {}"\
                          .format(indegrees[child]))
                    indegrees[child]-=1
                visited.append(curr)
                result.append(curr)

        if self.V != len(result):
            print("Cycle present! No solutions")
            return -1

        return result
