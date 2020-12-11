#!/usr/bin/python3


def fizzbuzz():

    for nro in range(1, 101):

        if nro % 3 == 0 and nro % 5 == 0:
            print("FizzBuzz", end=" ")
        elif nro % 3 == 0:
            print("Fizz", end=" ")
        elif nro % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(nro, end=" ")
