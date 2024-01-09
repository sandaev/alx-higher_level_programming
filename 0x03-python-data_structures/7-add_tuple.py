#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) == 0 and len(tuple_b) == 0:
        x = 0
        y = 0
    elif len(tuple_a) == 0:
        x = tuple_b[0]
        y = tuple_b[1]
    elif len(tuple_b) == 0:
        x = tuple_a[0]
        y = tuple_b[1]
    elif len(tuple_a) == 1 or len(tuple_b) == 1:
        if len(tuple_a) == 2:
            y = tuple_a[1]
        elif len(tuple_b) == 2:
            y = tuple_b[1]
        else:
            y = 0
        x = tuple_a[0] + tuple_b[0]
    else:
        x = tuple_a[0] + tuple_b[0]
        y = tuple_a[1] + tuple_b[1]

    new_tuple = (x, y)

    return (new_tuple)
