# Breadth First Search Algorithm

from collections import deque

def bfs(graph, start):
    visited = set()  # Set to keep track of visited vertices
    queue = deque([start])  # Queue for BFS traversal
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")  # Process the vertex (e.g., print or store)

        # Explore neighbors of the current vertex
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Example graph represented as a dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting vertex for BFS traversal
start_vertex = 'D'

# Perform BFS traversal
print("BFS traversal:")
bfs(graph, start_vertex)
