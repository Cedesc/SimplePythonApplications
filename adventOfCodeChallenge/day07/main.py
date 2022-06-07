from Bag import Bag

TXT_FILE = 'input.txt'


def count_bags_with_shiny_gold_bag() -> int:

    counter = 0

    with open(TXT_FILE, "r") as file:
        lines = file.read().split("\n\n")

    return counter


def create_bags(lines: list[str]) -> list[Bag]:

    bags: list[Bag] = []


    return bags


def create_bag(line: str) -> Bag:

    words = line.split(" ")

    bag_name = f"{words[0]} {words[1]}"

    return Bag(bag_name, line)



if __name__ == '__main__':
    print(f"Answer 1:   {count_bags_with_shiny_gold_bag()}")
    x = create_bag("light beige bags contain 5 dark green bags, 5 light gray bags, 3 faded indigo bags, 2 vibrant aqua bags.")
