def is_row_valid(board, row):
    non_zero_numbers = [ num for num in board.grid[row] if num != 0 ]
    return is_distinct(non_zero_numbers)

def is_col_valid(board, col):
    non_zero_numbers = (
        [ board.grid[i][col] for i in range(0, 9) if board.grid[i][col] != 0 ]
    )
    return is_distinct(non_zero_numbers)

def is_block_valid(board, row, col):
    non_zero_numbers = []

    row_indent, col_indent = int(row / 3), int(col / 3)
    start_row, end_row = 3 * row_indent, 3 * ( 1 + row_indent )
    start_col, end_col = 3 * col_indent, 3 * ( 1 + col_indent )

    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            if board.grid[i][j] != 0:
                non_zero_numbers.append(board.grid[i][j])

    return is_distinct(non_zero_numbers)

def is_row_complete(board, row):
    return (0 not in board.grid[row])


def is_col_complete(board, col):
    column = [ board.grid[i][col] for i in range(0, 9) ]
    return (0 not in column)

def is_block_complete(board, row, col):
    block = []

    row_indent, col_indent = int(row / 3), int(col / 3)
    start_row, end_row = 3 * row_indent, 3 * (1 + row_indent)
    start_col, end_col = 3 * col_indent, 3 * (1 + col_indent)

    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            if board.grid[i][j] != 0:
                block.append(board.grid[i][j])

    return (0 not in block)

def is_solved(board):
    #Check all rows
    for row in range(0, 9):
        if not is_row_complete(board, row):
            return False

    #Check all cols
    for col in range(0, 9):
        if not is_col_complete(board, col):
            return False

    #Check all blocks
    for center_row in range(0, 9, 3):
        for center_col in range(0, 9, 3):
            if not is_block_complete(board, center_row, center_col):
                return False

    return True

#Extra method for checking if the array has distinct elements
def is_distinct(els):
    test = []
    for el in els:
        if el != 0 and (el not in test): test.append(el)

    return test == els
