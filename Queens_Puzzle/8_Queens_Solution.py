import itertools
import time

def queen_arrangement(base_8):
    queen_arrangement = []

    row = 0
    while row < len(base_8):
        queen_arrangement.append([row, base_8[row]])
        row += 1

    return queen_arrangement

def queens_attack(queen_1, queen_2):
    #Check if two queens are at the same row or same column
    same_row = (queen_1[0] == queen_2[0])
    same_col = (queen_1[1] == queen_2[1])

    if (same_row or same_col):
        return True

    #Check if two queens are on the same diagonal
    x_change = queen_2[1] - queen_1[1]
    y_change = queen_2[0] - queen_1[0]

    if abs(x_change) == abs(y_change):
        return True

    #Otherwise, the function must return false
    return False

def check_arrangement(arrangement):
    number_coordinates = len(arrangement)

    i = 0
    while (i < number_coordinates):
        j = i + 1
        while (j < number_coordinates):
            queen_1 = arrangement[i]
            queen_2 = arrangement[j]

            if queens_attack(queen_1, queen_2):
                return False

            j += 1
        i += 1

    return True

my_list = [x for x in range(8)]

count = 0
files = {0: "a",1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}

print("Here is a list of solutions for the 8 Queens Puzzle:")
for permutation in itertools.permutations(my_list):
    test_arrangement = queen_arrangement(list(permutation))

    if check_arrangement(test_arrangement):
        list_coordinates = []

        for num_coordinates in test_arrangement:
            i = num_coordinates[0]
            j = num_coordinates[1]

            file = files[j]
            rank = str(8 - i)

            list_coordinates.append(file + rank)

        count += 1
        print(str(count) + ": " + str(list_coordinates))
        time.sleep(1)

print("The number of solutions to the queens puzzle =", count)
