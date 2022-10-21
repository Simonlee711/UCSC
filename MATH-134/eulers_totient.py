'''
- Performs the Euler's Totient Function [φ(n)] to see if a number is prime
- also contains a function that generates a nth amount of prime numbers
''' 

__author__ = 'Simon Lee in Math 134, siaulee@ucsc.edu'

from typing import Counter


def primes(n):                                                                      
  """ Yields an finite sequence of prime numbers. """                                             
  num = 2  # start at first prime number
  verbose = False
  counter = 0
  done = True                                                            
  while done:  # infinite loop
    if counter == n:
        done = False                                                                      
    is_prime = φ(num, verbose)
    if is_prime == True:
        counter += 1
        print(str(num) + " ")
        num += 1
        continue
    else:
        num += 1
        continue
  

def gcd(a, b):
    """ Function to return the gcd of two integers a and b """
    if (a == 0):
        return b
    return gcd(b % a, a)
 

def φ(n, verbose):
    """ A simple function to evaluate Euler Totient Function """
    result = 0
    prime = False
    if verbose:
        print("φ(" + str(n) + ")")
    for i in range(1, n):
        if verbose:
            print("gcd("+str(i)+","+str(n)+") = " + str(gcd(i, n)))
        if (gcd(i, n) == 1):
            result+=1
    if result == (n-1):
        prime = True
    return prime
 

if __name__ == "__main__":
    """ Main Module - Follow the instructions from the user input messages """
    verbose = False
    done = True
    choice = input("Would you like to computer Euler's Totient Function (E) or generate an finite sequence of primes (P): ").upper()
    number = int(input("Enter the number that you wish to compute (Euler Totient Function) or iterate through\
 (Infinite sequence of primes): "))
    while done:
        if choice == 'E':
            verbose_p = input("Would you like verbose printing (Y or N): ").upper()
            if verbose_p == 'Y':
                verbose = True 
                is_prime = φ(number, verbose)
                if is_prime == True:
                    print("This number " + str(number) + " is prime")
                else:
                    print("This number " + str(number) + " is not prime")
                done = False
                continue
            if verbose_p == 'N':
                is_prime = φ(number, verbose)
                if is_prime == True:
                    print("This number " + str(number) + " is prime")
                else:
                    print("This number " + str(number) + " is not prime")
                done = False
                continue
            else:
                print("Invalid Choice")
        if choice == 'P':
            primes(number)
            done = False
            continue
        else:
            print("Invalid option")
            continue