# Import necessary libraries
from collections import deque

# Define puzzle size (3x3)
N = 3


# Class to represent the puzzle state
class PuzzleState:
    def __init__(self, board, x, y, depth):
        self.board = board
        self.x = x          # Blank tile row position
        self.y = y          # Blank tile column position
        self.depth = depth  # Number of moves so far


# Possible moves: Left, Right, Up, Down
row = [0, 0, -1, 1]
col = [-1, 1, 0, 0]


# Function to check if current board is goal state
def is_goal_state(board):
    goal = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]]
    return board == goal


# Function to check if move is inside board
def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N


# Function to print the puzzle board
def print_board(board):
    for r in board:
        print(" ".join(map(str, r)))
    print("--------")


# BFS function to solve 8-puzzle problem
def solve_puzzle_bfs(start, x, y):
    q = deque()
    visited = set()

    # Add initial state to queue
    q.append(PuzzleState(start, x, y, 0))

    # Mark initial state as visited
    visited.add(tuple(map(tuple, start)))

    while q:
        curr = q.popleft()

        # Print current state
        print(f"Depth: {curr.depth}")
        print_board(curr.board)

        # Check goal state
        if is_goal_state(curr.board):
            print(f"Goal state reached at depth {curr.depth}")
            return

        # Try all 4 moves
        for i in range(4):
            new_x = curr.x + row[i]
            new_y = curr.y + col[i]

            if is_valid(new_x, new_y):

                # ✅ Step 1: Copy current board into new_board
                new_board = []
                for r in curr.board:
                    new_row = r[:]
                    new_board.append(new_row)

                # ✅ Step 2: Swap blank tile with neighboring tile
                temp = new_board[new_x][new_y]
                new_board[new_x][new_y] = new_board[curr.x][curr.y]
                new_board[curr.x][curr.y] = temp

                # Check if this new state is visited
                if tuple(map(tuple, new_board)) not in visited:
                    visited.add(tuple(map(tuple, new_board)))
                    q.append(PuzzleState(new_board, new_x, new_y, curr.depth + 1))

    print(" No solution found!")

