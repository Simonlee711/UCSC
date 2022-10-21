PROGRAM DESCRIPTION
-------------------
This program is called "Sorting: Putting your affairs in order" and as 
imagined, it is a sorting program. Sorting is a fundamental concept all
computer scientists go through so it is crucial that it works. We were
asked to build a bubble sort, shell sort, and two quick sorts: one using
the stack abstract data type and using its opposite the queue another 
abstract data type. We also utilized a set data type in this assignment 
to help with organizing with printing the tables for the sorted numbers.
This assignment organizes dynamically allocated arrays meaning that you
can organize any amount of numbers as long as it fits in the uint32-t, 
meaning it has to be smaller than an unsigned integer of 32 bytes. We
also have a custom seed similar to what we had asgn 1 so we can organize
random numbers instead of the same numbers every time. We also have the
option to print out a specific amount of elements just so then when 
organizing a large array we don't have to print that whole finite set. 
Many files are included in this assignment and are listed in my Design
Doc, and after running scan-build there were no bugs generated. However
the compares and the moves, and the stack-size are very much off for 
quick.c. I sort of printed out these counts weird because I used a 
pass by reference so I ended up not being able to count the compares
and the moves inside the partition. Also there is an error when running
the command line argument -a and it prints more than I want it too

HOW TO BUILD PROGRAM
--------------------
In order to build the program it is very similar to the previous assignment
where we are restricted to a specific amount of command line arguments that
we can run in order to see whether the output is correct. However as always
there is a makefile that links all my c files together so the program works 
properly. In total I believe there were 14 files not involving the README.md,
DESIGN.pdf, WRITEUP.pdf, and Makefile that were needed for this assignment. 
So it was crucial to link all the files in the Makefile. Lastly like always
you can compile the program by simply running "make sorting" in the terminal. 

HOW TO RUN PROGRAM
------------------
Last part of this assignment is to explain the command line arguments to 
properly run the program. The command line arguments consist of -a for all
-b for bubble sort, -s for shell short, -q for quick sort (stack), -Q for
quick sort (queue), -r for specific seed generator, -n for specific size 
for a dynamically allocated array, and lastly -p for specific print size.
You can run multiple commands at a time but you will need atleast one of
the sorts to be included or no output will be displayed. This assignment
was one of my favorites to implement and I am excited to have finally gotten
to do a sorting program.

WHAT TO PUT IN TERMINAL
-----------------------
```
make
```
```
./sorting [-a][-b][-s][-q][-Q]
```
