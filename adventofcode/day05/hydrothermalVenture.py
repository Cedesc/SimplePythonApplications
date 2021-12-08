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


def calculate_vent_map(coordinates: list[tuple[tuple[int, int], tuple[int, int]]]) -> list[list[int]]:

    vent_map: list[list[int]] = [[0 for _ in range(find_max_y(coordinates) + 1)]
                                        for _ in range(find_max_x(coordinates) + 1)]

    for vent in coordinates:
        start_x: int = vent[0][0]
        start_y: int = vent[0][1]
        end_x: int = vent[1][0]
        end_y: int = vent[1][1]

        for x in range(start_x, end_x + 1):
            vent_map[x][start_y] += 1

        for y in range(start_y + 1, end_y + 1):
            vent_map[start_x][y] += 1


    return vent_map


def calculate_overlapping_points(coordinates: list[tuple[tuple[int, int], tuple[int, int]]]) -> int:

    vent_map: list[list[int]] = calculate_vent_map(coordinates)

    overlap_counter: int = 0

    for row in vent_map:
        for entry in row:
            if entry >= 2:
                overlap_counter += 1

    return overlap_counter



if __name__ == '__main__':

    coords: list[tuple[tuple[int, int], tuple[int, int]]] = transform_txt_file('ventCoordinates.txt')
    print(calculate_overlapping_points(coords))
