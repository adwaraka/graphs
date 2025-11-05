def spUnweighted(graph, start, end):
    if start not in graph or end not in graph:
        return None

    # Store (currentNode, path_to_currentNode)
    queue = [(start, [start])]
    visited = {start}
    parent = {start: None}  # Stores parent of each node for path reconstruction

    while queue:
        currentNode, path = queue.pop(0)

        if currentNode == end:
            # Reconstruct path using parent pointers
            path = []
            node = end
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]  # Reverse to get path from start to end

        for neighbor in graph.get(currentNode, []):
            if neighbor not in visited:
                visited.add(neighbor)
                # Set currentNode as parent of neighbor
                parent[neighbor] = currentNode
                queue.append((neighbor, path + [neighbor]))

    return None  # No path found

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']
}

start_node = 'A'
end_node = 'G'
path = spUnweighted(graph, start_node, end_node)

if path:
    print(f"Shortest path from {start_node} to {end_node}: {path}")
else:
    print(f"No path found from {start_node} to {end_node}.")