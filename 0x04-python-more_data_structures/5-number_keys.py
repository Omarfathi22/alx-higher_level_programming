#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0
    list_keys = list(a_dictionary.keys())
    index = 0
    while index < len(list_keys):
        num += 1
        index += 1
    return num
