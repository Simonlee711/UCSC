"""
Module that will help demonstarte the Elgamal Cryptosystem.
This iteration of ElGamal will take in a string of test of any size and encode and decode the message. 
"""
__author__ = 'Simon Lee in Math 134, siaulee@ucsc.edu'

import random 
from math import pow
  
a = random.randint(2, 10)
  
def gcd(a, b):
    '''
    Simple function that will compute the gcd of two values a and b
    '''
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)
  

def keygen(q):
    '''
    Will randomly generate a very large number used as the key
    '''
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)
  
    return key
  

def Modular_exponentiation(a, b, c):
    '''
    Function that computes the modular exponentiation
    '''
    x = 1
    y = a
  
    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)
  
    return x % c
  

def encrypt(msg, q, h, g):
    '''
    Encryption function of the ElGamal Cryptosystem
    '''
    encrypted_msg = []
  
    k = keygen(q)# Private key for sender
    s = Modular_exponentiation(h, k, q)
    p = Modular_exponentiation(g, k, q)
      
    for i in range(0, len(msg)):
        encrypted_msg.append(msg[i])
  
    print("g^k used : ", p)
    print("g^ak used : ", s)
    for i in range(0, len(encrypted_msg)):
        encrypted_msg[i] = s * ord(encrypted_msg[i])
  
    return encrypted_msg, p
  
def decrypt(en_msg, p, key, q):
    '''
    Decryption function of the ElGamal Cryptosystem
    '''
    decrypted_msg = []
    h = Modular_exponentiation(p, key, q)
    for i in range(0, len(en_msg)):
        decrypted_msg.append(chr(int(en_msg[i]/h)))
          
    return decrypted_msg
  

if __name__ == '__main__':
    '''
    Main Driving function
    '''
    
    # asks user for message
    print("------------------------------")
    message = input("What's the message: ")
    print("------------------------------")
    print("Original Message :", message)
    print("------------------------------")
    
    #generates random key q and a second random key between 2 < x < q
    q = random.randint(pow(10, 20), pow(10, 50))
    g = random.randint(2, q)
  
    key = keygen(q)# Private key for receiver
    h = Modular_exponentiation(g, key, q)
    print("g used : ", g)
    print("g^a used : ", h)
  
    encrypted_msg, p = encrypt(message, q, h, g)
    print("------------------------------")
    print("Encrypted Message:", encrypted_msg)
    print("------------------------------")
    decrypted_msg = decrypt(encrypted_msg, p, key, q)
    decrypted = ''.join(decrypted_msg)
    print("Decrypted Message :", decrypted);
  
