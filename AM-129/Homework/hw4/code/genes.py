'''
Python module to visualize SARS-CoV-2 sequence data
'''
__author__ = 'Simon Lee: siaulee@ucsc.edu'

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def codon_counter(DNAseq):
    codon_table = dict()
    codon = [DNAseq[i:i+3] for i in range(0, len(DNAseq), 1)]
    
    for DNA in codon:
        if DNA in codon_table:
            codon_table[DNA] += 1
        else:
            codon_table[DNA] = 1
    
    # delete non codon entries 
    del codon_table['aa\n']
    del codon_table['a\n']
    del codon_table['\n']
    
    return codon_table

def plot_codon(histo):
    plt.figure(figsize=(16,8)) 
    plt.bar(range(len(histo)), histo.values())
    plt.xticks(range(len(histo)), list(histo.keys()), rotation='vertical')
    plt.grid()
    plt.ylabel('Frequency')
    plt.xlabel('Codon');
    plt.title("Codon frequency in SARS-CoV-2");
    plt.savefig('histogram.png')
    plt.show()

def baseDensity(geneStr, nWind=200):
    A = np.zeros(len(geneStr)-nWind)
    C = np.zeros(len(geneStr)-nWind)
    G = np.zeros(len(geneStr)-nWind)
    T = np.zeros(len(geneStr)-nWind)
    for n in range(0,len(geneStr)-nWind):
        A_count = geneStr[n:n+nWind].count('a')
        C_count = geneStr[n:n+nWind].count('c')
        G_count = geneStr[n:n+nWind].count('g')
        T_count = geneStr[n:n+nWind].count('t')
        A[n] += A_count/nWind
        C[n] += C_count/nWind
        G[n] += G_count/nWind
        T[n] += T_count/nWind
    return A, T, C, G

def plot_density(dA, dT, dC, dG):
    plt.figure(figsize=(16,8))
    plt.plot(dA)
    plt.plot(dT)
    plt.plot(dC)
    plt.plot(dG)
    plt.grid()
    plt.ylabel('Fraction per window')
    plt.xlabel('Sequence Position')
    plt.title("Density of base pairs through gene sequence")
    plt.legend(('A','T','C','G'), loc='upper left')
    plt.savefig('density.png')
    plt.show()

if __name__=="__main__":
    # Open genome
    with open('sarsCov2Sequence.txt','r') as geneFile:
        geneStr = geneFile.readline()
    
    # Generate codon histogram
    histo = codon_counter(geneStr)
    # Plot histogram with nice formatting
    plot_codon(histo)
    # Find base-pair density
    #dA,dT,dC,dG = baseDensity(geneStr)
    #plot_density(dA, dT, dC, dG)
    # Or supply a different window width
    dA,dT,dC,dG = baseDensity(geneStr, nWind=500)
    plot_density(dA, dT, dC, dG)
    
