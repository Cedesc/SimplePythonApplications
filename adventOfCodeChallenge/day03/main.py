TXT_FILE = 'input.txt'


def how_many_trees(right: int = 3, down: int = 1) -> int:
    counter = 0

    with open(TXT_FILE, "r") as file:
        lines = file.read().split("\n")

    row_length = len(lines[0])

    horizontal = 0
    vertical = 0

    for _ in range(len(lines) - 1):
        horizontal = (horizontal + right) % row_length
        vertical += down
        # print(vertical, horizontal)
        try:
            if lines[vertical][horizontal] == '#':
                counter += 1
        except:  # extreme ugly
            break

    return counter


if __name__ == '__main__':
    print(f"Answer 1:  {how_many_trees()}")

    result = how_many_trees(1, 1)
    result *= how_many_trees(3, 1)
    result *= how_many_trees(5, 1)
    result *= how_many_trees(7, 1)
    result *= how_many_trees(1, 2)
    print(f"Answer 2:  {result}")
