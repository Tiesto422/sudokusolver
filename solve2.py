

board_test = [
    [0, 5, 0, 6, 0, 0],
    [0, 0, 3, 5, 0, 0],
    [3, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 3],
    [0, 0, 2, 4, 0, 0],
    [0, 0, 1, 0, 6, 0]
]


def solve2(bd):
    find = find_empty2(bd)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 7):
        if valid2(bd, i, (row, col)):
            bd[row][col] = i

            if solve2(bd):
                return True

            bd[row][col] = 0

    return False


def valid2(bd, num, pos):
    for i in range(len(bd)):
        if bd[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(bd)):
        if bd[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 2

    for i in range(box_y * 2, box_y * 2 + 2):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bd[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board2(bd):

    for i, row in enumerate(bd):
        for j, val in enumerate(row):
            if j == 5:
                print(val)
            else:
                print(str(val) + " ", end="")

    print("\n")


def find_empty2(bd):

    for i, row in enumerate(bd):
        for j, val in enumerate(row):
            if val == 0:
                return (i, j)

    return None
