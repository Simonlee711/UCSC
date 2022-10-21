# assignment: programming assignment 3
# author: Simon Lee
# date: November 15, 2020
# file: calculator.py is a program that calculates two float numbers using any of the four operators: +, -, *, /
# input: any float number
# output: interactive messages
def format(num1, precision = 2):
    num1 = round(num1,2)
    partint = int(num1)
    partdec = num1 - partint
    if partdec == 0:
        return str(partint)
    else:
        return str(num1)

def format(num2, precision = 2):
    num2 = round(num2,2)
    partint = int(num2)
    partdec = num2 - partint
    if partdec == 0:
        return str(partint)
    else:
        return str(num2)
def add (num1, num2):
    sum1 = (num1) + (num2)
    print(format(num1) + " + " + format(num2) + " = " + format(sum1))
def subtract (num1, num2):
    dif1 = (num1) - (num2)
    print(format(num1) + " - " + format(num2) + " = " + format(dif1))
def multiply (num1, num2):
    prod1 = (num1) * (num2)
    print(format(num1) + " x " + format(num2) + " = " + format(prod1))
def divide (num1, num2):
    if num2 == 0:
        print("The division by zero is prohibited!")
    else:
        quo1 = (num1) / (num2)
        print(format(num1) + " / " + format(num2) + " = " + format(quo1))     
def isfloat (token):
    dot = False
    minus = False
    for char in token :
        if char.isdigit() :
            continue
        elif char == "." :
            if not dot:
                dot = True
            else :
                return False
        elif char == "-" and token[0] == "-":
            if not minus:
                minus = True
            else :
                return False
        else:
            return False
    return True
        


#main program
print("Welcome to Calculator Program!")
done = False
while not done:
    choose = input("Please choose one of the following operations:\nAddition - A\
\nSubtraction - S\nMultiplication - M\nDivision - D\n>").upper()
    print()
    
    if choose == "A":
        print("You chose addition.")

    elif choose == "S":
        print("You chose subtraction.")

    elif choose == "M":
        print("You chose multiplication.")

    elif choose == "D":
        print("You chose division.")
        
    else:
        print("You did not choose correctly.")
        continue
    
    while True:
        num1 = input("Please enter the first number: ")
        print()
        if isfloat(num1):
            num1 = float(num1)
            print(f"The first number is " + format(num1) + ".")
            break
        else:
            print("You did not choose a number.")
            continue
    while True:
        num2 = input("Please enter the second number: ")
        print()
        if isfloat(num2):
            num2 = float(num2)
            print("The second number is " + format(num2) + ".")
            break
        else:
            print("You did not choose a number")
            continue

    if choose == "A":
        add(num1, num2)

    elif choose == "S":
        subtract(num1, num2)

    elif choose == "M":
        multiply(num1, num2)

    elif choose == "D":
        divide(num1, num2)



    replay = input("Do you want to continue? [Y/N]: ").upper()
    print()
    
    if replay == "N":
        done = True
print("Goodbye!")
