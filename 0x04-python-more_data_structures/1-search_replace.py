#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    index = 0
    while index < len(my_list):
        if my_list[index] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[index])
        index += 1
    return new_list
