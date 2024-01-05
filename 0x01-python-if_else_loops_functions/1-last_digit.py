#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of"
str2 = "is"
sign = False
if (number < 0):
    sign = True
    number = -1 * number
lastDigit = number % 10
if (sign):
    lastDigit = -1 * lastDigit
    number = -1 * number
if (lastDigit > 5):
    str3 = "and is greater than 5"
elif (lastDigit == 0):
    str3 = "and is 0"
else:
    str3 = "and is less than 6 and not 0"
print(f"{str1} {number} {str2} {lastDigit} {str3}")
