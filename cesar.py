#!/usr/bin/env python3
# -*- coding: utf-8 -*-

FIRST_LETTER = ord('A')
LAST_LETTER = ord('Z')
NUM_LETTERS = LAST_LETTER - FIRST_LETTER + 1

DEFAULT_KEY = 3


def cifrado_cesar(s, key=DEFAULT_KEY):
    salida = ''
    for c in s.upper():
         num = ord(c)
         if FIRST_LETTER <= num <= LAST_LETTER:
            num = num + key
            if num > LAST_LETTER:
                num = FIRST_LETTER + (num % LAST_LETTER) - 1
         salida = salida + chr(num)
    return salida


def descifrado_cesar(s, key=DEFAULT_KEY):
    reverse_key = NUM_LETTERS - key
    return cifrado_cesar(s, reverse_key)

assert cifrado_cesar('A', key=1) == 'B'
assert cifrado_cesar('A') == 'D'
assert cifrado_cesar('W') == 'Z'
assert cifrado_cesar('X') == 'A'
assert cifrado_cesar('Y') == 'B'
assert cifrado_cesar('Z') == 'C'

print(cifrado_cesar('ALTEZA', key=3)) == 'DOWHCD'
assert cifrado_cesar('DOWHCD', key=23) == 'ALTEZA'

assert descifrado_cesar(cifrado_cesar('HOLA CESAR')) == 'HOLA CESAR'

