# Dijkstra's Shortestpath

Dijkstra's algorithm is a popular algorithm used to find the shortest path between nodes in a graph. It works by assigning tentative distances to all nodes and then iteratively selecting the node with the smallest tentative distance and updating the distances of its neighboring nodes. This process continues until all nodes have been visited.

# Code Explanation 

In the code, the dijkstra function takes two arguments: graph, which represents the graph structure, and start, which is the starting node for the shortest path calculation. The function returns a dictionary distances that contains the shortest distances from the starting node to all other nodes in the graph.

The algorithm begins by initializing all distances with infinity except for the start node, which is set to 0. It also creates an empty set visited to store the visited nodes.

The main loop continues until all nodes have been visited. In each iteration, the node with the smallest tentative distance is selected from the unvisited nodes. If there is no such node, the loop breaks. The selected node is then added to the visited set.

Next, the algorithm updates the tentative distances of the neighboring nodes. It checks if the distance through the current node is shorter than the current tentative distance of a neighboring node. If it is, the distance is updated.

Finally, the function returns the distances dictionary containing the shortest distances from the start node to all other nodes.

In the example usage, a sample graph is defined, and the Dijkstra's algorithm is called with the start node 'C'. The resulting shortest distances from node 'C' to all other nodes are printed.