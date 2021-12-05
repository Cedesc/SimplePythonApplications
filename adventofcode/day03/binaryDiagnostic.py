from copy import copy
from functools import reduce


def calculate_gamma_and_epsilon(binary_report_text_file: str) -> (int, int):

    with open(binary_report_text_file, "r") as file:
        lines: list[str] = file.read().split("\n")


    occurences_of_ones_relative_to_zeros: list[int] = [0 for _ in range(len(lines[0]))]

    for binary_number in lines:

        for digit_index in range(len(binary_number)):

            if binary_number[digit_index] == "1":
                occurences_of_ones_relative_to_zeros[digit_index] += 1
            elif binary_number[digit_index] == "0":
                occurences_of_ones_relative_to_zeros[digit_index] -= 1
            else:
                print(f"Undefined Digit: {binary_number[digit_index]} in the number {binary_number}")


    gamma: str = ""
    epsilon: str = ""

    for entry in occurences_of_ones_relative_to_zeros:

        if entry < 0:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"


    return int(gamma, 2), int(epsilon, 2)


def calculate_oxygen_generator_and_CO2_scrubber_rating(binary_report_text_file: str) -> (int, int):

    with open(binary_report_text_file, "r") as file:
        lines_for_O: list[str] = file.read().split("\n")

    lines_for_C: list[str] = copy(lines_for_O)

    length_of_binary_numbers: int = len(lines_for_O[0])

    # Idea: Use "foldl" ("reduce" in python) to compute the relative occurences of ones to zeros, like in
    # "calculate_gamma_and_epsilon" and then filter the list.
    # Do this for every digit (for loop) and two times (for Oxygen Generator Rating and CO2 Scrubber Rating).
    for i in range(length_of_binary_numbers):

        if reduce(lambda num_of_ones, line: num_of_ones + 1 if line[i] == '1' else num_of_ones - 1, lines_for_O, 0) \
                >= 0:
            lines_for_O = list(filter(lambda line: line[i] == '1', lines_for_O))
        else:
            lines_for_O = list(filter(lambda line: line[i] == '0', lines_for_O))

        if reduce(lambda num_of_ones, line: num_of_ones + 1 if line[i] == '1' else num_of_ones - 1, lines_for_C, 0) \
                < 0:
            if len(list(filter(lambda line: line[i] == '1', lines_for_C))) != 0:
                lines_for_C = list(filter(lambda line: line[i] == '1', lines_for_C))
        else:
            if len(list(filter(lambda line: line[i] == '0', lines_for_C))) != 0:
                lines_for_C = list(filter(lambda line: line[i] == '0', lines_for_C))


    oxygen_generator_rating: str = lines_for_O[0]
    co2_scrubber_rating: str = lines_for_C[0]

    return int(oxygen_generator_rating, 2), int(co2_scrubber_rating, 2)


if __name__ == '__main__':

    g1, e1 = calculate_gamma_and_epsilon('report.txt')
    print(f"Gamma: {g1}  Epsilon: {e1}   \nProduct of those (Power Consumption): {g1 * e1}\n")

    g2, e2 = calculate_oxygen_generator_and_CO2_scrubber_rating('report.txt')
    print(f"Oxygen Generator Rating: {g2}  CO2 Scrubber Rating: {e2}   "
          f"\nProduct of those (Life Support Rating): {g2 * e2}")
