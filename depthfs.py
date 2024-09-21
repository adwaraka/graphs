class DFS(object):

    def __init__(self, graph):
        self.graph = graph

    def dfs(self, src):
        visited, stack, result = [], [], []
        stack.append(src)
        while stack != []:
            curr = stack.pop()
            if curr not in visited:
                stack.extend(self.graph[curr])
                visited.append(curr)
                result.append(curr)
        return result
