#!/usr/bin/env python3 
# Name: Simon Lee (siaulee)
# Group Members: Campbell Strand, Mateo Etcheveste, Jonathan Zau
'''
Program that takes various statistics based on user input of amino acid (protein) sequence
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
          

# Please do not modify any of the following.  This will produce a standard output that can be parsed
    
import sys
def main():
    '''
    Main Driver of the code
    '''
    inString = input('protein sequence?')
    while inString :
        myParamMaker = ProteinParam(inString)
        myAAnumber = myParamMaker.aaCount()
        print ("Number of Amino Acids: {aaNum}".format(aaNum = myAAnumber))
        print ("Molecular Weight: {:.1f}".format(myParamMaker.molecularWeight()))
        print ("molar Extinction coefficient: {:.2f}".format(myParamMaker.molarExtinction()))
        print ("mass Extinction coefficient: {:.2f}".format(myParamMaker.massExtinction()))
        print ("Theoretical pI: {:.2f}".format(myParamMaker.pI()))
        print ("Amino acid composition:")
        
        if myAAnumber == 0 : myAAnumber = 1  # handles the case where no AA are present 
        
        for aa,n in sorted(myParamMaker.aminoDictosition().items(), 
                           key= lambda item:item[0]):
            print ("\t{} = {:.2%}".format(aa, n/myAAnumber))
    
        inString = input('protein sequence?')
        

if __name__ == "__main__":
    main()
    
    # VLSPADKTNVKAAW - example user input
