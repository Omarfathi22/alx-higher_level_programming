#!/usr/bin/python3
i = ord('z')
while i >= ord('a'):
    if i % 2 == 0:
        diff = 0
    else:
        diff = 32
    print('{}'.format(chr(i - diff)), end='')
    i -= 1
