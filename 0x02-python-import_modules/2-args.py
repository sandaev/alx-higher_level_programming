#!/usr/bin/python3
import sys
if __name__ == "__main__":

    argv_len = len(sys.argv) - 1
    if (argv_len >= 1):
        if (argv_len == 1):
            print('{} argument:'.format(argv_len))
        else:
            print('{} arguments:'.format(argv_len))
        for i in range(argv_len):
            print('{}: {}'.format((i + 1), sys.argv[i + 1]))
    else:
        print('{} arguments.'.format(argv_len))
