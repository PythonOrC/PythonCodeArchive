import string
from random import randint, choice
import collections
from math import gcd


def encrypt(plaintext):
    letters = string.ascii_letters
    n = len(letters)
    k1s = []
    for i in range(1, n):
        if gcd(n, i) == 1:
            k1s.append(i)
    k1 = choice(k1s)
    k2 = randint(0, n)
    ciphertext = ""
    for char in plaintext:
        try:
            m = letters.index(char)
            c = (m * k1 + k2) % n
            ciphertext += letters[c]
        except Exception:
            ciphertext += char
    return ciphertext, k1, k2


def check_only(text):
    d = collections.Counter(text)
    cnt = collections.Counter()
    for key, value in d.items():
        if value > 1:
            cnt[key] = value
    return cnt


def inverse_mod(key, N):
    for i in range(1, N):
        if (key * i) % N == 1:
            return i
    return False


def decrypt(content, K1, K2):
    letters = string.ascii_letters
    N = len(letters)
    K1_inverse = inverse_mod(K1, N)
    plaintext = ""
    for char in content:
        try:
            ind = letters.index(char)
            ind = (ind - K2) * K1_inverse % N
            decryption_char = letters[ind]
            plaintext += decryption_char
        except:
            plaintext += char
    return plaintext, K1_inverse


print(encrypt("knowledge is power"))
print(decrypt("xVEsRu Kdyi",23,3))