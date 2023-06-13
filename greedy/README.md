# Greedy algorithms 

A Greedy Algorithm is an algorithmic approach that makes the best available choice at every step in the hope of finding an optimal solution. Greedy algorithms are computationally cheaper than other families of algorithms like dynamic programming or brute force because they don’t explore the solution space too much. 

# Greedy algorithmic vs Non-greedy algorithmic

An example of a popular greedy algorithm is Dijkstra’s algorithm that finds the path with the minimum cost from one vertex to the others in a graph. This algorithm finds such a path by always going to the nearest vertex.

A not Greedy Algorithm, on the other hand, checks all options before arriving at a final solution. Unlike a greedy approach which stops once it gets its results.

The use of a greedy algorithm depends on the problem and criteria used. There are cases where we can obtain a solution that is good enough by using a greedy strategy. However, there are also problems for which greedy algorithms don’t yield the best solution and might even yield the worst possible solution.


# When should I use it?

One example where a greedy algorithm is the best choice is the "Activity Selection Problem" The problem is to select the maximum number of activities that can be performed, given a set of activities with their start and finish times, assuming that only one activity can be performed at a time.

| (see the python code -> greedy.py)

In this example, the algorithm sorts the activities based on their finish times in ascending order. It starts by selecting the activity with the earliest finish time and then iteratively selects the next activity whose start time is greater than or equal to the finish time of the previously selected activity.

The greedy algorithm works well for this problem because it exploits the fact that selecting activities with the earliest finish times allows for the maximum number of activities to be performed without conflicts. This strategy yields the optimal solution in this case.

In contrast, a non-greedy algorithm, such as dynamic programming, may not be the best choice for the Activity Selection Problem. Dynamic programming is useful when we need to solve problems by breaking them down into overlapping subproblems. However, for the Activity Selection Problem, the greedy approach of selecting activities based on finish times provides an optimal solution without the need for dynamic programming.

Therefore, in this specific scenario, the greedy algorithm is the best choice as it is simpler, more efficient, and provides an optimal solution