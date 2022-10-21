'''
Substituion Cipher Program that also counts number of chracaters and its frequencies
'''
__author__ = 'Simon Lee in Math 134, siaulee@ucsc.edu'

# String of ASCII characters which are considered printable. 
# This is a combination of digits, ascii_letters, punctuation, and whitespace.
from string import printable  
from string import punctuation
from string import digits
import random

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

#generates randomly generated key everytime
def make_key_a():
    RAND_KEY = ''.join(sorted(printable, key=lambda _:random.random()))
    return RAND_KEY

def make_key_alpha():
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet = list(alphabet)
    random.shuffle(alphabet)
    return ''.join(alphabet)

# counts frequencies of letters again
def count_frequencies(text):
    all_freq = {}
    for i in text:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq

#encodes message by generating a random key with all printable characters in the main function
def encode_a(plaintext, key):
    return ''.join(key[printable.index(char)] for char in plaintext)

#decodes message by using same random key as encode_a function to revert message 
def decode_a(ciphertext, key):
    return ''.join(printable[key.index(char)] for char in ciphertext)

#encodes message by generating a random key with only upper case alphabet letters in the main function
def encode_alpha(plaintext, key):
    keyIndices = [alphabet.index(k) for k in plaintext]
    return ''.join(key[keyIndex] for keyIndex in keyIndices)

#decodes message by using same random key as encode_alpha function to revert message 
def decode_alpha(ciphertext, key):
    keyIndices = [key.index(k) for k in ciphertext]
    return ''.join(alphabet[keyIndex] for keyIndex in keyIndices)

# main program
if __name__ == "__main__":
    done = False
    iterations = 1
    while not done:
        print("Would you like to encode & decode, or count the frequencies of letters in the message?")
        choice = input("Type S to encode & decode, C to count character frequencies or Q to quit: ").upper()
        
        # OPTION 1
        # you want to encrypt and decrypt something option
        if choice == 'S':
            message = input("Enter a message: ")
            choice2 = input("would you like a key of: \nA - alphabet letters or \nP - all printable characters: ").upper()
            
            # OPTION 1a: you want to encrypt & decrypt a message containing only alphabet letters.
            # A far more secure subtitution cipher which can subsitute any character with any printable value in Python
            if choice2 == 'P':
                iterations = int(input("How many different times would you like to encrypt and decrypt messages? "))
                for i in range(0, iterations):
                    RAND_KEY = make_key_a()
                    encoded = encode_a(message, RAND_KEY)
                    decoded = decode_a(encoded, RAND_KEY)
                    print("\n----- iteration "+ str(i + 1) + " -----\n")
                    print("The original message is: " + message + "\n")
                    print("Encryption key: " + RAND_KEY + "\n")
                    print("CipherText: " + encoded + "\n")
                    print("Decrypted PlainText: "+ decoded + "\n")
                continue
            
            # OPTION 1b: you want to encrypt & decrypt a message containing only alphabet letters. Similar to example in class
            # However instead of 26! since I include both lower case and upper case, there are 52! of encoding a message
            if choice2 == 'A':
                if any(p in message for p in punctuation):
                    print("Message has punctuation and does not work with this alphabet substituion cipher")
                    done = True
                    continue
                if any(d in message for d in digits):
                    print("Message has digits and does not work with this alphabet substituion cipher")
                    done = True
                    continue
                iterations = int(input("How many different times would you like to encrypt and decrypt messages? "))
                for i in range(0, iterations):    
                    RAND_KEY = make_key_alpha()
                    encoded = encode_alpha(message, RAND_KEY)
                    decoded = decode_alpha(encoded, RAND_KEY)
                    print("\n----- iteration "+ str(i + 1) + " -----")
                    print("The original message is: " + message + "\n")
                    print("Encryption key: " + RAND_KEY + "\n")
                    print("CipherText: " + encoded + "\n")
                    print("Decrypted Plaintext: "+ decoded + "\n")
                continue
            
            # OPTION 1c: wrong command line option (error edge case)
            else:
                print("Invalid choice!")
                done = True
            continue
        
        # OPTION 2: Counting frequencies of each character that occurs in the message
        if choice == 'C':
            message = input("Enter Message to count frequencies: ")
            counter = count_frequencies(message)
            print(counter)
            continue
        
        # OPTION 3: Terminate Program option
        if choice == 'Q':
            done = True
        
        # OPTION 4: wrong command line option (error edge case)
        else:
            print("Invalid choice")
            done = True