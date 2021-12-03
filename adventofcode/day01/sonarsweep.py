

def count_measurement_increases(measurement_text_file: str):

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


if __name__ == '__main__':
    print(count_measurement_increases('measurements.txt'))
