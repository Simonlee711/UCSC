#!/usr/bin/env python3 
# Name: Simon Lee
# Group Members: Campbell Strand, Mateo Etcheveste, Jonathan Zau

'''
A converter program that matches amino acids or codons using python dictionaries 
'''
short_AA = {
            'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
            'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
            'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
            'ALA': 'A', 'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'
            }

long_AA = {value:key for key,value in short_AA.items()}

rnaCodonTable = {
# Second Base
# U             C             A             G
#U
'UUU': 'Phe', 'UCU': 'Ser', 'UAU': 'Tyr', 'UGU': 'Cys',
'UUC': 'Phe', 'UCC': 'Ser', 'UAC': 'Tyr', 'UGC': 'Cys',
'UUA': 'Leu', 'UCA': 'Ser', 'UAA': '---', 'UGA': '---',
'UUG': 'Leu', 'UCG': 'Ser', 'UAG': '---', 'UGG': 'Trp',
#C 
'CUU': 'Leu', 'CCU': 'Pro', 'CAU': 'His', 'CGU': 'Arg',
'CUC': 'Leu', 'CCC': 'Pro', 'CAC': 'His', 'CGC': 'Arg',
'CUA': 'Leu', 'CCA': 'Pro', 'CAA': 'Gln', 'CGA': 'Arg',
'CUG': 'Leu', 'CCG': 'Pro', 'CAG': 'Gln', 'CGG': 'Arg',
#A
'AUU': 'Ile', 'ACU': 'Thr', 'AAU': 'Asn', 'AGU': 'Ser',
'AUC': 'Ile', 'ACC': 'Thr', 'AAC': 'Asn', 'AGC': 'Ser',
'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg',
'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg',
#G
'GUU': 'Val', 'GCU': 'Ala', 'GAU': 'Asp', 'GGU': 'Gly',
'GUC': 'Val', 'GCC': 'Ala', 'GAC': 'Asp', 'GGC': 'Gly',
'GUA': 'Val', 'GCA': 'Ala', 'GAA': 'Glu', 'GGA': 'Gly',
'GUG': 'Val', 'GCG': 'Ala', 'GAG': 'Glu', 'GGG': 'Gly'
}
dnaCodonTable = {key.replace('U','T'):value for key, value in rnaCodonTable.items()}

def search(string):
    # simple conditionals that check through all dicitionaries
    if string in short_AA:        
        print (string +" = " + short_AA[string])
    elif string in long_AA:         
        print (string +" = " + long_AA[string])
    elif string in rnaCodonTable:  
        print (string +" = " + rnaCodonTable[string].upper())
    elif string in dnaCodonTable:     
        print (string +" = " + dnaCodonTable[string].upper())
    else:
        # if input doesn't comply with any dictionary keys it will print out default message
        print('unknown')      

def main():
    ''' main driver of code'''
    # takes in user input
    Aminos = input("Enter a codon or Amino Acid: ")
    search(Aminos)

main()
