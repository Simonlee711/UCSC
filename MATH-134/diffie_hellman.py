"""
Module that will help demonstarte the Elgamal Cryptosystem.
"""

__author__ = 'Simon Lee in Math 134, siaulee@ucsc.edu'

import math

def shared_key(base, prime, a, b):
    '''
    parameters:
    :g - public key 
    :base - base number
    :prime - modulus
    :a_private_key - raise the base to this power (kept secret)
    :b_private_key - raise the base to this power (kept secret)

    Alice -> Bob

        g = base^a_private_key mod prime

    Bob -> Alice 

        g = base^b_private_key mod prime
    
    Shared key:

        shared_key = g^private_key mod prime
    '''
    print("------------------------------\n")
    a_public_key = pow(base,a,prime)
    b_public_key = pow(base,b,prime)
    sharedkey1 = pow(b_public_key, a_private_key,prime)
    sharedkey2 = pow(a_public_key, b_private_key,prime)
    return a_public_key, b_public_key, sharedkey1, sharedkey2



if __name__ == '__main__':
    '''
    Driver code
    '''
    print("------------------------------")
    prime = int(input("What is the prime number you wish to compute: "))
    base = int(input("What is the base: "))
    a_private_key = int(input("What is Alice's private key: "))
    b_private_key = int(input("What is Bob's private key: "))
    pub1, pub2, share1, share2 = shared_key(base, prime, a_private_key, b_private_key)
    print("Press enter for public information\n")
    print("------------------------------")
    input()
    print("Prime number (modulus):", prime, "\nBase:", base, "\nPublic Key (Alice):", pub1, "\nPublic Key (Bob):", pub2, "\n")
    print("------------------------------\n")
    print("Press enter for private information\n")
    print("------------------------------")
    input()
    print("Alice's Private key:",a_private_key,"\nBob's Private key:", b_private_key, "\nShared key:", share1, "=", share2)
    print("Shared key is", share1,"\n")
    print("------------------------------")