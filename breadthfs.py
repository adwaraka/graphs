class BFS(object):

    def __init__(self, graph):
        self.graph = graph

    def bfs(self, src):
        visited, queue, result = [], [], []
        queue.append(src)
        while queue != []:
            curr = queue.pop(0)
            if curr not in visited:
                queue.extend(self.graph[curr])
                visited.append(curr)
                result.append(curr)
        return result
