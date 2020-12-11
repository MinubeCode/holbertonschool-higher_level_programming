#!/usr/bin/python3


def uppercase(str):

    convierte = 0
    imprime = ""

    for item in str:
        almacena = ord(item)
        almacena = almacena - 32
        imprime = chr(almacena)

        print("{}".format(imprime), end="")
