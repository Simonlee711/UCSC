#!/usr/bin/env python3 
# Name: Simon Lee (siaulee)
# Group Members: Campbell Strand, Mateo Etcheveste, Jonathan Zau

'''
A module that performs a lot of counts for DNA, codons, and Amino acids
'''

class NucParams:
    '''
    The NucParams class constructs a multitude of counts using dictionaries
    '''
    rnaCodonTable = {
    # RNA codon table
    # U
    'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C',  # UxU
    'UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C',  # UxC
    'UUA': 'L', 'UCA': 'S', 'UAA': '-', 'UGA': '-',  # UxA
    'UUG': 'L', 'UCG': 'S', 'UAG': '-', 'UGG': 'W',  # UxG
    # C
    'CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R',  # CxU
    'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',  # CxC
    'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',  # CxA
    'CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',  # CxG
    # A
    'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S',  # AxU
    'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',  # AxC
    'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',  # AxA
    'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',  # AxG
    # G
    'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G',  # GxU
    'GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',  # GxC
    'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',  # GxA
    'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'  # GxG
    }
    dnaCodonTable = {key.replace('U','T'):value for key, value in rnaCodonTable.items()}

    def __init__ (self, inString=''):
        '''
        Constructor Method for NucParams program. Constructs all ionaries taking optional user input
        '''
        # nucleotide bases Dictionary
        self.validNuc = ['A','C','G','T','U','N']
        self.nucComp = {nucleo: 0 for nucleo in self.validNuc}
        
        # builds a Dictionary for amino acids
        self.aaComp = {amino: 0 for amino in NucParams.rnaCodonTable.values()}
        
        # builds a Dictionary for codons
        self.codonComp = {codon: 0 for codon in NucParams.rnaCodonTable.keys()}
        
        self.addSequence(inString)
        
        
    def addSequence (self, inSeq):
        '''
        Method that does all the intangibles of the code
        '''
        
        # cleans up sequence
        temp = ''.join(inSeq.upper()).split()
        usr = ''.join(temp)
        seq = ''
        
        # gets rid of invalid characters (non - ACTGUN) and counts nucleotide bases
        for nucleo in usr:
            if nucleo in self.nucComp.keys():
                seq += str(nucleo)
                self.nucComp[nucleo] += 1
        
        # transcribes DNA to RNA
        seq = seq.replace("T", "U")
        
        # constructs codon list within a sequence 
        codonsList = []
        for i in range(0, len(seq), 3):
            codonsList.append(seq[i:i+3])
        
        # translation from codon to amino acid
        for codon in codonsList:
            if codon in NucParams.rnaCodonTable.keys():
                self.aaComp[NucParams.rnaCodonTable[codon]] += 1
                self.codonComp[codon] += 1
            
    def aaComposition(self):
        '''
        returns a Dictionary of the amino acid counts
        '''
        return self.aaComp
    def nucComposition(self):
        '''
        returns a Dictionary of counts of valid nucleotides found in the analysis. (ACGTNU}
        '''
        return self.nucComp
    def codonComposition(self):
        '''
        returns a Dictionary that counts codons.
        '''
        return self.codonComp
    def nucCount(self):
        '''
        returns an integer value, summing every valid nucleotide {ACGTUN} 
        '''
        return sum(self.nucComp.values())

import sys
class FastAreader :
    ''' 
    Define objects to read FastA files.
    
    instantiation: 
    thisReader = FastAreader ('testTiny.fa')
    usage:
    for head, seq in thisReader.readFasta():
        print (head,seq)
    '''
    def __init__ (self, fname=''):
        '''contructor: saves attribute fname '''
        self.fname = fname
            
    def doOpen (self):
        ''' Handle file opens, allowing STDIN.'''
        if self.fname is '':
            return sys.stdin
        else:
            return open(self.fname)
        
    def readFasta (self):
        ''' Read an entire FastA record and return the sequence header/sequence'''
        header = ''
        sequence = ''
        
        with self.doOpen() as fileH:
            
            header = ''
            sequence = ''
            
            # skip to first fasta header
            line = fileH.readline()
            while not line.startswith('>') :
                line = fileH.readline()
            header = line[1:].rstrip()

            for line in fileH:
                if line.startswith ('>'):
                    yield header,sequence
                    header = line[1:].rstrip()
                    sequence = ''
                else :
                    sequence += ''.join(line.rstrip().split()).upper()

        yield header,sequence

