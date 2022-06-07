import string


TXT_FILE = 'input.txt'


def total_sum_of_yes(everyone: bool) -> int:

    counter = 0

    with open(TXT_FILE, "r") as file:
        group_answers = file.read().split("\n\n")


    for group in group_answers:
        if everyone:
            counter += group_sum_of_everyone_yes(group)
        else:
            counter += group_sum_of_anyone_yes(group)


    return counter


def group_sum_of_anyone_yes(group_answers: str) -> int:

    # lines = group_answers.split("\n")

    group_answers = group_answers.replace("\n", "")

    set_of_answers = set()

    # print("")
    for answer in group_answers:
        # print("++++++++++++")
        # print(answer)
        set_of_answers.add(answer)
    # print(set_of_answers)
    # print(len(set_of_answers))

    return len(set_of_answers)


def group_sum_of_everyone_yes(group_answers: str) -> int:

    remaining_letters = string.ascii_lowercase

    # group_answers = group_answers.replace("\n", "")

    lines = group_answers.split("\n")

    set_of_answers = set()

    print(lines)
    print("#####################")


    for line in lines:
        for letter in remaining_letters:
            if letter not in line:
                remaining_letters = remaining_letters.replace(letter, "")

    # print(remaining_letters)


    return len(remaining_letters)



if __name__ == '__main__':
    print(f"Answer 1:   {total_sum_of_yes(everyone=False)}")

    print(f"Answer 2:   {total_sum_of_yes(everyone=True)}")
