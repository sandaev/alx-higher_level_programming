#!/usr/bin/python3

def roman_to_int(roman_string):
    dic = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    if not isinstance(roman_string, str):
        return (0)
    elif roman_string is None or not roman_string.isalpha():
        return (0)
    elif len(roman_string) == 0:
        return (0)
    for i in roman_string:
        if i.lower() not in dic.keys():
            return (0)
    total = 0
    roman_string = list(roman_string.lower())
    while len(roman_string):
        if len(roman_string) == 1:
            total += dic[roman_string[0]]
            del roman_string[0]
        elif dic[roman_string[0]] >= dic[roman_string[1]]:
            total += dic[roman_string[0]]
            del roman_string[0]
        else:
            total += dic[roman_string[1]] - dic[roman_string[0]]
            del roman_string[0]
            del roman_string[0]
    return (total)
