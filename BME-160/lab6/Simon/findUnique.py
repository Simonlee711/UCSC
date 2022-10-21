#!/usr/bin/env python3 
# Name: Simon Lee (siaulee)
# Group Members: Campbell Strand, Mateo Etcheveste, Jonathan Zau
'''
This module is a class that finds all unique subsets for tRNA sequences as discussed in class
'''
class tRNAsFinder:
    '''
    This class utilizes sets to find all unique subsets of tRNA sequences and stores them in a list
    '''

    def __init__(self, seq=""):
        '''
        Constructor method for the uniqueFinderclass
        '''
        self.seq = seq
        self.tRNAs = []
        
        
    def cleanSeq(self, sequence):
        '''
        Cleans sequence of '-', '_', and '.' 
        '''
        temp = sequence.upper()
        temp_seq = temp.replace("-", "")
        temp2_seq = temp_seq.replace("_", "")
        self.seq = temp2_seq.replace(".","")

    
    def powerSet(self):
        '''
        #Finds the Power set of the sequence. [powerset] 
        '''
        # Just following professors rough design plan
        powerset = []
        size = len(self.seq)
        for index in range(size):
            for sub in range(index + 1, size + 1): # iterates through all possible subsets
                powerset.append(self.seq[index:sub]) # adds subset to the powerset list
        if powerset not in self.tRNAs:
            self.tRNAs.append(powerset)
        return powerset

    
    def uniqueSubsets(self):
        '''
        Function that returns all unique subsets of a sequence. [Unique]
        '''
        # Just following professors rough design plan
        PowerSets = self.tRNAs
        PowerSets.remove(self.powerSet())
        PowerSets = set().union(*PowerSets) # converts list to set and takes union of powerset 
        subset = set(self.powerSet()) - PowerSets
        return list(subset)

    def getEssentials(self):
        '''
        gets the essential. [Essential]
        '''
        nonEssential = []
        unique = self.uniqueSubsets()
        copy = self.uniqueSubsets()

        for subset in unique:
            copy.remove(subset)
            for comb in copy:
                if subset in comb:
                    if comb not in nonEssential:
                        nonEssential.append(comb) # appends a list of nonessential values to subtract later on
            copy.append(subset)
        return  set(unique).difference(set(nonEssential)) # This returns simply the essential tRNAs


################################################################################################################################
import sequenceAnalysis

def indexFinder(string, sub):
    '''
    
    '''
    indices = []
    for i in range(len(string)):
        index = string.find(sub, i) # Professors hint
        # checks to see if we have hit end of string
        if index == -1:
            break
        if index not in indices:
            indices.append(index)
            
    return indices


def main():
    '''
    Main Driver of the code
    '''
    # Create all objects
    fastaReader = sequenceAnalysis.FastAreader()
    uniqueFinder = tRNAsFinder()
    output = []

    for header, seq in fastaReader.readFasta():
        aa = header[8:11] # sort by amino acid name hence we index splice
        uniqueFinder.cleanSeq(seq) # cleans up sequence for printing
        output.append((aa, header, seq)) # appends a set of 3 variables
        uniqueFinder.powerSet()
    output.sort()
    
    # iterates through all fasta file content and prints appropriatley
    essentials = [] 
    for aa, header, seq in output:
        uniqueFinder.cleanSeq(seq)
        essentials.clear() 
        
        for essential in uniqueFinder.getEssentials():
            finder = indexFinder(uniqueFinder.seq, essential)
            for pos in finder:
                tup = (essential, pos)
                essentials.append(tup)
        essentials.sort(key=lambda tup: tup[1]) # sorted for printing
        
        # Print statements
        print(header +"\n"+ uniqueFinder.seq)
        for subset in essentials:
            print(subset[1]*"." + subset[0])
    
    
if __name__ == "__main__":
    main()