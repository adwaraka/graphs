import heapq

def dijkstra(graph: dict, start: str) -> dict:
    pQueue = [(0, start)]  # the distance is 0 and it is a start node
    distances = {}
    for node in graph.keys():
        distances[node] = float('inf')  # distances to all nodes are inf
    distances[start] = 0  # start is zero away from start!

    while pQueue:
        currentDistance, currentNode = heapq.heappop(pQueue)

        # existing distance to the current node is already shorter; ignore
        if currentDistance > distances[currentNode]:
            continue

        for neighbor, weight in graph[currentNode].items():
            # IMPORTANT; add the current distance to the weight
            distance = currentDistance + weight
            if distances[neighbor] > distance:
                distances[neighbor] = distance
                heapq.heappush(pQueue, (distance, neighbor))
    return distances


if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start = 'A'
    shortest_distances = dijkstra(graph, start)
    print(f"Shortest distances from node {start}: {shortest_distances}")

    start = 'B'
    shortest_distances = dijkstra(graph, start)
    print(f"Shortest distances from node {start}: {shortest_distances}")
