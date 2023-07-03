# Define infinity as a large enough value. This value will be used
# for vertices not connected to each other
INF = 99999

# Define a function to print the solution matrix
def printSolution(dist):
    print("The following matrix shows the shortest distances between every pair of vertices")
    for i in range(len(dist)):
        for j in range(len(dist[i])):
            if dist[i][j] == INF:
                print("%7s" % "INF", end=" ")
            else:
                print("%7d" % dist[i][j], end=" ")
        print()

# Define a function to implement Floyd-Warshall algorithm
def floydWarshall(graph):
    # Initialize the solution matrix same as input graph matrix.
    # Or we can say the initial values of shortest distances are based
    # on shortest paths considering no intermediate vertex.
    dist = graph.copy()

    # Add all vertices one by one to the set of intermediate vertices.
    # ---> Before start of an iteration, we have shortest distances between all
    # pairs of vertices such that the shortest distances consider only the
    # vertices in set {0, 1, 2, .. k-1} as intermediate vertices.
    # ----> After the end of an iteration, vertex no. k is added to the set of
    # intermediate vertices and the set becomes {0, 1, 2, .. k}
    for k in range(len(graph)):
        # Pick all vertices as source one by one
        for i in range(len(graph)):
            # Pick all vertices as destination for the above picked source
            for j in range(len(graph)):
                # If vertex k is on the shortest path from i to j,
                # then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Print the solution matrix
    printSolution(dist)

# Define a sample graph using an adjacency matrix
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

# Call the function with the sample graph
floydWarshall(graph)