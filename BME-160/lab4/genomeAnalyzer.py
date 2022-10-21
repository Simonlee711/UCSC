#!/usr/bin/env python3 
# Name: Simon Lee (siaulee)
# Group Members: Campbell Strand, Mateo Etcheveste, Jonathan Zau

'''
A program that prints statistics of FastA file
'''

from sequenceAnalysis import ProteinParam, NucParams, FastAreader

class genomeAnalyzer:
    """
    This Program calculates codon usage, sequence size, gcContent
    """
    def __init__(self, filename='testGenome.fa'):
        '''
        Constructor for genomeAnalyzer
        '''
        self.filename = filename
        
        
    def mb_calculator (self, fastaFile):
        '''
        This function calculates the megabases of a DNA sequence
        '''
        
        #Professors main code, reads in fasta file. Changed variables for readability
        nucleotides = NucParams()
        for head, seq in fastaFile.readFasta():
            nucleotides.addSequence(seq)

        megaBase = nucleotides.nucCount()/ 1000000

        return megaBase, nucleotides
    
    def gc_pct(self, nucSeq):
        '''
        Method that calculates GC percentage within a sequence
        '''
        nucleotides = nucSeq.nucComposition()
        gc_count = nucleotides['G'] + nucleotides['C']
        return gc_count / nucSeq.nucCount() * 100
    
    def codonStats(self, codons, nucParams):
        '''
        Method that returns codon stats:
        -codon
        -amino acid
        -codon count
        -final percentage
        '''
        # labmda expression to get dictionary sorted correctly
        dict_ = dict(sorted(nucParams.rnaCodonTable.items(), key=lambda item: item[1])) 
        sort_codon = list(dict_.keys())
        aa = []
        aa_count = []
        codon_count = []
        for codon in sort_codon:
            
            aa.append(nucParams.rnaCodonTable[codon])
            aa_count.append(nucParams.aaComp[nucParams.rnaCodonTable[codon]])
            codon_count.append(codons[codon])
            
        fpct = []
        for i in range(len(sort_codon)):
            if codon_count[i] > 0:
                fpct.append((codon_count[i]/aa_count[i])*100)
                continue
            else:
                fpct.append(codon_count[i]/1) *100
                continue
        
        return sort_codon, aa, codon_count, fpct 
            
    
    def print_stats(self):
        '''
        A method that prints all relevant statistics needed for the program
        '''
        self.myReader = FastAreader(self.filename)
        
        mb, nucParams = self.mb_calculator(self.myReader)
        GC_pct = self.gc_pct(nucParams)
        
        print("sequence length = "+ str(round(mb,2)) +" Mb\n")
        print("GC content = "+ str(round(GC_pct,1)) + "%\n")
        
        codons = nucParams.codonComposition()
        codon, aa, c_count, fpct = self.codonStats(codons, nucParams)
        
        done = False
        i = 0
        loopLength = len(codon)
        while not done:
            print('{} : {} {:5.1f}% ({:6d})'.format(codon[i], aa[i], fpct[i], c_count[i]))
            i += 1
            if loopLength <= i:
                done = True
            

def main (fileName=None):
    '''
    Main Driver of the code
    '''
    file_content = genomeAnalyzer()
    file_content.print_stats()
    
if __name__ == "__main__":
    main('testGenome.fa')
