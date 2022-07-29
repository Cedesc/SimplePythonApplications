

class Button:

    def __init__(self, sound: str, color: str = None):
        self.sound: str = sound
        self.color: str = color  # todo better type like rgb value AND default should not be None

    def play_sound(self):
        pass


if __name__ == '__main__':
    pass
