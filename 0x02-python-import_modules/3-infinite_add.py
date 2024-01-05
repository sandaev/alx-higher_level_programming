#!/usr/bin/python3
import sys
if __name__ == "__main__":
    total = 0
    args_len = len(sys.argv) - 1
    for i in range(args_len):
        i += 1
        total += int(sys.argv[i])
    print('{}'.format(total))
