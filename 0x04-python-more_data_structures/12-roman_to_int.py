#!/usr/bin/python3
def to_subtract(list_num):
    to_sub = 0
    max_list = max(list_num)
    index = 0
    while index < len(list_num):
        n = list_num[index]
        if max_list > n:
            to_sub += n
        index += 1
    return (max_list - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_n.keys())

    num = 0
    last_rom = 0
    list_num = [0]
    index_1 = 0
    while index_1 < len(roman_string):
        ch = roman_string[index_1]
        index_2 = 0
        while index_2 < len(list_keys):
            r_num = list_keys[index_2]
            if r_num == ch:
                if rom_n.get(ch) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [rom_n.get(ch)]
                else:
                    list_num.append(rom_n.get(ch))
                last_rom = rom_n.get(ch)
            index_2 += 1
        index_1 += 1
    num += to_subtract(list_num)

    return (num)
