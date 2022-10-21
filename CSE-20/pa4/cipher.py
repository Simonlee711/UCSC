# assignment: programming assignment 4
# author: Simon Lee
# date: November 29, 2020
# file: cipher.py is a program that (put the description of the program)
# input: Enter a file in either plaintext or ciphertext and be able to encode or decode a specific message from the file.
# output: Encoding or Decoding messages from files.

# read text from a file and return text as a string

def readfile():
   code_to_read = input("\nPlease enter a file for reading: ")
   try:
      file1 = open(code_to_read, "r")
      lines = file1.readlines()
      message = to_string(lines)
   except IOError:
      print("\nFile cannot be opened")
      readfile()
      
   else:
      file1.close()
      
   return message

# write a string (message) to a file

def writefile(code_to_print):
   try:
      file1 = open(code_to_print, "w")
      lines = file1.writelines(hidden_message)
      final_message = to_string(lines)
      
   except IOError:
      print("File cannot be opened")
      writefile(code_to_print)
   except TypeError:
      final_message = hidden_message
   else:
      file1.close()

   return final_message
  
      


# make a list (tuple) of letters in the English alphabet

def make_alphabet():
   alphabet = ()
   for i in range(26):
       char = i + 65
       alphabet += (chr(char),)
   #print (alphabet)
   return alphabet

# encode text letter by letter using a Caesar cipher
# return a list of encoded symbols

def encode(plaintext):
   plaintext = plaintext.upper()
   shift = 3
   ciphertext = []
   alphabet = make_alphabet()
   length = len(alphabet)
   for char in plaintext:
       found = False
       for i in range(length):
           if char == alphabet[i]:
               letter = alphabet[(i + shift) % length]
               ciphertext.append(letter)
               found = True
               break
       if not found:
           ciphertext.append(char)
   return ciphertext


# decode text letter by letter using a Caesar cipher
# return a list of decoded symbols
# check how the function encode() is implemented
# your implementation of the function decode() can be very similar
# to the implementation of the function encode()

def decode(ciphertext):
   ciphertext = ciphertext.upper()
   shift = -3
   plaintext = []
   alphabet = make_alphabet()
   length = len(alphabet)
   for char in ciphertext:
       found = False
       for i in range(length):
           if char == alphabet[i]:
               letter = alphabet[(i + shift) % length]
               plaintext.append(letter)
               found = True
               break
       if not found:
           plaintext.append(char)
   return plaintext
   

# converts a list into a string
# for example, the list ["A", "B", "C"] to the string "ABC" or
# the list ["H", "O", "W", " ", "A", "R", "E", " ", "Y", "O", "U", "?"] to the string "HOW ARE YOU?"

def to_string(lines):
   s = ""
   for char in lines:
      s += char
   return s



# main program
done = False
while not done:
   print("\nWould you like to encode or decode the message?\n")
   choice = input("Type E to encode, D to decode, or Q to quit: ").upper()
   

   if choice == 'E':
      message = readfile()
      plaintext = message
      ciphertext = encode(plaintext)
      hidden_message = to_string(ciphertext)
      code_to_print = input("\nPlease enter a file for writing: ")
      final_message = writefile(code_to_print)
      print("\nPlaintext: \n" + plaintext)
      print("\nCiphertext: \n" + str(final_message))
      continue

   elif choice == 'D':
      message = readfile()
      ciphertext = message
      plaintext = decode(ciphertext)
      hidden_message = to_string(plaintext)
      code_to_print = input("\nPlease enter a file for writing: ")
      final_message = writefile(code_to_print)
      print("\nCiphertext: \n" + ciphertext)
      print("\nPlaintext: \n" + str(final_message))
      continue

   elif choice == 'Q':
      done = True
      
   else:
      continue

print("\nGoodbye!")

   
