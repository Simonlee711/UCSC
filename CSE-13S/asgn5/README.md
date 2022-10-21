PROGRAM DESCRIPTION
--------------------
Hamming codes is an error correction algorithm which will
know where the errors are based on the parity bits calculated.
Parity bits are calculated from performing a matrix multiplication
with the Generator Matrix. This is essentially what the encode.c 
file is doing: generating a hamming code. Now that we have an encoded 
hamming code we want to find the error syndrome which is using the 
same process in which we matrix multiply a H transpose matrix in which
we recieve our error syndrome. After that we can check to see if the
error syndrome is in the lookup table and we can do that by setting 
up an array of 16 elements because 0000 - 1111 in binary can only go
up to 0-15 which is exactly what we want. Then it will correct itself
if it can be and were done.

ISSUES WITH MY PROGRAM
----------------------
program statistics are not correct :(

off by way to much

HOW TO BUILD PROGRAM
--------------------
In order to build the program we first must compile it and in this 
particular assignment we had alot of main files so we had to make an
executable for each of them separatley but could also make them all if 
we prompted all in our terminal. 

HOW TO RUN PROGRAM
-------------------
As always there are a set of opt arg command options that we have for 
this assignment. Beginning in ./encode we have three optarg arguments
we could put which is -h helper message, -i to read a specified in file
and -o to write to a specified outfile. And in ./decode we have the same
thing as encode but with an additional -v verbose which prints out the
statistics for the file. 

WHAT TO PUT IN TERMINAL
-----------------------
```
make
```
```
//to run encoder
./encode [-h] [-i infile] [-o outfile]
```
```
//to run decoder
./decode [-h] [-v] [-i infile] [-o outfile]
```
