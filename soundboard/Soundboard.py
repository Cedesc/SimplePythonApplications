from Button import Button


class Soundboard:

    def __init__(self, width: int, height: int, buttons: list[Button] = None):

        if buttons is None:
            buttons = list()

        # if the number of buttons exceeds the maximal number of fields, an Exception will be thrown
        if len(buttons) < width * height:
            raise Exception

        # the board is a list with "height" lists
        self.board: list[list[Button]] = list(list() * height)
        # assign a field to every button, from top left to bottom right
        for b_index in range(len(buttons)):
            self.board[b_index // width].append(buttons[b_index])


if __name__ == '__main__':
    pass
