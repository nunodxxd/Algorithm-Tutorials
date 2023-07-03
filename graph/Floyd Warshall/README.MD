# Floyd-Warshall

The Floyd-Warshall algorithm is an algorithm for finding the shortest paths between all pairs of vertices in a directed weighted graph with positive or negative edge weights (but with no negative cycles). A single execution of the algorithm will find the lengths (summed weights) of the shortest paths between all pairs of vertices. It is also known as:
- Floyd’s algorithm 
- The Roy–Warshall algorithm
- The Roy–Floyd algorithm 
- WFI algorithm


# Code Explanation 

The numbers on the edges represent the weights or distances between the vertices. The vertices are labeled as 0, 1, 2 and 3.

The adjacency matrix of this graph is:

|   | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 | 0 | 5 | INF | 10 |
| 1 | INF | 0 | 3 | INF |
| 2 | INF | INF | 0 | 1 |
| 3 | INF | INF | INF | 0 |

The matrix shows the direct distance from each vertex to each vertex. For example, the distance from vertex 0 to vertex 1 is 5, and the distance from vertex 1 to vertex 3 is INF (meaning there is no direct path).

The Floyd-Warshall algorithm updates this matrix by considering each vertex as an intermediate vertex and checking if there is a shorter path through that vertex. For example, when we consider vertex 0 as an intermediate vertex, we check if there is a shorter path from vertex 1 to vertex 3 through vertex 0. The direct distance from vertex 1 to vertex 3 is INF, and the distance from vertex 1 to vertex 0 plus the distance from vertex 0 to vertex 3 is 5 + 10 = 15. Since 15 is less than INF, we update the matrix with this value.

The updated matrix after considering vertex 0 as an intermediate vertex is:

|   | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 | 0 | 5 | INF | 10 |
| 1 | INF | 0 | 3 | **15** |
| 2 | INF | INF | 0 | 1 |
| 3 | INF | INF | INF | 0 |

The bold values are the ones that are changed or affected by the intermediate vertex.

We repeat this process for all the vertices in the graph. The final matrix after considering all the vertices as intermediate vertices is:

|   | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 | 0 | 5 | **8** | **9** |
| 1 | INF | 0 | 3 | **4** |
| 2 | INF | INF | 0 | 1 |
| 3 | INF | INF | INF | 0 |

This matrix shows the shortest distance between every pair of vertices in the graph. The values of 8, 4 and 9 are obtained by adding the distances of two paths that go through an intermediate vertex. For example:
- The value of 8 is obtained by adding the distance from vertex 0 to vertex 1 and the distance from vertex 1 to vertex 2. That is, 8 = 5 + 3. The intermediate vertex is vertex 1.
- The value of 4 is obtained by adding the distance from vertex 1 to vertex 2 and the distance from vertex 2 to vertex 3. That is, 4 = 3 + 1. The intermediate vertex is vertex 2.
- The value of 9 is obtained by adding the distance from vertex 0 to vertex 1 and the distance from vertex 1 to vertex 3. That is, 9 = 5 + 4. The intermediate vertex is vertex 1.

|   | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 | 0 | 5 | 8 = 5 + 3 | 9 = 5 + 4 |
| 1 | INF | 0 | 3 | 4 = 3 + 1 |
| 2 | INF | INF | 0 | 1 |
| 3 | INF | INF | INF | 0 |

