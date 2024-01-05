#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        sign = True
        number = -1 * number
    lastDigit = number % 10
    print(lastDigit, end="")
    return (lastDigit)
