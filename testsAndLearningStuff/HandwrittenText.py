from pywhatkit import text_to_handwriting

# https://www.youtube.com/watch?v=a7MrAoVYdzk


def myTextToHandwritten(input_text: str):
    text_to_handwriting(input_text, 'out.jpg', (0, 0, 150))


if __name__ == '__main__':
    text = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut \n" \
           "labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores \n" \
           "et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
    myTextToHandwritten(text)
