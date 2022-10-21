PROGRAM DESCRIPTION
-------------------
You may be familiar with the process of protein (bio)synthesis, which is fundamental to the function of all living beings here on Earth.

In a very real—but also very messy—way, the DNA in all of our cells contains programs (genes) executed by various components of our cells. Genes are sequences of genetic code that most commonly result in the creation of proteins, which are polypeptide molecules consisting of a sequence of amino acids. Proteins are the major product of our cells. The essential idea is that DNA is transcribed into mRNA in the nucleus of a cell, which ribosomes then translate into actual protein molecules.

As you may know, the recent Pfizer/BioNTech and Moderna vaccines against COVID-19 are actually just a bunch of synthetic mRNA packed in lipids for transport. When injected into our bloodstream, this RNA enters our immune cells, which then dutifully create the protein encoded by the RNA—in this case, a slightly modified version of the spike protein found on the surface of actual SARS-CoV-2 viral bodies.

Rosalind problem PROT regards simulating the process of translating RNA into proteins. Given a RNA string (A/C/G/U characters) as input, we produce a protein string as output, using 20 different English letters to represent the 20 different amino acids most commonly produced during protein biosynthesis. The concept is simple: Each codon (triplet of nucleotides in RNA) codes for a single amino acid. Special start and stop codons indicate beginning and end points of the translation process.

HOW TO RUN PROGRAM
------------------
One interesting way of testing your module functions is to search a genome (or part of one) for possible proteins and see if they correspond to the products of any actual genes that have been identified by scientists in the relevant genome.

For example, the following module, if placed in the same directory as rosalind, would print (one per line) all potential proteins in standard input, which is assumed to contain a DNA string.
```
"""
Prints all potential proteins, one per line, encoded by DNA on standard input.
"""
import re
import sys
import rosalind

if __name__ == '__main__':
  # Use a regular expression to discard all non-A/C/GT characters, then transcribe the DNA to RNA
  rna = re.sub('[^ACGT]', '', sys.stdin.read()).translate({ord('T'): ord('U')})
  # Print the elements of the list returned by rosalind.potential_proteins(), one per line
  print('\n'.join(rosalind.potential_proteins(rna)))
```
