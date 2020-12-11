#!/usr/bin/python3


def print_last_digit(number):

    ultimoNro = int(repr(number)[-1])
    print("{:d}".format(ultimoNro), end="")

    return ultimoNro
