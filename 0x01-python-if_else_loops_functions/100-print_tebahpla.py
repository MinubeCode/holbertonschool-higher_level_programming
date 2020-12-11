#!/usr/bin/python3


def uppercase():

    var = 122
    cont = 0
    var2 = 90

    while var >= 97:

        cont = cont + 1

        if cont % 2 == 0:
            var2 = var2 - 1
            print(chr(var2), end="")
            var2 = var2 - 1
        else:
            print(chr(var), end="")

        var = var - 1
