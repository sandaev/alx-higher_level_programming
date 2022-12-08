#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if len(a_dictionary) > 0:
        new_dic = {}
        for k, v in a_dictionary.items():
            new_dic[k] = v * 2
        return (new_dic)
    return (a_dictionary)
