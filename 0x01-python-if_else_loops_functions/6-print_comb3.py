#!/usr/bin/python3
secuencia = 0

while secuencia < 90:

    if secuencia <= 9:
        print("0{:d}, ".format(secuencia), end="")
    else:
        if secuencia == 10:
            secuencia = secuencia + 1
        elif secuencia == 20:
            secuencia = secuencia + 2
        elif secuencia == 30:
            secuencia = secuencia + 3
        elif secuencia == 40:
            secuencia = secuencia + 4
        elif secuencia == 50:
            secuencia = secuencia + 5
        elif secuencia == 60:
            secuencia = secuencia + 6
        elif secuencia == 70:
            secuencia = secuencia + 7
        elif secuencia == 80:
            secuencia = secuencia + 8
        else:
            print("{}".format(secuencia), end=", " if secuencia < 89 else "\n")

    secuencia = secuencia + 1
