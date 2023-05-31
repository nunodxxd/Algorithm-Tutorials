import sys

def dijkstra(graph, start):
    # Initialize the distance dictionary with infinity for all nodes except the start node
    distances = {node: sys.maxsize for node in graph}
    distances[start] = 0

    # Create a set to store visited nodes
    visited = set()

    while len(visited) < len(graph):
        # Select the node with the smallest tentative distance
        min_distance = sys.maxsize
        min_node = None

        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node

        if min_node is None:
            break

        # Add the current node to the visited set
        visited.add(min_node)

        # Update the tentative distances of the neighboring nodes
        for neighbor, weight in graph[min_node].items():
            new_distance = distances[min_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances

# Example usage
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 2, 'B': 1, 'D': 2},
    'D': {'B': 3, 'C': 2, 'E': 4},
    'E': {'D': 4}
}

start_node = 'C'
distances = dijkstra(graph, start_node)

print("Shortest distances from node", start_node)
for node, distance in distances.items():
    print(node, "-", distance)
