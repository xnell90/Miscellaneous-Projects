from board import *
from logic import *

def possible_values(board, row, col):
    row_val = [ board.grid[row][i] for i in range(0, 9) if board.grid[row][i] != 0 ]
    col_val = [ board.grid[i][col] for i in range(0, 9) if board.grid[i][col] != 0 ]
    blk_val = []

    row_indent, col_indent = int(row / 3), int(col / 3)
    start_row, end_row = 3 * row_indent, 3 * (1 + row_indent)
    start_col, end_col = 3 * col_indent, 3 * (1 + col_indent)

    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            if board.grid[i][j] != 0:
                blk_val.append(board.grid[i][j])

    invalid_values = []

    for row_col_blk in [row_val, col_val, blk_val]:
        for val in row_col_blk:
            if val not in invalid_values:
                invalid_values.append(val)

    return [i for i in range(1, 10) if i not in invalid_values]

def solve_sudoku(board):
    if is_solved(board):
        board.display()
    else:
        i = 0
        j = 0
        exit = False

        for row in range(0, 9):
            for col in range(0, 9):
                if board.grid[row][col] == 0:
                    i = row
                    j = col
                    exit = True
                    break
            if exit: break

        valid_values = possible_values(board, i, j)
        for val in valid_values:
            board.grid[i][j] = val
            solve_sudoku(board)

        board.grid[i][j] = 0

print("Puzzle Before...")
puzzle = Sudoku_Board("input_puzzle.txt")
puzzle.display()
print()
print("Puzzle After....")
solve_sudoku(puzzle)
