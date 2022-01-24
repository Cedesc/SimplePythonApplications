import secrets
import string


def createSecurePassword(password_length=40):
    """ The recommendation of the BSI is a entropy of 100 Bit
    With len(chars) == 94 is the entropy per character 6.555 Bit
    So the passwords must consist of at least 16 characters
    Note: I remove some ambiguous characters, so the password is less secure than with the full alphabet """

    # create alphabet
    chars = string.digits + string.ascii_letters + string.punctuation

    # remove ambiguous characters
    for letter in ["I", "l", "1", "|", "0", "O", "'", "`", "´"]:
        chars = chars.replace(letter, "")

    # print alphabet which is used for password generation
    # print(chars)

    # print created password
    print(''.join(secrets.choice(chars) for _ in range(password_length)))


if __name__ == '__main__':

    createSecurePassword(password_length=40)

    while True:
        length = input('\nGib "exit" oder nichts ein um das Programm zu beenden\n'
              'Gib eine Zahl x ein um ein Passwort der Länge x zu erstellen\n')
        if length == "" or length == "exit":
            break
        createSecurePassword(password_length=int(length))
