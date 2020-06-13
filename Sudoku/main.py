from board import *
from logic import *
from random import randint

def main_menu():
    while(True):
        print("********************************")
        print("Select a Sudoku Puzzle to Solve")
        print("1: Easy")
        print("2: Medium")
        print("3: Hard")
        print("4: Quit")
        print("********************************")
        puzzle = input(">>> ")
        print("********************************")

        puzzle_file = 'Puzzles'

        if puzzle in ['1', '2', '3', '4']:
            if puzzle == '4': break
            else:
                random_puzzle = randint(0, 299)
                while random_puzzle % 3 != (int(puzzle) - 1):
                    random_puzzle = randint(0, 299)

                puzzle_file += "/Puzzle" + str(random_puzzle) + ".txt"
                run_puzzle(Sudoku_Board(puzzle_file))
                break
        else:
            print("Please enter a valid selection.")

    print("Good bye.")

def print_message(section, val, row_or_col_num = None):
    if section == "Row" or section == "Col":
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!Invalid Input - %s %d has %d!!!!!!!!!!!!" % (section, row_or_col_num, val))
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
    else:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!Invalid Input - %s has %d !!!!!!!!!!!!!" % (section, val))
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")

def run_puzzle(board):
    while not is_solved(board):
        board.display()

        row = int(input("Enter Row Number: "))
        col = int(input("Enter Col Number: "))
        val = int(input("Enter Val Number: "))

        board.set_value(row, col, val)

        row_valid = is_row_valid(board, row)
        col_valid = is_col_valid(board, col)
        blk_valid = is_block_valid(board, row, col)

        if (not row_valid) or (not col_valid) or (not blk_valid):
            if not row_valid: print_message("Row", val, row)
            elif not col_valid: print_message("Col", val, col)
            else: print_message("Blk", val)

            board.set_value(row, col, 0)

        print("********************************")

    print("Congratulations! You completed the game.")

main_menu()
