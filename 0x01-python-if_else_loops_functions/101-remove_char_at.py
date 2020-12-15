#!/usr/bin/python3


def remove_char_at(str, n):

    aux = ""
    init = 0
    end = 0

    if n == 0:
        init = 1
        aux = str[init:]
    elif n == -1:
        aux = str[:-1]
    elif n < 0:
        init = n + 1
        end = n
        aux = str[:end] + str[init:]
    else:
        init = n + 1
        end = n
        aux = str[:end] + str[init:]

    return aux
