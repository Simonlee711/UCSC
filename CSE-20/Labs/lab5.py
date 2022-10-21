#Lab 5

# 1)Write a code snippet that asks the user to enter a word
# (“Please, enter a word: ”) and prints the word backwards.


randomWord = str(input("Please, enter a word: "))
backwardsWord = randomWord[::-1]
print(backwardsWord)


# 2)A palindrome is a word, phrase, or sequence that reads the same backward as
#forward. Write a code snippet that asks the user to enter a palindrome (“Please,
# enter a palindrome: ”) and verifies if the word x entered by the user is a palindrome
# (“The word x is a palindrome.” or “The word x is not a palindrome.”; x should be
# substituted to its value).


x = str(input("Please, enter a palindrome: "))
backwards = (x[::-1])
if backwards == x:
       print(f"The word {x} is a palindrome.")
else:
       print(f"The word {x} is not a palindrome.")


