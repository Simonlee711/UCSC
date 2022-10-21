Simon Lee
siaulee
Winter 2021
Lab 4: Syntax Checker

-----------------------
DESCRIPTION
-This lab is our second one used on the MARS program. This lab is by far more complex than the previous one and the objective is to read a file from a program argument (user input) and then that will be used to check for balanced brackets, braces, and parentheses. EX: A balanced parentheses would be an open parentheses corresponded by a closed parentheses anywhere throughout the program;    (hello). There are a few errors that can occur in the lab. One is if there is stuff that are pushed to the stack and never popped, there is if there's nothing left to pop in the stack, and lastly there is if there is a mismatch between braces, brackets and parentheses ex: ( }. This lab has many conditions that are required that need to be met in order for this lab to run smoothly. Within the program argument itself it has top start with a letter and cannot exceed 20 characters. While very technical it has been one of the coolest labs to make out of scratch!

-----------------------
FILES

Lab4.asm
This file includes the MIPS assembly code which was made in design of the description
TEST.txt
This file is one of the test cases used for my lab.
TESTtwo.txt
This file is one of the test cases used for my lab.
TESTthree.txt
This file is one of the test cases used for my lab.

-----------------------
INSTRUCTIONS

As previously mentioned this program is run on (MARS). Once you've opened up the file you can run the program by first assembling the program, then running it. You will be asked to put in a program argument aka a text file, which will then be properly opened and read. The contents that the syntax checker is looking for are the braces, brackets, and the parantheses When these values are found in the txt file it will be pushed onto the stack which a data structure where memory can be pushed or stored, or popped and pulled out. So to keep track of where an error might occur there are multiple counters implemented incase there's a mismatch, nothing left on the stack, or if everything is left on the stack. Very cool Lab when it is run through mips!
