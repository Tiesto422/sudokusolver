

board_test = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve3(bd):
    find = find_empty3(bd)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid3(bd, i, (row, col)):
            bd[row][col] = i

            if solve3(bd):
                return True

            bd[row][col] = 0

    return False


def valid3(bd, num, pos):
    for i in range(len(bd)):
        if bd[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(bd)):
        if bd[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bd[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board3(bd):

    for i, row in enumerate(bd):
        for j, val in enumerate(row):
            if j == 8:
                print(val)
            else:
                print(str(val) + " ", end="")

    print("\n")


def find_empty3(bd):

    for i, row in enumerate(bd):
        for j, val in enumerate(row):
            if val == 0:
                return (i, j)

    return None
