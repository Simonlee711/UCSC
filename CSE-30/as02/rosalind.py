#!/usr/bin/envpython3                                                                               
"""                                                                                                 
assignment2 - rosalind.py                                                                           
"""                                                                                                 
__author__ = 'Simon Lee for CSE30 Spring 2021, siaulee@ucsc.edu'                                    
                                                                                                    
import re                                                                                           
                                                                                                    
                                                                                                    
def dataset():                                                                                      
    amino_dict = {}  # start with empty dictionary                                                  
    with open("amino.txt", "r") as amino_file:                                            
        for lines in amino_file:                                                                    
            data = lines.split()                                                                    
            dna_conv = re.sub('[^ACGT]', '', data[0]).translate({ord('T'): ord('U')})               
            # straight from the website to convert dna to rna                                       
            amino_dict[dna_conv] = data[2]                                                          
                                                                                                    
    return amino_dict                                                                               
                                                                                                    
                                                                                                    
amino = dataset() 


def prot(rna: str) -> str:                                                                          
    """                                                                                             
    Calculates and returns the protein string encoded by an RNA string, or None if the encoding is  
    valid. A valid encoding consists of 12 or more codons, where the first is start codon 'AUG',    
    followed by at least 10 more non-stop codons, and then a stop codon.                            
    (The shortest known protein is length 11: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3864261/)
                                                                                                    
    Amino-acid encoding information shall be taken from the dict represented by variable amino.     
                                                                                                    
    :param rna: An RNA string (assumed to contain characters in 'ACGU', with len(rna) % 3 == 0).    
    :return: The protein string encoded by rna, or None if the the encoding is invalid.             
    """ 
    full_protein = ''  # this is an empty protein string variable that will be filled.              
    if len(rna) < 36:                                                                               
        return                                                                                      
    else:                                                                                           
        if len(rna) % 3 != 0:                                                                       
            return                                                                                  
        else:                                                                                       
            if rna[0:3] == 'AUG' and (rna[-3:] == 'UAA' or rna[-3:] == 'UAG' or rna[-3:] == 'UGA'): 
                for p in range(0, len(rna), 3):  # p is the iterator                                
                    if amino[rna[p:p + 3]] == 'O':                                                  
                        if len(rna) != len(rna[0:p + 3]):                                           
                            return                                                                  
                        else:                                                                       
                            break                                                                   
                    else:                                                                           
                        protein = amino[rna[p: p + 3]]                                              
                        full_protein += protein                                                     
                if len(full_protein) < 12:                                                          
                    return                                                                          
                else:                                                                               
                    return full_protein                                                             
            else:                                                                                   
                return  


def potential_proteins(rna: str) -> list[str]:                                                      
    """                                                                                             
    Calculates and returns all potential valid protein encodings in an RNA string. Any protein valid
    according to function prot() shall be considered valid by this function as well.                
                                                                                                    
    Amino-acid encoding information shall be taken from the dict represented by variable amino.     
                                                                                                    
    :param rna: An RNA string (assumed to contain characters in 'ACGU').                            
    :return: A list of the possible proteins in the RNA, in the order encountered in the RNA.       
    """                                                                                             
    pot_prot = []                                                                                   
    for i in range(len(rna)):  # checks every 3 but doesn't but iterates by 1                       
        codon = rna[i: i + 3]  # codon checker                                                      
        if codon == 'AUG':                                                                          
            full_protein = ''                                                                       
            for j in range(i, len(rna), 3):                                                         
                if len(rna[j:j + 3]) % 3 == 0:                                                      
                    if amino[rna[j: j + 3]] == 'O':                                                 
                        valid_protein = prot(rna[i:j + 3])                                          
                        break                                                                       
                    else:                                                                           
                        protein = amino[rna[j: j + 3]]                                              
                        full_protein += protein                                                     
            if valid_protein is None:                                                               
                continue                                                                            
            else:                                                                                   
                pot_prot.append(full_protein)  # appends to list                                    
    return pot_prot                                                                   
