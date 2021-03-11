#  Copyright (c) 2021. Clinton Fernandes (clintonf@gmail.com

from cryptography.fernet import Fernet


def generate_key(filename: str) -> None:
    f"""
    Generates am assymetric cryptographic key file.
    :param filename: filename to write key to
    :return: {None}
    """
    key = Fernet.generate_key()

    fh = open(filename, 'w')
    fh.write(key.decode())
    fh.close()


def get_key_from_file(filename: str) -> str:
    f"""
    Gets an encryption key from a file.

    :param filename: filename for the encryption key
    :return: {str} encryption key
    """
    fh = open(filename, 'r')
    key = fh.read()
    fh.close()
    return key


def encrypt(key: Fernet, message: str) -> bytes:
    f"""
    Encrypts a message.

    :param key: cryptographic key
    :param message: message to encrypt
    :return: {bytes}
    """

    token = key.encrypt(message.encode())

    return token


def decrypt(key: Fernet, encrypted_message: bytes) -> str:
    f"""
    Decrypts a message.

    :param key: encryption key
    :param encrypted_message:  message to decrypt
    :return: {str}
    """

    decrypted_message = key.decrypt(encrypted_message)

    return decrypted_message.decode()
