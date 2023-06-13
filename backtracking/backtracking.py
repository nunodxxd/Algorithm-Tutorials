# Backtracking Algorithm

def is_safe(board, row, col, N):
    # Check if it's safe to place a queen at position (row, col)
    
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check if there is a queen in the upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # Check if there is a queen in the upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    return True


def solve_n_queens(board, row, N, solutions):
    # Base case: all queens are placed
    if row == N:
        solution = []
        for i in range(N):
            row_data = ''.join(['Q' if j == 1 else '.' for j in board[i]])
            solution.append(row_data)
        solutions.append(solution)
        return
    
    # Try placing a queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_n_queens(board, row + 1, N, solutions)
            board[row][col] = 0  # Undo the choice


def n_queens(N):
    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_n_queens(board, 0, N, solutions)
    return solutions


# Example usage:
n = 4
solutions = n_queens(n)

print(f"Number of solutions for {n}-queens problem: {len(solutions)}")
for solution in solutions:
    for row in solution:
        print(row)
    print()
