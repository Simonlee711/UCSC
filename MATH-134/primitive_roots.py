"""
Module that will help find primtive roots of a number given certain criteria

Definition of Primitve Root:
That is, the integer g is a primitive root (mod n) if for every number aa relatively prime to n there is an integer z such that a ≡ (g^z (mod n)).
"""
__author__ = 'Simon Lee in Math 134, siaulee@ucsc.edu'

import math

def primtive_roots(number, mod):
    counter = 1
    for i in range(1, mod-1):
        print(str(number) + "^" + str(counter) + " mod " + str(mod))
        answer = pow(number, counter, mod)
        print(str(pow(number,counter)) + " mod " + str(mod) + " = " + str(answer))
        counter += 1
        if answer == 1:
            print(number, "is not a primitive root")
            return None
        if counter == mod - 1:
            print(number, "is a primitive root")
            return number
        
              


if __name__ == '__main__':
    #prime = int(input("maximum: "))
    mod = int(input("What number are you trying to find primitive roots: "))
    primitve_num = []
    for i in range(1, mod):
        print("------------------------------")
        number = primtive_roots(i,mod)
        if number != None:
            primitve_num.append(number)
    print("------------------------------")
    print(primitve_num)
