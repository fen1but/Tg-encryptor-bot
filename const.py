import os
from os import environ

token = environ['token']

eng_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

eng_alphabet_up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

leet_alphabet = [['A', 'a', '4', '/\\', '@', 'λ'], ['B', 'b', '6', '8', '13', 'I3', '|3', 'β'], ['C', 'c', '(', '<', '©'], ['D', 'd', '|)', '[)', 'I)'], ['E', 'e', '3', 'ё', '€', '[-'], ['F', 'f', ']=', '|=', 'I='], ['G', 'g', '(_+', 'C-', '(_-'], ['H', 'h', '/-/', '[-]', ']-[', ')-(', '#', '}{'], ['I', 'i', '1', '!', '|'], ['J', 'j', '_|', '_/', '_7', '_)'], ['K', 'k', '|<', '|(', '|X'], ['L', 'l', '£', '1_', '|_', ], ['M', 'm', '/\/\\', '|V|', '(T)', '|\/|', '^^', '|^^|'], ['N', 'n', '|\|', '/\/'], ['O', 'o', '0', '()', '[]', 'Ω'], ['P', 'p', '|*', '|o', '|>', '?', '9', '|D'], ['Q', 'q', '(_,)', 'O,', '(,)'], ['R', 'r', '12', '|?', '|2', 'Я'], ['S', 's', '5', '$'], ['T', 't', '7', '+', '-|-'], ['U', 'u', '|_|', 'L|', '(_)'], ['V', 'v', '\/', '\\\//', '√'], ['W', 'w', '\/\/', 'VV', '\V/', '\|/', 'UU'], ['X', 'x', '><', ')(', '*'], ['Y', 'y', '"/', 'λ'], ['Z', 'z', '7_', '2', '>_', '%']]

def translateMessage(keyword, txt, dec1):
    translated = []
    keyIndex = 0
    keyword = keyword.lower()
    for symbol in txt:
        try:
            numm = eng_alphabet.index(symbol.lower())
            if dec1 == 1:
                numm += eng_alphabet.index(keyword[keyIndex])
            elif dec1 == 2:
                numm -= eng_alphabet.index(keyword[keyIndex])
            numm %= len(eng_alphabet)
            if symbol.isupper():
                translated.append(eng_alphabet[numm].lower())
            elif symbol.islower():
                translated.append(eng_alphabet[numm])
            keyIndex += 1
            if keyIndex == len(keyword):
                keyIndex = 0
        except ValueError:
            translated.append(symbol)
    return ''.join(translated)

def encryptMessage(keyword, txt):
    return translateMessage(keyword, txt, 1)

def decryptMessage(keyword, txt):
    return translateMessage(keyword, txt, 2)
