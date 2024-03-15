#!/usr/bin/python3

def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        i = 4
        while i < 6:
            c = add(c, i)
            i += 1
        return c
    else:
        return sub(a, b)
