import math

TXT_FILE = 'input.txt'


def get_highest_seat_ID() -> int:

    highest_id = 0

    with open(TXT_FILE, "r") as file:
        lines = file.read().split("\n")

    row_specifier = lines[0][:7]
    column_specifier = lines[0][7:]
    print(row_specifier)
    print(column_specifier)


    return highest_id


def get_row(specifier: str) -> int:

    min_row = 0
    max_row = 127
    # 0 1 2 3 4 5 6 7

    for letter in specifier:

        mean = calculate_distance(min_row, max_row)

        if letter == 'L':
            max_row -= mean
        if letter == 'R':
            min_row += mean
        else:
            raise Exception

    if min_row != max_row:
        raise Exception

    return min_row


def get_column(specifier: str) -> int:

    min_column = 0
    max_column = 7
    # 0 1 2 3 4 5 6 7

    for letter in specifier:

        mean = calculate_distance(min_column, max_column)

        if letter == 'L':
            max_column -= mean
        if letter == 'R':
            min_column += mean
        else:
            raise Exception

    if min_column != max_column:
        raise Exception

    return min_column


def calculate_ID(row: int, column: int) -> int:
    return row * 8 + column


def calculate_distance(min_value: int, max_value: int) -> int:
    return math.ceil((max_value - min_value) / 2)


if __name__ == '__main__':
    # print(f"Answer 1:  {get_highest_seat_ID()}")
    print((0 + 7) // 2)
    print(math.ceil(7))
