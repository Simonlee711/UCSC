# assignment: programming assignment 1
# author: Simon Lee
# date: October 13,2020
# file: hello.py is a program that asks the user to enter user’s name,
#       age, and favorite movie and outputs a greeting message that
#       include the information about the user
# input: string data
# output: string data

x = "Nice "
y = "to meet you, "
z = x + y


username = str(input("Hello! What is your name? "))
age = int(input("\nWhat is your age? "))
favorite_movie = str(input("\nWhat is your favorite movie? "))

print("\n" + z + username + ".")
print(f"You are {age} years old and your favorite movie is {favorite_movie}.")
