"""
Module that will help demonstarte the Elgamal Cryptosystem.
This iteration of ElGamal will take in a integer of any size and encode and decode the message. 
(Similar to the one learned in class)
"""
__author__ = 'Simon Lee in Math 134, siaulee@ucsc.edu'

import math
import random


def encrypt(public_key, base, msg, k, prime):
    '''
    To encrypt follow the simple formula

    (c1,c2)[cipher text] = (base^k, publickey^k * msg) mod prime

    k - random element generated between 50 and prime
    public key - base^a or base^b depending on the direction
    '''
    c1 = pow(base, k) % prime
    c2 = (pow(public_key, k) * msg) % prime

    return c1, c2


def decrypt(clue,mask,prime,privatekey):
    '''
    To decrypt follow the even simpler formula

    (c1,c2) = (clue,mask) so,

    original msg = (clue^(prime-1-privatekey) * mask) mod prime 
    '''
    exponent = prime - 1 - privatekey
    msg = (pow(clue, exponent) * mask) % prime

    return msg


if __name__ == '__main__':
    '''
    Driver code
    '''
    print("------------------------------")
    prime = int(input("What is the prime number you wish to compute: "))
    base = int(input("What is the base: "))
    a_private_key = int(input("What is Alice's private key: "))
    b_private_key = int(input("What is Bob's private key: "))
    message = int(input("What is the message you wish to encrypte/decrypt: "))
    while True:
        direction = input("Would you like to send from: Alice -> Bob (A) or Bob -> Alice (B): ").upper()
        print("------------------------------")
        if direction == 'A':
            b_public_key = pow(base,b_private_key) % prime
            rand_element = random.randint(50,prime)
            clue, mask = encrypt(b_public_key, base, message, rand_element, prime)
            d_msg = decrypt(clue, mask, prime, b_private_key)
            print ("Original Message:", message)
            print("Encrypted Message: (",clue,",",mask,")")
            print("Decrypted Message:",d_msg)
            print("------------------------------")
            break
        if direction == 'B':
            a_public_key = pow(base,a_private_key) % prime
            rand_element = random.randint(50,prime)
            clue, mask = encrypt(a_public_key, base, message, rand_element, prime)
            d_msg = decrypt(clue, mask, prime, a_private_key)
            print ("Original Message:", message)
            print("Encrypted Message: (",clue,",",mask,")")
            print("Decrypted Message:",d_msg)
            print("------------------------------")
            break
        else:
            print("invalid choice")
            print("------------------------------")
            continue
