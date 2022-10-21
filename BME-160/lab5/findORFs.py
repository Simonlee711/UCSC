#!/usr/bin/env python3 
# Name: Simon Lee (siaulee)
# Group Members: Campbell Strand, Mateo Etcheveste, Jonathan Zau

from sequenceAnalysis import OrfFinder, FastAreader

"""
ORF Finder
----------
iterate through three frames from 3' - 5'
    iterate through codons through splicing i, i+3
        if a start codon is found
            add its index
        if a stop codon is found
            find its index
            find its length
            if length is > minlength
                save the gene from orf
            reset variables
        
        check for frame with with no start codon but a end codon
            repeat steps from first set of if statements
        
        check for frame with start codon but no end codon
            repeat steps from above

**repeat for reverse from 5' to 3' end**

"""


########################################################################
# CommandLine
########################################################################
class CommandLine() :
    '''
    Handle the command line, usage and help requests.

    CommandLine uses argparse, now standard in 2.7 and beyond. 
    it implements a standard command line argument parser with various argument options,
    a standard usage and help.

    attributes:
    all arguments received from the commandline using .add_argument will be
    avalable within the .args attribute of object instantiated from CommandLine.
    For example, if command is an object of the class, and requiredbool was
    set as an option using add_argument, then command.args.requiredbool will
    name that option.
 
    '''
    
    def __init__(self, inOpts=None) :
        '''
        Implement a parser to interpret the command line argv string using argparse.
        '''
        
        import argparse
        self.parser = argparse.ArgumentParser(description = 'Program prolog - a brief description of what this thing does', 
                                             epilog = 'Program epilog - some other stuff you feel compelled to say', 
                                             add_help = True, #default is True 
                                             prefix_chars = '-', 
                                             usage = '%(prog)s [options] -option1[default] <input >output'
                                             )
        self.parser.add_argument('-lG', '--longestGene', action = 'store', nargs='?', const=True, default=False, help='longest Gene in an ORF')
        self.parser.add_argument('-mG', '--minGene', type=int, choices= (100,200,300,500,1000), default=100, action = 'store', help='minimum Gene length')
        self.parser.add_argument('-s', '--start', action = 'append', default = ['ATG'],nargs='?', 
                                 help='start Codon') #allows multiple list options
        self.parser.add_argument('-t', '--stop', action = 'append', default = ['TAG','TGA','TAA'],nargs='?', help='stop Codon') #allows multiple list options
        self.parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')  
        if inOpts is None :
            self.args = self.parser.parse_args()
        else :
            self.args = self.parser.parse_args(inOpts)


def main():
    '''
    A program that reads in a fasta file from command line argument and prints out genes from longest to shortest
    '''
    command = CommandLine()
    if command.args.longestGene:
        fastaFile = FastAreader()
        
        # use same file reader code from last week
        for header, sequence in fastaFile.readFasta():
            print(header)
            # create an OrfFinder object
            orf_info = OrfFinder(sequence)
            
            #append list of genes found with minGene argument
            orf_info.Orf_search(command.args.minGene)
            orf_info.rev_Orf_search(command.args.minGene)
            # print statement that sorts our genes by longest length to shortest length
            orf_list = sorted(orf_info.found_orfs, key=lambda orf: orf[3], reverse = True)
            print(orf_list)
            for frame, start_index, stop_index, seq_length in orf_list:
                if seq_length > command.args.minGene: 
                    print('{:+d} {:>5d}..{:>5d} {:>5d}'.format(frame, start_index, stop_index, seq_length))

        

if __name__ == "__main__":
    main()