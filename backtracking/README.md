# Backtracking

Backtracking is a general algorithmic technique used to find solutions for problems that involve searching through a large number of possibilities. It is especially useful when we have a combinatorial problem where we need to make a series of choices, but we want to optimize those choices to find the best possible solution.

The basic idea behind backtracking is to explore all possible solutions incrementally, but to backtrack or undo the choices that don't lead to a valid solution. This allows the algorithm to efficiently prune branches of the search tree that are not promising.

# Code explanation 

Let's consider an example of the famous N-Queens problem, which involves placing N chess queens on an N×N chessboard in such a way that no two queens threaten each other.

In this example, the is_safe() function checks if it is safe to place a queen at a specific position on the chessboard. It verifies that there are no other queens in the same column or in the diagonals.

The solve_n_queens() function is the backtracking algorithm itself. It takes the board, the current row, the size N, and a solutions list. If all queens are placed (base case), it appends the current solution to the solutions list. Otherwise, it tries placing a queen in each column of the current row, and recursively calls itself to solve the remaining problem. After exploring a choice, it undoes the choice by setting the position back to 0.

Finally, the n_queens() function initializes the chessboard, calls the backtracking algorithm, and returns the list of solutions. In the example usage, we solve the 4-queens problem and print the number of solutions along with each solution represented as a chessboard.