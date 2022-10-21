'''
Performs the Euclidean Algorithm which will help you find the gcd(x,y) of two integers x and y

Also contains a verbose option of how it got the arithmetic
'''
__author__ = 'Simon Lee in Math 134, siaulee@ucsc.edu'

# imports the floor division arithmetic from the math library
from math import * 

def euclid_algorithm(x, y, verbose):
    if x < y:
        return euclid_algorithm(y, x, verbose)
    while y != 0:
        if verbose:
            print(str(x) + " = " + str(floor(x/y)) + " * " + str(y) + " + " + str(x % y))
            (x,y) = (y, x % y)
        else:
            (x,y) = (y, x % y)
    print("gcd is " + str(x))
    return x

def extended_gcd(a, b, verbose):
    '''
    returns (g, x, y) where g is the GCD of a and b are the values that go into the following equation from class:
    
    Linear Combination equation:    
            a*x + b*y = gcd

    Below details the proof which we worked out in class which helps us build the equation
    '''

    # a = 1 * a + 0 * b
    (r1, x1, y1) = (a, 1, 0)
    # b = 0 * a + 1 * b
    (r2, x2, y2) = (b, 0, 1)

    while r2 != 0:
        # dividing r1 by r2 to get r3:
        # r1 = q3 * r2 + r3
        q3 = r1 // r2
        r3 = r1 % r2

        # r3 = r1 - q3*r2
        #    = x1 * a + y1 * b - q3 * (x2 * a + y2 * b)
        #    = (x1 - q3 * x2) * a + (y1 - q3 * y2) * b
        x3 = (x1 - q3*x2)
        y3 = (y1 - q3*y2)

        # next step r1 will be our current r2
        # and r2 will be our current r3
        (r1, x1, y1) = (r2, x2, y2)
        (r2, x2, y2) = (r3, x3, y3)
        if verbose:
            print( str(x1) +"("+ str(a) + ") + " + str(y1) + "(" + str(b) + ") = " + str(r1))
    
    print("Linear combination:")
    print( str(x1) +"("+ str(a) + ") + " + str(y1) + "(" + str(b) + ") = " + str(r1))
    return (r1, x1, y1)

if __name__ == "__main__":
    verbose = False
    done = True
    while done:
        x = int(input("Enter the first number in whcih you want to perform the Euclidean Algorithm: "))
        y = int(input("Enter the second number in whcih you want to perform the Euclidean Algorithm: "))
        choice = input("Would you like to find the gcd (Euclidean Algorithm) or the linear combination of the gcd (E or L)").upper()
        if choice == 'E':
            verbose_option = input("Would you like verbose printing (Y or N)").upper()
            if verbose_option == 'Y':
                verbose = True
                euclid_algorithm(x,y,verbose_option)
                done = False
                continue
            if verbose_option == 'N':
                euclid_algorithm(x,y,verbose)
                done = False
                continue
            else:
                print("Invalid option")
                continue
        if choice == 'L':
            verbose_option = input("Would you like verbose printing (Y or N)").upper()
            if verbose_option == 'Y':
                verbose = True
                extended_gcd(x,y,verbose_option)
                done = False
                continue
            if verbose_option == 'N':
                extended_gcd(x,y,verbose)
                done = False
                continue
            else:
                print("Invalid option")
                continue
        else:
            print("Invalid choice")
            continue