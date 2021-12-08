from functools import reduce


def transform_txt_file(vent_coordinates_txt_file: str) -> list[tuple[tuple[int, int], tuple[int, int]]]:

    vent_coordinates: list[tuple[tuple[int, int], tuple[int, int]]] = []

    with open(vent_coordinates_txt_file, "r") as file:
        lines: list[str] = file.read().split("\n")

    for line in lines:
        start_and_end: list[str] = line.split(" -> ")
        start: list[str] = start_and_end[0].split(",")
        end: list[str] = start_and_end[1].split(",")
        vent_coordinates.append( ( (int(start[0]), int(start[1])), (int(end[0]), int(end[1])) ) )

    return vent_coordinates


def find_max_x(coordinates: list[tuple[tuple[int, int], tuple[int, int]]]) -> int:
    return reduce(lambda a, b: max(a, max(b[0][0], b[1][0])), coordinates, 0)

def find_max_y(coordinates: list[tuple[tuple[int, int], tuple[int, int]]]) -> int:
    return reduce(lambda a, b: max(a, max(b[0][1], b[1][1])), coordinates, 0)


def calculate_vent_map(coordinates: list[tuple[tuple[int, int], tuple[int, int]]],
                       with_diagonals: bool = True) -> list[list[int]]:

    vent_map: list[list[int]] = [[0 for _ in range(find_max_x(coordinates) + 1)]
                                        for _ in range(find_max_y(coordinates) + 1)]

    for vent in coordinates:
        start_x: int = vent[0][0]
        start_y: int = vent[0][1]
        end_x: int = vent[1][0]
        end_y: int = vent[1][1]

        if start_x == end_x:
            if start_y <= end_y:
                for y in range(start_y, end_y + 1):
                    vent_map[y][start_x] += 1
            else:
                for y in range(end_y, start_y + 1):
                    vent_map[y][start_x] += 1

        elif start_y == end_y:
            if start_x <= end_x:
                for x in range(start_x, end_x + 1):
                    vent_map[start_y][x] += 1
            else:
                for x in range(end_x, start_x + 1):
                    vent_map[start_y][x] += 1

        elif with_diagonals:
            if start_x <= end_x:
                if start_y <= end_y:  # left top to right bot
                    print(f"left top to right bot with "
                          f"start_x = {start_x}, end_x = {end_x}, start_y = {start_y}, end_y = {end_y}")
                    for i in range(end_x + 1 - start_x):
                        vent_map[start_y + i][start_x + i] += 1
                else:  # left bot to right top
                    print(f"left bot to right top with "
                          f"start_x = {start_x}, end_x = {end_x}, start_y = {start_y}, end_y = {end_y}")
                    for i in range(end_x + 1 - start_x):
                        vent_map[start_y - i][start_x + i] += 1
            else:
                if start_y <= end_y:  # right top to left bot
                    print(f"right top to left bot with "
                          f"start_x = {start_x}, end_x = {end_x}, start_y = {start_y}, end_y = {end_y}")
                    for i in range(end_x + 1 - start_x):
                        vent_map[start_y + i][start_x - i] += 1
                else:  # right bot to left top
                    print(f"right bot to left top with "
                          f"start_x = {start_x}, end_x = {end_x}, start_y = {start_y}, end_y = {end_y}")
                    for i in range(end_x + 1 - start_x):
                        vent_map[start_y - i][start_x - i] += 1

        # else:
        #     print("Error! Every Vent should be vertical, horizontal or 45 Degrees diagonal!")
        #     print(f"Start x: {start_x}  End x: {end_x}\n"
        #           f"Start y: {start_y}  End y: {end_y}")
    print(vent_map)  # todo delete
    return vent_map


def calculate_overlapping_points(coordinates: list[tuple[tuple[int, int], tuple[int, int]]],
                                 with_diagonals: bool=True) -> int:

    vent_map: list[list[int]] = calculate_vent_map(coordinates, with_diagonals=with_diagonals)

    overlap_counter: int = 0

    for row in vent_map:
        for entry in row:
            if entry >= 2:
                overlap_counter += 1

    return overlap_counter



if __name__ == '__main__':

    coords: list[tuple[tuple[int, int], tuple[int, int]]] = transform_txt_file('ventTest.txt')

    # without Diagonals
    print(calculate_overlapping_points(coords, with_diagonals=False))  # 7473

    # with Diagonals
    # print(calculate_overlapping_points(coords, with_diagonals=True))
