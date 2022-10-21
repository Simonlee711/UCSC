#Quiz 1
# fix a program input/ output

name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
print(f"Hello {name}") # this should print the user's name
print("You are " + str(age) + " old.")

#Please write a code snippet that asks the user to enter two integer
#numbers, a dividend (numerator) and a non-zero divisor (denominator), and
#then prints their integer quotient along with the remainder. If you do not
#know what dividend, divisor, quotient, and remainder mean, maybe this
#formula will help you to understand them: dividend = divisor × quotient +
#remainder.
print("\n")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
quotient = num1 // num2
remainder = num1 % num2

print("Quotient:  " + str(quotient) + " Remainder:  " + str(remainder))





#Quiz 2
#fix a program see which number is greater
print("\n")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
     print ("The first number is greater than the second number:")
     print (f"{num1} > {num2}") 
else:
     print ("The second number is greater than the first number:")
     print (f"{num1} < {num2}")

#Write a program. This program asks the user to input an integer that
#corresponds to a triangle size and then generates a triangle of the given
#size at the top left corner of the terminal window. For example, if the input
#is 4 the program output looks like this:
#
#****
# ***
#  **
#   *
print("\n")

value = 0
userNum = int(input("Hello User! Enter a number : "))
value = userNum
for size in range(value):

    for star in range(value-size):
        print("*",end="  ")

    print()

#got 3/15 on this program. 





#Quiz 3
# fix a program: draw an isoceles triangle

print("\n")

# draw a isosceles triangle
def draw_triangle():
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (i*2 + 1))

done = False
while not done:
    height = int(input("Please enter the height of a triangle: "))
    draw_triangle()
    ans = input("Do you want to quit? [Y/N]: ").upper()
    if ans == "Y":
        done = True

#Write a program. This program prompts the user to enter a word and then
#counts how many letters and vowels in the word entered by the user. For
#example, if the user enters the word “hello” the output should look like this:
# hello 5 letters, 2 vowels
print("\n")

word = input("Please Enter a word : ")
vowels = 0
letters = 0
letlen = len(word)
for i in word:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
    or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1

print(f"{word} {letlen} letters, {vowels} vowels")




#Quiz 4
#Fix a program. This program should calculate the matrix addition (C = A + B,
#where each element of matrix C is equal to the sum of the elements of
#matrices A and B that have the same indexes cij = aij + bij ).

print("\n")
# program code starts here
m, n = 3, 3       # matrix dimensions
A = [ [1, 0, 0],
      [0, 1, 0],
      [0, 0, 1] ]
B = [ [2, 0, 0],
      [2, 0, 0],
      [2, 0, 0] ]

C = []

for i in range(m):
    C.append([])
    for j in range(n):
        C[i].append(A[i][j] + B[i][j])
    print (C[i])

#the code runs perfectly

#Write a program. Write a program that asks the user to enter some text,
#parses it into words, and creates a dictionary of words (vocabulary), where
#keys are unique words and their values are their occurrences (frequencies).
#Your code should print the dictionary at the end. For example, if the input
#text is the quote from the famous English poet Lord Byron:
print("\n")


wordbundle = input("Enter whatever you want: ")

wordlist = wordbundle.split()

solution = dict()
for line in wordlist:
     wordlist = line.split()
     for word in wordlist:
         if word not in solution:
               solution[word] = 1
         else:
               solution[word] += 1

print(solution)

#ran out of time 6/10 
