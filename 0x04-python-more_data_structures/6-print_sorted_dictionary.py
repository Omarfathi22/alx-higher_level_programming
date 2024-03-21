#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    index = 0
    while index < len(list_ord):
        key = list_ord[index]
        value = a_dictionary.get(key)
        print("{}: {}".format(key, value))
        index += 1
