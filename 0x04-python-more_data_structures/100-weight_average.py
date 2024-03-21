#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    den = 0
    index = 0
    list_length = len(my_list)

    while index < list_length:
        tup = my_list[index]
        num += tup[0] * tup[1]
        den += tup[1]
        index += 1

    return (num / den)
