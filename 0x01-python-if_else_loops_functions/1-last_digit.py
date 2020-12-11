#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ultimoNro = int(repr(number)[-1])

if number < 0:
   ultimoNro = ultimoNro * -1

if ultimoNro > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, ultimoNro))
elif ultimoNro == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, ultimoNro))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, ultimoNro))
