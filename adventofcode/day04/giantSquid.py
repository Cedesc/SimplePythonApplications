

class Bingo_Board:

    def __init__(self, numbers_on_board: list[int]):

        if not len(numbers_on_board) == 25:
            print(f"Invalid number of input data: {len(numbers_on_board)} entries in input list {numbers_on_board}")

        else:
            self.data_row0: list[int] = numbers_on_board[:5]
            self.data_row1: list[int] = numbers_on_board[5:10]
            self.data_row2: list[int] = numbers_on_board[10:15]
            self.data_row3: list[int] = numbers_on_board[15:20]
            self.data_row4: list[int] = numbers_on_board[20:25]
            self.data_rows: list[list[int]] = [self.data_row0, self.data_row1, self.data_row2,
                                               self.data_row3, self.data_row4]

            self.mark_row0: list[bool] = [False for _ in range(5)]
            self.mark_row1: list[bool] = [False for _ in range(5)]
            self.mark_row2: list[bool] = [False for _ in range(5)]
            self.mark_row3: list[bool] = [False for _ in range(5)]
            self.mark_row4: list[bool] = [False for _ in range(5)]
            self.mark_rows: list[list[bool]] = [self.mark_row0, self.mark_row1, self.mark_row2,
                                                self.mark_row3, self.mark_row4]

    def __str__(self):
        return f"{self.data_row0}   {self.mark_row0}\n" \
               f"{self.data_row1}   {self.mark_row1}\n" \
               f"{self.data_row2}   {self.mark_row2}\n" \
               f"{self.data_row3}   {self.mark_row3}\n" \
               f"{self.data_row4}   {self.mark_row4}"


    def print_data_rows(self):
        return f"{self.data_row0}\n" \
               f"{self.data_row1}\n" \
               f"{self.data_row2}\n" \
               f"{self.data_row3}\n" \
               f"{self.data_row4}"

    def print_mark_rows(self):
        return f"{self.mark_row0}\n" \
               f"{self.mark_row1}\n" \
               f"{self.mark_row2}\n" \
               f"{self.mark_row3}\n" \
               f"{self.mark_row4}"

    def mark_number(self, number: int) -> None:
        for row_index in range(5):
            for column_index in range(5):
                if self.data_rows[row_index][column_index] == number:
                    self.mark_rows[row_index][column_index] = True

    def check_row(self, row_index: int) -> bool:
        """ Check one row if all entries are marked"""
        for entry in self.mark_rows[row_index]:
            if not entry:
                return False
        return True

    def check_all_rows(self) -> bool:
        """ Check all rows if ONE of them is fully marked """
        for row_index in range(5):
            if self.check_row(row_index):
                return True
        return False

    def check_column(self, column_index) -> bool:
        """ Check one column if all entries are marked"""
        for row in self.mark_rows:
            if not row[column_index]:
                return False
        return True

    def check_all_columns(self) -> bool:
        """ Check all columns if ONE of them is fully marked """
        for row_index in range(5):
            if self.check_row(row_index):
                return True
        return False

    def check_all_rows_and_columns(self) -> bool:
        """ Check all rows and columns if ONE row or column is fully marked, so it is a bingo """
        return self.check_all_rows() or self.check_all_columns()

    def sum_of_all_unmarked_numbers(self) -> int:
        """ Calculate the sum of all unmarked entries """
        result: int = 0
        for row_index in range(5):
            for column_index in range(5):
                if not self.mark_rows[row_index][column_index]:
                    result += self.data_rows[row_index][column_index]
        return result



def transform_txt_file(binary_report_text_file: str) -> (list[int], list[Bingo_Board]):

    bingo_numbers: list[int]
    bingo_boards: list[Bingo_Board] = []

    with open(binary_report_text_file, "r") as file:
        txt_elements: list[str] = file.read().split("\n\n")

    first_line = txt_elements[0].split(",")
    bingo_numbers = list(map(lambda x: int(x), first_line))

    for element in txt_elements[1::]:
        new_board_data: list[int] = []
        for element_row in element.split("\n"):
            for number_or_empty in element_row.split(" "):
                if number_or_empty != "":
                    new_board_data.append(int(number_or_empty))
            # Alternative to the previous 3 lines:
            # new_board_data += list(map(lambda s: int(s), filter(lambda el: el != "", element_row.split(" "))))
        bingo_boards.append(Bingo_Board(new_board_data))
        new_board_data.clear()

    print(bingo_numbers)
    print(bingo_boards[3])
    print(bingo_boards[3].mark_row3)
    bingo_boards[3].mark_number(40)
    print(bingo_boards[3].mark_row3)

    return bingo_numbers, bingo_boards


def bingo_calculation(input_numbers: list[int], possible_boards: list[Bingo_Board]) -> int:

    for number in input_numbers:
        for board in possible_boards:
            board.mark_number(number)
            if board.check_all_rows_and_columns():
                return number * board.sum_of_all_unmarked_numbers()



if __name__ == '__main__':

    numbers, boards = transform_txt_file('bingoBoards.txt')

    print(bingo_calculation(numbers, boards))

