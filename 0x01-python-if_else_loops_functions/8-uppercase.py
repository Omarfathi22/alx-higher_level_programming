#!/usr/bin/python3
def uppercase(str):
    index = 0
    length = len(str)
    while index < length:
        if ord(str[index]) >= 97 and ord(str[index]) <= 122:
            print(chr(ord(str[index]) - 32), end="")
        else:
            print(str[index], end="")
        index += 1
    print()
