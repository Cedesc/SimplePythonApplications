

def count_measurement_increases(measurement_text_file: str) -> int:

    counter = 0

    with open(measurement_text_file, "r") as file:
        lines = file.read().split("\n")

    previous_number: int = int(lines[0])
    actual_number: int

    for line in lines:
        actual_number = int(line)
        if previous_number < actual_number:
            counter += 1
        previous_number = actual_number

    return counter


def count_sum_of_3_measurement_increases(measurement_text_file: str) -> int:

    counter = 0

    with open(measurement_text_file, "r") as file:
        lines = file.read().split("\n")

    second_predecessor_number: int = int(lines[0])
    first_predecessor_number: int = int(lines[1])
    actual_number: int = int(lines[2])

    previous_sum: int = second_predecessor_number + first_predecessor_number + actual_number
    actual_sum: int

    for line in lines[3::]:
        second_predecessor_number = first_predecessor_number
        first_predecessor_number = actual_number
        actual_number = int(line)

        actual_sum = second_predecessor_number + first_predecessor_number + actual_number

        if previous_sum < actual_sum:
            counter += 1

        previous_sum = actual_sum

    return counter


if __name__ == '__main__':
    print(count_measurement_increases('measurements.txt'))
    print(count_sum_of_3_measurement_increases('measurements.txt'))
