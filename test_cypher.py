import pytest
from cypher import *


def test_encrypt_1():
    expected = '_T8/szUG'
    actual = encrypt('Elements', 'My Secret Password')
    assert expected == actual


def test_encrypt_2():
    expected = '_T8/szUGn\n'
    actual = encrypt('Elements 2', 'My Secret Password')
    assert expected == actual


def test_encrypt_3():
    expected = 'QsgD4um5f'
    actual = encrypt('4 me 2 be', 'My pass 1234')
    assert expected == actual


def test_encrypt_4():
    import string
    expected = 'acegikmoqsuwyACEGIKMOQSUWY!#%\')+-/;=?[]_{} \n\x0b02468ac!#%\')+-/;=?[]_{} ' \
               '\n\x0b02468acegikmoqsuwyACEGIKMOQSU'
    actual = encrypt(string.printable, string.ascii_letters)
    assert expected == actual


def test_decrypt_1():
    expected = 'Elements'
    actual = decrypt('_T8/szUG', 'My Secret Password')
    assert expected == actual


def test_decrypt_2():
    expected = 'Elements 2'
    actual = decrypt('_T8/szUGn\n', 'My Secret Password')
    assert expected == actual


def test_decrypt_3():
    expected = '4 me 2 be'
    actual = decrypt('QsgD4um5f', 'My pass 1234')
    assert expected == actual


def test_decrypt_4():
    import string
    expected = string.printable
    actual = decrypt('acegikmoqsuwyACEGIKMOQSUWY!#%\')+-/;=?[]_{} \n\x0b02468ac!#%\')+-/;=?[]_{} '
                     '\n\x0b02468acegikmoqsuwyACEGIKMOQSU', string.ascii_letters)
    assert expected == actual
