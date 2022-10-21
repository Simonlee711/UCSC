PROGRAM DESCRIPTION
-------------------
The Great Firewall of Santa Cruz is an assignment using Bloomfilter's, Linked lists,
Hash tables, and a few other ADT's we have previously covered (bit vectors, nodes) and the 
purpose of the program is to filter out badspeak and replace oldspeak words into their
new and improved newspeak forms. This assignment could be easily accomplished by simply
doing dictionary lookups but the point of this assignment is to introduce us to bloom 
filters which is an ADT which simply lets you know whether a member (a word) is in a set.
By being able to identify the badspeak and the oldspeak we can send out the corresponding 
automated message warning the citizens of the Glorious Peoples Republic of Santa Cruz, or 
even threatening them and sending them to joycamp so they will never use these degenrate 
words. Another thing that we learned through this is hashing which basically encoding 
data or in this case a word and giving it a unique identifier that we can easily look up. 
Overall this assignment is pretty nifty and its been a great journey to say the least to 
be finishing up this class. 

HOW TO BUILD PROGRAM
--------------------
Like previous assignments within the repository we always have a makefile which links and
connects the appropriate files to create object files and executables that we can run. For 
this assignment we will have one main file from our banhammer.c file and it will be the main
file that brings all the ADT's and performs the functionality of the program. By prompting 
make in the terminal it will build you the ./banhammer executable that you will be able to 
run.

HOW TO RUN PROGRAM
------------------
When it comes to running the program we must first explain as always all the command line 
arguments that it takes. This program will run primarily on standard input or output but you
can always have it read in from an infile by simply running ./banhammer < (name of text).txt.
But this program like many of our programs has a -h which contains a helper message which will
tell you how specifically you run the program. We also have -t and a -f which is similar to our 
sorting assignment in which you can customize the size of the hash table and the bloom filter 
but by default the hash table is a size of 10,000 and the bloom filter size at default is 2^20.
And lastly we have the -m which I have explained in my write up which is the move to the front 
which may affect the overall time complexity of the linked list. We also have -s which we may
have previously referred to as verbose printing in that it will print the statistics of the
program. Some of the the statistics that will be calculated are the average seek length, hash
table load, and bloom filter load. All these features will be simply printed to standard output
and if you are curious as to what everything means you may read more about it in my 
WRITEUP.pdf which is also somewhere in the repository

WHAT TO PUT IN TERMINAL
-----------------------
```
make
```
```
./banhammer [-h] [-s] [-m] [-t size] [-f size]
```

FINAL THOUGHTS
---------------
Its been quite the eventful journey in this class. These past 7 assignments have been some of the
toughest but most rewarding assignments of my life and I can't believe how awesome its been to make 
it to the end of another class in my young computer science journey. I truly learned about a lot of 
ADT's and overall about computer systems. Without a doubt this has been the best class of my young 
career and I cannot wait to dive deeper into the field of Computer Science. I wanna thank Darrell 
Long, Eugene Chou, Sahiti Vallamhr, Sabrina Au, Brian Zhao, Eric Hernandez, Miles Galpa Grossklag
and Jloritz from discord for their help every week. I also just wanted to shoutout some of my friends
I was able to make through this class in Mhia Grace Mojica, Audrey Ostrom, Harlene Virk, Sean Fujiwara,
and Sam Garcia. After going to the same sections over and over together, it was nice to branch out to 
other people in this class because it hasn't been the easiest year with COVID-19 and the lack of 
connection and friends you normally make in class. I am very much about documenting things so this
may be weird but Overall 11/10 experience. Great class. highly recommend and just feeling grateful
and smarter than I was a quarter ago :) 

-Simon Lee on June 3rd, 2021
