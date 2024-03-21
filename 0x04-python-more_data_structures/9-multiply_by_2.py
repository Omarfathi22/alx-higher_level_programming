#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()
    list_keys = list(new_dir.keys())
    index = 0
    while index < len(list_keys):
        key = list_keys[index]
        new_dir[key] *= 2
        index += 1
    return new_dir
