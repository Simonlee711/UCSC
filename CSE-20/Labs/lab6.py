#Lab 6
#Regular Expressions
# Write your own code. Make a regular expression pattern that can be used to
# find all email addresses: username@server.domain, where username, server,
# and domain are strings made of any letters, numbers and underscores. 

import re

p_lower = re.compile( r'[a-z]') 

p_upper = re.compile( r'[A-Z]')

p_digit = re.compile( r'[0-9]')

p_underscore = re.compile(r'[_,@]')

randEmail=str(input("Enter any email formatted like this; username@server.domain :")

m_lower = p_lower.search (randEmail)

m_upper = p_upper.search (randEmail)

m_digit = p_digit.search(randEmail)

m_underscore = p_underscore.search(randEmail)

if m_lower and m_upper and m_digit and m_underscore:

     print(" Your email has an upper, lower, digit, and underscore")

#has an error of not checking the @ symbol. Recieved 3/4 credit on this one

# 2)Write a code snippet that asks the user to enter an email address
# (use input()) and verify if it is a valid email address according to the
# regular expression pattern that you designed in the previous problem.

import re

p_lower = re.compile( r'[a-z]') 

p_upper = re.compile( r'[A-Z]')

p_digit = re.compile( r'[0-9]')

p_underscore = re.compile(r'[_]')

randEmail=str(input("Enter any email formatted like this; username@server.domain :")

m_lower = p_lower.search (randEmail)

m_upper = p_upper.search (randEmail)

m_digit = p_digit.search(randEmail)

m_underscore = p_underscore.search(randEmail)

if m_lower and m_upper and m_digit and m_underscore:

                  print("The email is valid.")

else:

                  print("The email is invalid.")

 

