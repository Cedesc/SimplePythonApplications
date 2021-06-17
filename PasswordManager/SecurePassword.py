import secrets
import string


def createSecurePassword(password_length=40):
    """ The recommendation of the BSI is a entropy of 100 Bit
    With len(chars) == 94 is the entropy per character 6.555 Bit
    So the passwords must consist of at least 16 characters """
    chars = string.digits + string.ascii_letters + string.punctuation
    print(''.join(secrets.choice(chars) for _ in range(password_length)))


if __name__ == '__main__':
    createSecurePassword(password_length=40)
