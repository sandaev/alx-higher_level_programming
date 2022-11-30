#!/usr/bin/python3
for num in range(100):
    if (num < 99):
        print('{num:02d}'.format(num=num), end=", ")
    else:
        print('{}'.format(num))
