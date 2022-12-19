#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num_ele = 0
    try:
        for i in range(x):
            if i == x - 1:
                print("{}".format(my_list[i]))
            else:
                print("{}".format(my_list[i]), end="")
            num_ele += 1
    except IndexError as err:
        print("")
    finally:
        return (num_ele)
