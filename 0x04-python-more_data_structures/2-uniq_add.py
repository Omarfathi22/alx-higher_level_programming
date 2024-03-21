#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    num = 0
    uniq_iter = iter(uniq_list)

    while True:
        try:
            i = next(uniq_iter)
            num += i
        except StopIteration:
            break

    return num
