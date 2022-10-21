#!/usr/bin/env python3 
# Name: Simon Lee (siaulee)
# Group Members: Campbell Strand, Mateo Etcheveste, Jonathan Zau

'''
A module that performs a lot of counts for DNA, codons, and Amino acids
'''

import numpy as np

class ProteinParam :
    '''
    This class has various methods that calculate a wide range of statistics.
    
    In addition we utilize some fixed values in the form of a dictionary to assist in computation
    '''
# These tables are for calculating:
#     molecular weight (aa2mw), along with the mol. weight of H2O (mwH2O)
#     absorbance at 280 nm (aa2abs280)
#     pKa of positively charged Amino Acids (aa2chargePos)
#     pKa of negatively charged Amino acids (aa2chargeNeg)
#     and the constants aaNterm and aaCterm for pKa of the respective termini
#  Feel free to move these to appropriate methods as you like

# As written, these are accessed as class attributes, for example:
# ProteinParam.aa2mw['A'] or ProteinParam.mwH2O

    aa2mw = {
        'A': 89.093,  'G': 75.067,  'M': 149.211, 'S': 105.093, 'C': 121.158,
        'H': 155.155, 'N': 132.118, 'T': 119.119, 'D': 133.103, 'I': 131.173,
        'P': 115.131, 'V': 117.146, 'E': 147.129, 'K': 146.188, 'Q': 146.145,
        'W': 204.225,  'F': 165.189, 'L': 131.173, 'R': 174.201, 'Y': 181.189
        }

    mwH2O = 18.015
    aa2abs280= {'Y':1490, 'W': 5500, 'C': 125}

    aa2chargePos = {'K': 10.5, 'R':12.4, 'H':6}
    aa2chargeNeg = {'D': 3.86, 'E': 4.25, 'C': 8.33, 'Y': 10}
    aaNterm = 9.69
    aaCterm = 2.34

    def __init__ (self, protein):
        '''
        Constructor method for the ProteinParam class
        '''
        protein = protein.upper() # converts every sequence to uppercase - useful across all programs
        splitSeq = ''.join(protein).split() # split at every space
        self.proteinSeq = ''.join(splitSeq).upper() # conncatenate strings
        
        # constructs dictionary that counts 
        self.aminoDict = {key:self.proteinSeq.count(key) 
                       for key in ProteinParam.aa2mw.keys()}
        

    def aaCount (self):
        '''
        takes in no arguments and counts the occurence of amino acids
        '''
        aaCount = 0
        for aa in self.proteinSeq: # goes through user input sequence
            if aa in self.aa2mw.keys(): # checks to see if amino acid dict keys match seq amino acids
                aaCount += 1
        return aaCount  

    def pI (self):
        '''
        takes in no arguments. theoretical isolelectric point can be estimated 
        by finding the particular pH that yields a neutral net Charge (closest to 0)
        '''
        charge = []
        rangeList = np.arange(0.0,14.01,0.01) # makes numpy array from 0 to 14 spaced by 0.01
        for pH in rangeList:
            charge.append(self._charge_(pH))
        value = min(charge, key=abs) # finds smallest value - straight from my codelab 
        index = charge.index(value) * 0.01 # finds index which correlates to pH 
        return index

    def aminoDictosition (self) :
        '''
        takes in no arguments. returns a dictionary of amino acid counts from constructor
        '''   
        return self.aminoDict 

    def _charge_ (self,pH):
        '''
        takes in pH as a parameter to find net charge at certain pH level. 
        This method calculates the net charge on the protein at a specific pH
        '''
        pos, neg = 0.0, 0.0
        for aa in self.proteinSeq:   
            # summation for positive charge
            if aa in self.aa2chargePos.keys():   
                pos += (10 ** self.aa2chargePos[aa])/ (10 ** self.aa2chargePos[aa] + (10 ** pH))  
            
            # summation for negative charge
            elif aa in self.aa2chargeNeg.keys():
                neg += (10**pH)/(10**self.aa2chargeNeg[aa]+ (10 ** pH))
                
            else:
                continue
        # adds the N and C terminus
        pos += (10**self.aaNterm)/(10**self.aaNterm + 10**pH)
        neg += (10**pH)/(10**self.aaCterm+10**pH)
        netCharge = pos - neg
        
        return netCharge

    def molarExtinction (self):
        '''
        takes in no arguments. The extinction coefficient indicates how much light 
        a protein absorbs at a certain wavelength. From the molar extinction 
        coefficient of tyrosine, tryptophan and cystine at a given wavelength, 
        the extinction coefficient of the native protein in water can be computed:
        
        𝐸=(𝑁_𝑌*𝐸_𝑌)+(𝑁_𝑊*𝐸_𝑊)+(𝑁_𝐶*𝐸_𝐶)
        '''
        # equation above
        molarExt = float((self.aminoDict.get('Y')*self.aa2abs280['Y']) + (self.aminoDict.get('W')*self.aa2abs280['W']) + (self.aminoDict.get('C')*self.aa2abs280['C']))
        return molarExt
                         
    def massExtinction (self):
        '''
        takes in no arguments. Using molar extinction and molecular weight we can calculate massExtinction
        '''
        myMW =  self.molecularWeight()
        return self.molarExtinction() / myMW if myMW else 0.0

    def molecularWeight (self):
        '''
        takes in no arguments. Calculates amino acids molecular weights and excluding the waters 
        that are released with peptide bond formation
        '''
        sumVal = 0
        water = self.mwH2O * (self.aaCount() - 1) # calculates water
        
        # runs summation that calculates molecular weight
        for aa in self.proteinSeq:
            if aa in self.aa2mw.keys():
                sumVal += self.aa2mw.get(aa)
        
        molecWeight = sumVal - water
        return molecWeight
    
    
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

        
class OrfFinder():
    '''
    class that finds genes in open reading frames from FASTA file
    '''

    def __init__(self, sequence):
        '''
        Constructor method that sets up all seqence orf algorithm
        '''
        self.sequence = sequence
        self.complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        self.stopCodons = ['TAG','TAA','TGA']
        self.startCodons = ['ATG']
        self.found_orfs = [] 

    def reverse(self):
        '''
        returns the reverse complement of the DNA strands
        '''
        rev = list(self.sequence)
        rev = reversed([self.complement.get(nuc, nuc) for nuc in rev])
        rev = ''.join(rev)
        
        reverse_seq = rev
        
        return reverse_seq

    def add_Orf(self, frame, start_index, stop_index, seq_length):
        '''
        adds genes found to orfs list
        '''
        self.found_orfs.append([frame, start_index, stop_index, seq_length])
        
    def Orf_search(self, minlength):
        '''
        Find genes in Open reading frames on the 3'-5' strand 
        '''
        pos = [] # empty list that tracks the start 
        startPos = False
        codonIterate = False

        for frame in range(0,3): 
            startPos = False  
            codonIterate = False
            pos = []
            for i in range(frame, len(self.sequence), 3):
                # reads a codon at a time
                codon = self.sequence[i:i+3] 
                # begins counting sequence length after first codon is found
                if codon in self.startCodons:
                    startPos = True
                    codonIterate = True
                    pos.append(int(i)) # updates position
                
                # when stop codon is found, we check whether it is a valid orf
                if (codon in self.stopCodons) and startPos == True:
                    start = pos[0] + 1 - frame
                    stop = i + 3
                    if frame == 0:
                        length = stop - start + 1
                    if frame == 1:
                        length = stop - start
                    if frame == 2: 
                        length = stop - start - 1
                    if length > minlength:
                        self.add_Orf((frame%3)+1, start, stop, length)
                            
                    pos = []
                    
                    startPos = False
                    codonIterate = True
                
                # edge case for no start codon but found stop codon, dangling end
                if (codon in self.stopCodons) and (codonIterate == False):  
                    start = 1
                    stop = i + 3
                    length = stop - start + 1
                    if length > minlength:
                        self.add_Orf((frame%3)+1, start, stop, length)
                    pos = []
                    
                    codonIterate = True
                    
            # edge case for start codon but found no stop codon, dangling stop
            if startPos == True:  
                start = pos[0] + 1
                stop = len(self.sequence)
                length = stop - start + 1
                if length > minlength:
                    self.add_Orf((frame%3)+1, start, stop, length)
        return self.found_orfs

    def rev_Orf_search(self, minlength): #go trhough test file and comment out working lines, then compare orfs by hand to find error
        '''
        Find genes in Open reading frames on the 5'-3' strand 
        '''
        # extract a reverse complemented sequence
        revSeq = self.reverse()
        pos = []
        startPos = False
        codonIterate = False
        
        # repeat Orf finder algorithm - first iterate through 3 frames
        for frame in range(0, 3):  
            startPos = False  
            codonIterate = False
            pos = []
            
            # check through each codon
            for i in range(frame, len(revSeq), 3):
                codon = revSeq[i:i + 3]  
                
                # if codon is a start codon start tracking index and length
                if codon in self.startCodons:  
                    pos.append(i)
                    startPos = True
                    codonIterate = True
                
                # if codon is a stop codon start calculating  length
                if (codon in self.stopCodons) and (startPos == True):  
                    stop = len(revSeq) - pos[0]
                    start = len(revSeq) - (i+2)
                    length = stop - start + 1
                    if length > minlength:
                        self.add_Orf(((frame%3) + 1)* -1, start, stop, length)
                    pos = []
                    startPos = False
                    codonIterate = True
                
                # edge case for no start codon but found stop codon, dangling end
                if (codon in self.stopCodons) and (codonIterate == False):  
                    start = len(revSeq) - i - 1
                    stop = len(revSeq)
                    length = stop - start + 1
                    if length > minlength:
                        self.add_Orf(((frame%3) + 1)* -1, start, stop, length)
                    pos = []
                    codonIterate = True
            
            # edge case for start codon but found no stop codon, dangling stop
            if startPos == True:  
                start =  pos[0] + 1
                stop = 1
                if length > minlength:
                    length = stop - start + 1
                self.add_Orf((-1 * (frame%3) + 1), start, stop, length)
        return self.found_orfs

