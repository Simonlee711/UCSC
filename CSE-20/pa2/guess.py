# assignment: programming assignment 2
# author: Simon Lee
# date: 10/29/2020
# file: guess.py is an interactive game that asks the user to guess a number from 1 to 10
# input: only integers from 1 to 10
# output: interactive messages

from random import randint

done = False
print (f"\nPlay a game: Guess My Number")


while not done :
    mynumber = randint(1,10)
    print (f"\nYou have three attempts to guess my number.")
    guess = int(input(f"\nPlease enter a number from 1 to 10: "))
    
    for i in range(2):
        if int(guess) > int(mynumber):    
            print(f"\nYou guessed wrong. Your number is bigger than mine.")
            guess = int(input("\nGuess again. Please enter a number: "))
            continue
            
        elif int(guess) < int(mynumber):
            print(f"\nYou guessed wrong. Your number is smaller than mine.")
            guess = int(input("\nGuess again. Please enter a number: "))
            continue
        else:
            break
    if guess > int(mynumber):
        print(f"\nYou guessed wrong. Your number is bigger than mine.")
        print(f"\nSorry you lost. My number is {mynumber}.")
    elif guess < int(mynumber):
        print(f"\nYou guessed wrong. Your number is smaller than mine.")
        print(f"\nSorry you lost. My number is {mynumber}.")
    else:
        print(f"\nYou guessed right. My number is {mynumber}. Congratulations you won!")
   
    
    replay = input("\nWould you like to play again [Y/N]? ").upper()
    if replay == "N":
        done = True
print("\nGoodbye!")
                    

                    

