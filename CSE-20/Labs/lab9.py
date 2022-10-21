#Lab 9
# 1)Write a code snippet of a function get_data () that asks the user to enter a
#float number and catches a ValueError exception. It should print “It is not a
#float number!” if the user enters a value in a wrong format such as a
#string of symbols or letters. If the user enters a value in the right format,
#the function prints “You entered n.”, where n is a number entered by the user.

def get_data():

  try:

      num = float(input ("Enter an number: "))

      print(f"You entered {num}.")

  except ValueError:

      print("It is not a float number!")

# 2)Modify your function get_data() that allows the user to enter a value
# multiple times until a value is in the right format and can be accepted.
# Assume the same specifications as your previous function.

def get_data():
   try:
        num = float(input("Enter an number: "))
        print(f"You entered {num}.")
   except ValueError:
        print("It is not a float number!")
        get_data()




