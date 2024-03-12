#!/usr/bin/python3
def uppercase(str):
    result = ''
    for char in str:
        if 97 <= ord(char) <= 122:
            upp = chr(ord(char) - 32)
            result += '{}'.format(upp)
        else:
            result += '{}'.format(char)
    print('{}'.format(result))
