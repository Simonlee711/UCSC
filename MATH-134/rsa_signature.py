'''
Program that demonstartes how to verify an rsa digital signature
'''

__author__ = 'Simon Lee in Math 134, siaulee@ucsc.edu'

import math

if __name__ == '__main__':
    '''
    main function aka the driver code
    '''
    print("------------------------------")
    choice = input("Do you know private information? (Y or N): ").upper()
    if choice == 'Y':
        # enter private info p and q
        print("------------------------------")
        p = int(input("pick prime #1: "))
        q = int(input("pick prime #2: "))
        e = int(input("enter an public key (encryption key): "))
        print("------------------------------")

        # enter document so digital signature can be generated
        n = p*q
        print(n)
        document = int(input("Enter a document from 1 < x <= n: "))
        print("------------------------------")
        # computing important information
        φ = (p-1) * (q-1)
        d = pow(e,-1,φ)
        signature = pow(document, d)
        print("Document: ",str(document), "\nSignature:", str(signature))
        print("------------------------------")
        answer = pow(signature, e, n)
        print(str(answer), "=", str(signature) + "^" + str(e), "mod", n)
        print("The Document is VERIFIED\nDocument: ",document, "\nComputed Document (should match document): ", answer, "\nSignature: ", signature)
        print("------------------------------")
    
    if choice == 'N':
        # enter public info
        print("------------------------------")
        n = int(input("What is the value of public information 'n': "))
        e = int(input("enter an public key (encryption key): "))
        print("------------------------------")
        
        # enter document number
        print(n)
        document = int(input("Enter a document from 1 < x <= n: "))
        print("------------------------------")
        signature = int(input("Enter the proposed signature: "))

        # document = signature^e mod n
        answer = pow(signature, e, n)
        print(str(answer), "=", str(signature) + "^" + str(e), "mod", n)
        print("------------------------------")
        if int(answer) == int(document):
            print("The Document is VERIFIED\nDocument: ",document, "\nComputed Document (should match document): ", answer, "\nSignature: ", signature)
        else:
            print("The Document is UNVERIFIED\nDocument: ",document, "\nComputed Document (should match document): ", answer, "\nSignature: ", signature)
        print("------------------------------")

        

        
