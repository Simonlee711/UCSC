#Lab 4

# 1) Write your own code snippet that iterates through all characters in the
# sentence "Python is cool!" (they can be printed on one line or several lines).
# Use a for loop statement.

for char in ("Python is cool!"):

   print(char, end = "  ")

print("\n")

# 2)Write your own code snippet that iterates through the sequence of
# numbers from 1 to 10 and prints them with one number on EACH line. You
# should use a for loop statement and a range function.

start, stop, step = 1, 11, 1

for x in range(start, stop, step):                                   

                 print(x, end = " \n ")

print("\n")
# 3)Write your own code snippet that iterates through the sequence of
# numbers from 1 to 10 and prints them with one number on EACH line. You
# should use a while loop statement!

a = 1

while a < 11:

   print(a, end = "\n")

   a += 1

