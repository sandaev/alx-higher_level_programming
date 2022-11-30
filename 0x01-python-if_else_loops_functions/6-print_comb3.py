#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if (i >= j):
            continue
        else:
            if (i < 8):
                print('{}{}'.format(i, j), end=", ")
            else:
                print('{}{}'.format(i, j))
