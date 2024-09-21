from collections import defaultdict

class Topological(object):

    def __init__(self, graph):
        self.graph = graph

    def calculateIndegrees(self):
        indegrees = defaultdict(lambda: -1)
        zeroes = []
        for key, val in self.graph.items():
            indegrees[key]+=1
            for node in val:
                indegrees[node]+=1
        for key, val in indegrees.items():
            if val == 0:
                zeroes.append(key)
        return indegrees, zeroes

    def topologicalSort(self):
        queue, visited, result = [], [], []
        indegrees, zeroes = self.calculateIndegrees()
        for node in zeroes:
            queue.append(node)

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

        # TODO detect a cycle
        return result
