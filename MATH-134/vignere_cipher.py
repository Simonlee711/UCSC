'''
 Implementation of Vigenère Cipher in Python
'''
__author__ = 'Simon Lee in Math 134, siaulee@ucsc.edu'
 

def genKey(message, key):
    '''
    generates key so it keeps repeating itself based on the length of the message
    '''
    key = list(key)
    if len(message) == len(key):
        return(key)
    else:
        for i in range(len(message) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
     

def encrypt(message, key):
    '''
    encryption function using keyword to shift
    '''
    cipher_text = []
    for i in range(len(message)):
        if i == 0x20:
            x = ord(0x20)
            cipher_text.append(x)
            continue
        x = (ord(message[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))
     
def decrypt(cipher_text, key):
    '''
    decryption function using keyword to find original message
    '''
    orig_text = []
    for i in range(len(cipher_text)):
        if i == 0x20:
            x = ord(0x20)
            orig_text.append(x)
            continue
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))
     

if __name__ == "__main__":
    '''
    Main module that runs the code
    '''
    message = input("message: ").upper()
    keyword = input("keyword: ").upper()
    key = genKey(message, keyword)
    cipher_text = encrypt(message,key)
    plain_text = decrypt(cipher_text, key)
    print("------------------------------")
    print(message)
    print(keyword)
    print("------------------------------")
    print("Ciphertext :", cipher_text)
    print("Plaintext :", plain_text)