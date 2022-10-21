PROGRAM DESCRIPTION
-------------------
Rosalind problem PRTM involves computing the weight of a protein using the monoisotopic masses of amino acids. The monoisotopic mass table necessary for this Rosalind problem exists in simple text form on our server, in file amino-monoisotopic-mass. View that file in the browser or a text editor to see how it is formatted.

The Problem itself:

In a weighted alphabet, every symbol is assigned a positive real number called a weight. A string formed from a weighted alphabet is called a weighted string, and its weight is equal to the sum of the weights of its symbols.

The standard weight assigned to each member of the 20-symbol amino acid alphabet is the monoisotopic mass of the corresponding amino acid.

Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.

Sample Dataset
SKADYEK
Sample Output
821.392

HOW TO RUN PROGRAM
------------------
I recommend running this on the IDLE since you will need to use a REPL session.
Version 3.9 of Python is highly recommended.
Here is a REPL session demonstrating a working version of class Protein:
```
>>> from rosalind import Protein
>>> demo = Protein('MAMAPRTEINSTRING')
>>> demo
Protein('MAMAPRTEINSTRING')
>>> demo[0]
'M'
>>> demo[-1]
'G'
>>> demo[4:10]
Protein('PRTEIN')
>>> len(demo)
16
>>> print(demo)
MAMAPRTEINSTRING
>>> demo + demo
Protein('MAMAPRTEINSTRINGMAMAPRTEINSTRING')
>>> demo + 'SKADYEK'
Protein('MAMAPRTEINSTRINGSKADYEK')
>>> demo + '!!!'
Traceback (<redacted>):
ValueError: Invalid amino acid character: !
>>> demo.mass()
1742.8556
>>> Protein('SKADYEK').mass()
821.3919199999999
>>> demo == demo
True
>>> demo == 'MAMAPRTEINSTRING'
True
>>> demo == Protein('MAMAPRTEINSTRING')
True
>>> demo == 'MAMAPRTEINSTRING!'
False
>>> demo == Protein('SKADYEK')
False
```
