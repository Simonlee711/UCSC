'''
Caesar Cipher Program that also counts number of chracaters and its frequencies
'''
__author__ = 'Simon Lee in Math 134, siaulee@ucsc.edu'

def count_frequencies(text):
    all_freq = {}
    for i in text:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq

# make a list (tuple) of letters in the English alphabet

def make_alphabet():
   alphabet = ()
   for i in range(26):
       char = i + 65
       alphabet += (chr(char),)
   return alphabet

# encode text letter by letter using a Caesar cipher
# return a list of encoded symbols

def encode(plaintext, shift):
   plaintext = plaintext.upper()
   ciphertext = []
   alphabet = make_alphabet()
   length = len(alphabet)
   for char in plaintext:
       found = False
       for i in range(length):
           if char == alphabet[i]:
               letter = alphabet[(i + int(shift)) % length]
               ciphertext.append(letter)
               found = True
               break
       if not found:
           ciphertext.append(char)
   return ciphertext


# decode text letter by letter using a Caesar cipher
# return a list of decoded symbols

def decode(ciphertext,shift):
   ciphertext = ciphertext.upper()
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
if __name__ == "__main__":
    done = False
    while not done:
        print("\nWould you like to encode, decode, or count the frequencies of letters in the message?")
        choice = input("Type E to encode, D to decode, C to count character frequencies or Q to quit: ").upper()
        
        if choice == 'E':
            message = input("Enter Message to Encode: ")
            shift = 1
            plaintext = message
            print("\nPlaintext: \n" + plaintext)
            for i in range(1,26):
                ciphertext = encode(plaintext, shift)
                hidden_message = to_string(ciphertext)
                print("\nCiphertext: " + str(i) + "\n" + str(hidden_message))
                shift += 1
            done = True

        elif choice == 'D':
            message = input("Enter Message to Decode: ")
            shift = 1
            ciphertext = message
            print("\nCiphertext: \n" + ciphertext)
            for i in range(1,26):
                plaintext = decode(ciphertext, shift)
                hidden_message = to_string(plaintext)
                print("\nPlaintext: " + str(i) +"\n" + str(hidden_message))
                shift += 1
            done = True

        elif choice == 'C':
            message = input("Enter Message to count frequencies: ")
            counter = count_frequencies(message)
            print(counter)
            continue
       
        elif choice == 'Q':
            done = True
        else:
            print("That is not a valid option\n")
            break