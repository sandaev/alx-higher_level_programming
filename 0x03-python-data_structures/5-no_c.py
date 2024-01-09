#!/usr/bin/python3
def no_c(my_string):

    str_list = list(my_string)
    # list of idx of c and C
    remove_idx = [i for i in range(len(my_string))
                  if my_string[i] == 'c' or my_string[i] == 'C']
    for i in range(len(remove_idx)):
        idx = remove_idx[i] - i
        del str_list[idx]
    new_str = "".join(str_list)
    return (new_str)
