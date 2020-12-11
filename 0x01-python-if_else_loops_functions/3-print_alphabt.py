#!/usr/bin/python3

caracter = 97

while caracter < 123:
    if caracter == 113 or caracter == 101:
        caracter = caracter + 1
        continue
    else:
        print("{:c}".format(caracter), end="")
        caracter = caracter + 1
