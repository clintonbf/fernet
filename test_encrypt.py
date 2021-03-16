#  Copyright (c) 2021. Clinton Fernandes (clintonf@gmail.com

from fernet_encrypt_decrypt import *

def unpad (padded):
    pad = ord(padded[-1])
    return padded[:-pad]


def do_normal_test():
    """
    Demonstrates "normal" behaviour of the library.

    :return:
    """
    filename = "keyfile"
    message = "Hi HoboCat!"

    generate_key()

    key = get_key_from_file(filename)

    encrypted_message = encrypt(key, message)
    print("Message:", message, "is encrypted as", encrypted_message.decode())

    decrypted_message = decrypt(key, encrypted_message)
    print("Decrypted message is:", decrypted_message)


def do_node_test():
    """
    Decrypts a message encrypted by a node.js program.
        DOES NOT WORK.
    :return:
    """
    filename = "keyfile"
    key = get_key_from_file(filename)

    encrypted_message = unpad("i4VedWYyZvLIBRWgJp8krIln1K2K1Bz6Derb9sDkDt0=")
    decrypted_message = decrypt(key, bytes(encrypted_message, 'utf8'))
    print("Decrypted message is:", decrypted_message)


def main():
    # do_node_test()
    do_normal_test()


if __name__ == '__main__':
    main()