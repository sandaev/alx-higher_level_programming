#!/usr/bin/python3
from builtins import dir
if __name__ == "__main__":
    names = dir("hidden_4.pyc")
    len_names = len((dir("hidden_4.pyc")))
    for i in range(len_names):
        if (names[i][0] == '_'):
            continue
        print('{}'.format(names[i]))
