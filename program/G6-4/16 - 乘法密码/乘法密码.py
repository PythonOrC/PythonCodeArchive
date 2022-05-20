from math import gcd
from random import choice
from string import ascii_lowercase


def encrypt(plaintext):
    letter = ascii_lowercase + " "
    keys = []
    cipher = ""
    length = len(letter)

    for i in range(2, length - 1):
        if gcd(i, length) == 1:
            keys.append(i)
    key = choice(keys)

    for char in plaintext:
        m_index = letter.index(char)
        c_index = (m_index * key) % length
        cipher += letter[c_index]
    return cipher, key


def inverse_mod(k, n):
    for i in range(2, n):
        if (k * i) % n == 1:
            return i
    print("Invalid Key")
    return None


def decrypt(ciphertext, key):
    letter = ascii_lowercase + " "
    plain = ""
    length = len(letter)
    key = inverse_mod(key, length)

    for char in ciphertext:
        c_index = letter.index(char)
        m_index = (c_index * key) % length
        plain += letter[m_index]
    return plain, key


plaintext = "time lost cannot be won again"
print(plaintext)
print(encrypt(plaintext))
print(decrypt(*encrypt(plaintext)))
