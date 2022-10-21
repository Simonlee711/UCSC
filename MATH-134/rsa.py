"""
Module that will demonstarte the rsa cryptosystem
"""
import math

def encrypt(message, e, n):
    '''
    ciphertext = message ^ e mod n
    '''
    print(str(message), "^", str(e), " mod ",str(n))
    cipher = pow(int(message),int(e)) % int(n)
    return cipher

def decrypt(cipher, d, n):
    '''
    plaintext = message ^ d mod n
    '''
    print(str(cipher), "^", str(d), " mod ",str(n))
    plain = pow(int(cipher),int(d)) % int(n)
    return plain


if __name__ == '__main__':
    '''
    main function aka the driver code
    '''
    message = input("Enter a message(number): ")
    if message.isdigit():
        p = int(input("pick prime #1: "))
        q = int(input("pick prime #2: "))
        e = int(input("enter an public key (encryption key): "))
        n = p*q
        φ = (p-1) * (q-1)
        d = pow(e,-1,φ)

        # public information
        print("\npress enter for public information") 
        input()
        print("------------------------------")
        print("public information:")
        print("encryption key (public key) = ",e,"\nn = ",n)
        ciphertext = encrypt(message,e,n)
        print("ciphertext:",ciphertext)
        print("------------------------------\n")

        # private information
        print("press enter for private information") 
        input()
        print("------------------------------")
        print("private information:")
        print("p = ",p, "\nq = ", q, "\nφ(n) = ", φ, "\ndecryption key (private key) = ", d)
        plaintext = decrypt(ciphertext , d, n)
        print("plaintext:" ,plaintext)
        print("------------------------------")
    else:
        print("invalid input")