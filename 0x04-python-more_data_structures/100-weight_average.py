#!/usr/bin/python3

def weight_average(my_list=[]):
    up = 0
    down = 0

    if len(my_list) != 0:
        for i in range(len(my_list)):
            up += my_list[i][0] * my_list[i][1]
            down += my_list[i][1]
        result = up / down
        return (result)
    return (0)
