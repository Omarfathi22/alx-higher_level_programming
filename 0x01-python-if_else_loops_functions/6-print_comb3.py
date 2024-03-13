#!/usr/bin/python3
x = 0
while x < 10:
    y = x + 1
    while y < 10:
        if x == 8 and y == 9:
            print('89')
        else:
            print('{}{}, '.format(x, y), end='')
        y += 1
    x += 1
