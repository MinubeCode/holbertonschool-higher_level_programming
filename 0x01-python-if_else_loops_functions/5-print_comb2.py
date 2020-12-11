#!/usr/bin/python3

for secuencia in range(0, 100):
    if secuencia <= 9:
        print("0{:d}, ".format(secuencia), end="")
    else:
        print("{}".format(secuencia), end=", " if secuencia < 99 else "\n")
