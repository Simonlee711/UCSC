#!/usr/bin/env python3 
# Name: Simon Lee (siaulee)
# Group Members: Campbell Strand, Mateo Etcheveste, Jonathan Zau

'''
Read a DNA string from user input and return a collapsed substring of embedded Ns to: {count}.

Example: 
 input: AaNNNNNNGTC
output: AA{6}GTC

Any lower case letters are converted to uppercase
'''

class DNAstring (str):
    def length (self):
        ''' returns length of string'''
        return (length(self))
    
    def purify(self):
        ''' Return an upcased version of the string, collapsing a single run of Ns.'''
        N_count = self.count('N') # counts the number of N's
        purifiedSequence = self.replace("N"*N_count, "{"+str(N_count)+"}")
        return purifiedSequence.upper()
    
def main():
    ''' Get user DNA data and clean it up.'''
    data = input('DNA data?')
    thisDNA = DNAstring (data)
    pureData = thisDNA.purify()
    print (pureData)
    
main()
