class Sudoku_Board:
    def __init__(self, text_file):
        puzzle = []
        puzzle_file = open(text_file)

        for line in puzzle_file.readlines():
            row = [ int(num) for num in line.strip('\n') ]
            puzzle.append(row)

        no_change = [
            [row, col] for row in range(0, 9) for col in range(0, 9) if puzzle[row][col] != 0
        ]

        self.grid = puzzle
        self.no_change = no_change

    def display(self):
        print("     0 1 2   3 4 5   6 7 8")

        for row in range(0, 9):
            display_row = "  " + str(row) + ": "

            for col in range(0, 9):
                display_row += str(self.grid[row][col]) + " "

                if col % 3 == 2: display_row += "| "

            print(display_row)

            if row % 3 == 2 and row != 8:
                print("-------------------------------")

    def set_value(self, row, col, new_value):
        if [row, col] in self.no_change:
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!!!!Invalid Input - Cannot Change Value!!!!" )
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        else:
            self.grid[row][col] = new_value
