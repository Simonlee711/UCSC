#!/usr/bin/env python3 
# Name: Simon Lee 
# Group Members: Campbell Strand, Mateo Etcheveste, Jonathan Zau

'''
Program docstring goes here.
'''

class FastqString (str):
    ''' a class system that breaks down a sequence of text from a FASTQ file format'''
    def parse(self):
        ''' parses out each field of the run information from the string and returns a list with each of them.'''
        shortened_seq = self.replace("@","") # removes @ sign as it is useless to our sequence info
        parsed = shortened_seq.split(":") # makes a new element in a list at every :
        return parsed
        
def main():
    ''' driver of the code.'''
    
    # takes in input similar to seqCleaner
    data = input('FASTQ data?')
    thisFASTQ = FastqString (data)
    parsedData = thisFASTQ.parse()
    
    # list for the following for loop
    Word_print = ["Instrument =", "Run ID =", "Flow Cell ID =", "Flow Cell Lane =", "Tile Number =", "X-coord =", "Y-coord =" ]
    
    # ran two lists so we wouldn't have to write repetitive print statements. I'm kinda proud of this implementation ;)
    for i in range (0,7):
        print (Word_print[i], parsedData[i])
        
main()
