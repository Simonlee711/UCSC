"""
Module that will help find discrete logarithms of a number given certain criteria

Used to solve problems like:    2^x = 13 mod 19  (where we wish to find x)
"""
__author__ = 'Simon Lee in Math 134, siaulee@ucsc.edu'

import math

def discrete_log(base, mod, solution):
    counter = 1
    while True:
        print("Iteration " + str(counter))
        print(str(base) + "^" + str(counter) + " mod " + str(mod))
        answer = pow(base, counter, mod)
        if answer == solution:
            print(str(pow(base,counter)) + " mod " + str(mod) + " = " + str(answer))
            print("------------------------------")
            print(str(counter) + " is the exponent")
            print("------------------------------")
            break
        print(str(pow(base,counter)) + " mod " + str(mod) + " = " + str(answer))
        counter += 1
        print("------------------------------")          


if __name__ == '__main__':
    base = int(input("base: "))
    mod = int(input("mod: "))
    solution = int(input("solution: "))
    print("------------------------------")
    discrete_log(base,mod,solution)
