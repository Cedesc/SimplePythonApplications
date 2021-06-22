from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

# https://youtu.be/uZ9WWzkH17I bis 18:00min

""" Only good for single passwords, because the program would take too much time for whole files """


def generate_sk():
    """ generates a secret key and saves it in a keys/secret_key.pem file """
    generated_secret_key = RSA.generate(3072)
    with open("keys/secret_key.pem", "wb") as f_out:
        f_out.write(generated_secret_key.export_key(format='PEM'))
    return generated_secret_key


def import_key(file_name):
    """ imports and returns the specified key in the file_name"""
    with open(file_name, 'rb') as f_in:
        imported_key = RSA.import_key(f_in.read())
    return imported_key


def generate_pk(sk_input):
    """ generates a public key and saves it in a keys/public_key.pem file """
    generated_public_key = sk_input.publickey()
    with open("keys/public_key.pem", "wb") as f_out:
        f_out.write(generated_public_key.export_key(format='PEM'))
    return generated_public_key


def encrypt(pk_receiver, message):
    """ encrypts a message and returns the result
    :type pk_receiver: RSA public key
    :type message: bytes/bytearray/memoryview (Example: b"Hello World!")
    """
    cipher = PKCS1_OAEP.new(pk_receiver)
    encrypted_message = cipher.encrypt(message)
    return encrypted_message


def decrypt(sk, encrypted_message):
    """ decrypts a cipher and returns the result
    :type sk: RSA secret key
    :type encrypted_message: bytes/bytearray/memoryview
    """
    cipher = PKCS1_OAEP.new(sk)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message




if __name__ == '__main__':
    # generate_sk()
    secret_key = import_key('keys/secret_key.pem')
    public_key = generate_pk(secret_key)
    c = encrypt(public_key, b"hey hey yeah")
    print(f"Encrypted Message: {c}")
    m = decrypt(secret_key, c)
    print(f"Decrypted Message: {m}")
