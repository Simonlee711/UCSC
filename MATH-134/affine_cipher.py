"""
Module that will demonstrate the affine cipher shift
"""

__author__ = 'Simon Lee in Math 134, siaulee@ucsc.edu'

def egcd(a, b):
    '''
    Extended Euclidean algorithm
    '''
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
 
def modinv(a, m):
    '''
    Modular inverse calculator 
    '''
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
 
 
def affine_encrypt(text, key):
    '''
    computes the encryption using the key
    C = (a*P + b) % 26
    '''
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)
                  + ord('A')) for t in text.upper().replace(' ', '') ])
 
 
def affine_decrypt(cipher, key):
    '''
    computes the decryption using the key
    P = (a^-1 * (C - b)) % 26
    '''
    return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))
                    % 26) + ord('A')) for c in cipher ])
 
 

if __name__ == '__main__':
    '''
    input message and key and the cipher and plain text will be generated
    '''
    text = input("Message: ").upper()
    num1 = int(input("key val 1: "))
    num2 = int(input("key val 2: "))
    key = [num1, num2]
 
    # calling encryption and decryption function
    encrypted_message = affine_encrypt(text, key)
    decrypted_message = affine_decrypt(encrypted_message, key)

    #print message
    print("------------------------------") 
    print("Original message (in uppercase)" + text)
    print("Shift (" + str(num1) + "," + str(num2) + ")")
    print("------------------------------")
    print('Encrypted Text: {}'.format( encrypted_message ))
    print('Decrypted Text: {}'.format( decrypted_message ))
 