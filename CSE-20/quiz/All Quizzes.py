#Quizzes Programs:
# 1)This program has four errors, can you find and fix them all? Rewrite the
# code without errors. Please use the preformatted option instead of the
# default paragraph option for the code.

name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
print(f"Hello {name}") 
print("You are " + str(age) + " old.")

#2)Please write a code snippet that asks the user to enter two integer
#numbers, a dividend (numerator) and a non-zero divisor (denominator), and
#then prints their integer quotient along with the remainder. If you do not
#know what dividend, divisor, quotient, and remainder mean, maybe this
#formula will help you to understand them: dividend = divisor × quotient +
#reaminder.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
quotient = num1 // num2
remainder = num1 % num2

print("Quotient:  " + str(quotient) + "Remainder:  " + str(remainder))

#3)Fixing the program of a preformatted block of code. The program is
# to see which number is larger between two integers.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
     print ("The first number is greater than the second number:")
     print (f"{num1} > {num2}") 
else:
     print ("The second number is greater than the first number:")
     print (f"{num1} < {num2}")

#4)Write a program. This program asks the user to input an integer that
#corresponds to a triangle size and then generates a triangle of the given
#size at the top left corner of the terminal window. For example, if the input
#is 4 the program output looks like this:


value = 0
userNum = int(input("Hello User! Enter a number : "))
value = userNum
for size in range(value):

    for star in range(value-size):
        print("*",end="")

    print()

# recieved 3/15 on this code ^ bc did not follow all directions

#5)The code should have a function called draw_triangle that has only one
#parameter of the integer data type. The function should work with the main
#program written below and draw a triangle depending on the user's input
#that is used as the function argument.

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

#6)Write a program. This program prompts the user to enter a word and then
#counts how many letters and vowels in the word entered by the user. For
#example, if the user enters the word “hello” the output should look like this:
# hello 5 letters, 2 vowels

word = input("Please Enter a word : ")
vowels = 0
letters = 0
letlen = len(word)

for i in word:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
    or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
    vowels = vowels + 1

print(f"{word} {letlen} letters, {vowels} vowels")

#7)Fix a program. This program should calculate the matrix addition (C = A + B,
#where each element of matrix C is equal to the sum of the elements of
#matrices A and B that have the same indexes cij = aij + bij ).
#However it is incomplete: index values of nested lists A, B, and C and two
#list statements are missing. Can you find them and fix the program? 
#The fixed program output should be:
#[3, 0, 0]
#[2, 1, 0]
#[2, 0, 1]

# program code starts here
m, n = 3, 3       
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

#8)Write a program. Write a program that asks the user to enter some text,
#parses it into words, and creates a dictionary of words (vocabulary), where
#keys are unique words and their values are their occurrences (frequencies).
#Your code should print the dictionary at the end. 

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




