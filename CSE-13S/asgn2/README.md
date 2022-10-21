PROGRAM DESCRIPTION
-------------------
This program is called "A small numerical library". This program 
involved us making several functions that were supposed to 
replicate the behaviour of that of a typical math library
that we could simply import. This program was designed to help
us understand how exactly a library is made since computers can
only typically compute values with the operators: addition, 
subtraction, multiplication, and division. So in this assignment
we were asked to make a library for the computations of arcSin,
arcCos, arcTan, and Log. To do so we also needed mathematical 
functions Absolute value, Exponential, and Square Root. Lucky
for us we were provided some of these functions so it would 
not be as difficult. To find these approximations we were
require to use Methods: Taylors Series and/or Newton's Method.
I used both for this assignment and rather enjoyed seeing the
progression of this assignment. But I will warn you that my 
approximations for arcSin, and arcCos at values 1, and -1 are
not as accurate as I want them to be. 

HOW TO BUILD PROGRAM
--------------------
In order to build this mathlib-test.c program you will need to use the
makefile that I have included in this repository. Unlike the previous
assignment this makefile was a little differnt in which we had to 
link all the different files used to the make file using command -lm.
The files that were included in the process of making these files are
as follows: mathlib-test.c, mathlib.h, and mathlib.c. All these files
are described in the DESIGN.pdf so if you are curious as to what these 
files do, feel free to read the DESIGN document. Once you make 
mathlib-test, you will see that it compiles. 

HOW TO RUN THE PROGRAM
----------------------
Once we have compiled the program in the previous step we are then 
going to prompt the command ./mathlib-test -"1/5 choices". obviously 
we will not be entering quite that but in this assignment we utilized
a command called getopt where we get an argv and argc which will allow
us to prompt a command straight from the command line interface. For 
this assignment we have 5 choices those being "a" resembling all, "s" 
resembling arcSin, "c" resembling arcCos, "t" resembling arcTan, and 
lastly "l" resembling Log. so by prompting in ./mathlib-test -a for 
example, it will first call the functions listed, in this case it is
all the mathematical functions. Why you may ask. Well I have implemented
a flag system where when prompted, the flags will change from 0 to 1
in which those commands will be executed. So in this case arcSin will
be called and printed for its values from -1 to 1, then arcCos will be 
called and printed for its values from -1, to 1, etc. That is what is 
essentially happening in this mathlib-test.c file and there we go. We
have successfully implemented this program!

WHAT TO PUT IN TERMINAL
-----------------------
```
make
```
```
./mathlib-test [-a][-s][-c][-t][-l]
```
