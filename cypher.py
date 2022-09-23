# Division of PEMaCS
# CSCI-121 Elements of Computer Programming II
# Recitation 1 - Encryption with a password
# *******************************************************
import math
import string

alphabet = string.printable
ordinal_value = {ch: i for i, ch in enumerate(alphabet)}


def encrypt(message, password):
    encrypted_message = ''
    password = math.ceil(len(message) / len(password)) * password
    for index, ch in enumerate(message):
        pass_ch = password[index]
        key = ordinal_value[pass_ch]
        ord_of_ch = ordinal_value[ch]
        shifted_ord_of_ch = (ord_of_ch + key) % len(alphabet)
        encrypted_ch = alphabet[shifted_ord_of_ch]
        encrypted_message += encrypted_ch
    return encrypted_message


def decrypt(message, password):
    decrypted_message = ''
    password = math.ceil(len(message) / len(password)) * password
    for index, ch in enumerate(message):
        pass_ch = password[index]
        key = ordinal_value[pass_ch]
        ord_of_ch = ordinal_value[ch]
        shifted_ord_of_ch = (ord_of_ch - key) % len(alphabet)
        encrypted_ch = alphabet[shifted_ord_of_ch]
        decrypted_message += encrypted_ch
    return decrypted_message