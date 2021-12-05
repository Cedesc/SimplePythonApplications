

def calculate_horizontal_position_and_depth(command_text_file: str) -> (int, int):

    x_coord: int = 0
    depth: int = 0

    with open(command_text_file, "r") as file:
        lines: list[str] = file.read().split("\n")

    for line in lines:
        command, value = line.split(" ")

        if command == "forward":
            x_coord += int(value)

        elif command == "down":
            depth += int(value)

        elif command == "up":
            depth -= int(value)

        else:
            print("Undefined Command: " + line)

    return x_coord, depth


def calculate_horizontal_position_and_depth_with_aim(command_text_file: str) -> (int, int):

    x_coord: int = 0
    depth: int = 0
    aim: int = 0

    with open(command_text_file, "r") as file:
        lines: list[str] = file.read().split("\n")

    for line in lines:
        command, value = line.split(" ")

        if command == "forward":
            x_coord += int(value)
            depth += int(value) * aim

        elif command == "down":
            aim += int(value)

        elif command == "up":
            aim -= int(value)

        else:
            print("Undefined Command: " + line)

    return x_coord, depth


if __name__ == '__main__':

    x1, d1 = calculate_horizontal_position_and_depth('commands.txt')
    print("Without Aim:")
    print(f"Horizontal Position: {x1}  Depth: {d1}  \nProduct of those: {x1 * d1}\n")

    x2, d2 = calculate_horizontal_position_and_depth_with_aim('commands.txt')
    print("With Aim:")
    print(f"Horizontal Position: {x2}  Depth: {d2}  \nProduct of those: {x2 * d2}")

