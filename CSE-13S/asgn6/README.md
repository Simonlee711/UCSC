PROGRAM DESCRIPTION
-------------------
Huffman coding is a compressions algorithm that is very quite cool. The way it
works is that every unique character in a file is its own separate node including
0x00 and 0xFF incase your file contains nothing. Then each node in the binary tree
is assigned a code which can range from 1 bit to < 8 bits. This is actually where
the compression takes place in that a normal character takes up a whole byte but
the code of a character can be smaller than the typical 8 bits. After the file is
compressed, we will need communicate with the decoder somehow so then we can rebuild
the tree so in the encoder we must make another post traversal tree walk, to build an
array which indicates whether it is an 'L' or leaf node followed by its symbol or an
'I' which indicates its an internal nodes. After writing this out to the file the 
decode will first rebuild the tree by looking at the sequence containing the 'L' and
'I' and rebuild the binary tree. Once the binary tree has been built it will begin 
reading the encoded bits and walk the tree. In the process of walking the tree if it 
ever hits a leaf node it will realize it is the end of the line and will need to access
that leaf nodes character. This process will continue until it has hit the file.size 
which was passed in by the header and this way it will know when to stop incase we 
flushed the codes out somehow. After decompressing the code we will have the original
message. how very cool.


HOW TO BUILD PROGRAM
--------------------
This program like the lst one has multiple executable files. We have an entropy.c, 
encode.c, and a decode.c which all contain their own respective main files and we will
once again need to be able to run multiple main files at once to make this whole process
work if we want to do it all in one call. In the Makefile I have linked all the proper
files so it has access to all the functions in the ADT. And once we prompt make we will
be able to create object files for every .c file in this assignment. After that we are
now able to run the program 

HOW TO RUN PROGRAM
------------------
To run the program we have yet again some command line arguments that may be of good use.
And lucky for us encode and decode both have the same command line arguments so we wont 
need to explain them multiple times. We first begin per usual by either prompting in 
./encode or ./decode or ./entropy or you can even put them all on one line by piping.
Look at the following. ./encode -i corpora/artificial/a.txt | ./decode -o test.txt
Doing so will run both encode and decode at the same time and it will be able to compress
and decrompress the a.txt file that we prompted in and put its content into a dummy file
called test.txt. This is valid proof that the program works and I cannot wait for you to try
it. So if your run -h in encode or decode you will get a helper message which will sort of
explain what I just did in a condensed version. And as you saw in the example -i will take
in a infile that the user prompts. If none are specified it will just take in standard 
input. Next we have -o which takes in a specific output and if none are specified will be
printed to standard output. and lastley we have -v which is verbose which will print the
statistics for the compression that took place. Very cool assignment overall and I cannot
wait for you all to try it.

WHAT TO PUT IN TERMINAL
-----------------------
```
make
```
```
//to run encoder
./encode [-h] [-v] [-i infile] [-o outfile]
```
```
//to run decoder
./decode [-h] [-v] [-i infile] [-o outfile]
```
