#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101, 1):
        if (not num % 3):
            if (not num % 5):
                val = "FizzBuzz"
            else:
                val = "Fizz"
        elif (not num % 5):
            val = "Buzz"
        else:
            val = num
        print(f"{val}", end=" ")
