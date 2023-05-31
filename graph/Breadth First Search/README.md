# Breadth First Search Algorithm

Breadth First Search is a graph traversal algorithm that explores all the vertices of a graph in breadth-first order, i.e., visiting all the vertices at the same level before moving to the next level. It uses a queue data structure to keep track of the vertices to be visited next. Starting from a given source vertex, BFS visits all the vertices reachable from the source vertex by visiting the neighbors of the current vertex before visiting the neighbors of its neighbors.

# Code Explanation 


We import the deque class from the collections module to use it as a queue.
The bfs function takes two parameters: the graph (represented as a dictionary) and the start vertex from which we want to begin the BFS traversal.
We create an empty set called visited to keep track of visited vertices.
We initialize a deque called queue and add the start vertex to it.
We mark the start vertex as visited by adding it to the visited set.
We start a while loop that continues until the queue becomes empty.
Inside the loop, we pop the leftmost vertex from the queue using popleft() and store it in the variable vertex.
We process the vertex in any desired way (e.g., printing it or storing it).
We iterate through the neighbors of the vertex in the graph.
If a neighbor is not visited, we add it to the queue and mark it as visited.
The BFS traversal continues until all the vertices reachable from the start vertex have been visited.

In this example, we have a graph represented as a dictionary, where the keys are the vertices, and the values are lists of neighboring vertices. We specify the starting vertex for the BFS traversal as 'D', and then we call the bfs function to perform the traversal. The output will be the BFS traversal order starting from vertex 'D'.

Here's the breakdown of the traversal:

1 - Start at vertex D. 

(D ? ? ? ? ?)

2 - Visit D and enqueue its neighbors: B. 

(D B ? ? ? ?)

3 - Visit B and enqueue its neighbors: A, D (ignored already in queue), E. 

(D B A E ? ?)

4 - Visit A and enqueue its neighbor: C. 

(D B A E C ?)

5 - Visit E and enqueue its neighbor: F. 

(D B A E C F)

6 - Visit C (already visited), skip. (D B A E C F)

7 - Visit F (already visited), skip. (D B A E C F)

8 - The final BFS traversal order starting from vertex 'D' is D, B, A, E, C, F.