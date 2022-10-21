PROGRAM DESCRIPTION
-------------------
This program is called left, right center and it is a game where
atleast 2 or up to 14 players can play. In this game everyone 
starts with $3 and are rolling a specific amount of dice based
on how many $ they have up to 3 dice. There is a 50% chance 
you roll a pass, but the other 50 percent is made up of a left
in which you give a $1 to the person to your left, right in which
you give a person to your dollar a right, and center in which
you put money in the center. Even if you have $0 at one point 
you can easily return to the game if adjacent players rolls a 
Left or Right. As soon as there is only one person left with 
money they are declared the winner.

HOW TO BUILD PROGRAM
--------------------
In order to build this lrc.c program you will need to use the 
makefile that I have included in this repository. The makefile 
compiles our program in which we can play the game. By prompting
"make lrc" into the terminal you will be utilizing the makefile
and be compiling the program. Next in order to actually play the
game you will need to run the command "./lrc" in which the game
actually starts.

HOW TO RUN THE PROGRAM
----------------------
Once we have compiled the program in the previous step we were 
last asked to prompt in "./lrc" into our terminal. By doing so 
we have begun the left right center game. The user will then be
asked to put in a random seed because computers are not good 
when it comes to random generations therefore we utilize the
srandom() command to get us a random seed. It is important to 
note that if you run the same seed everytime you will get the 
same output. Lastly you will be asked to prompt a number of 
players in the program. So you will be asked to put a number
with atleast 2 and at most 14. Then the game shall begin and
you may proceed. Refer to the bottom to see the format.

WHAT TO PUT IN TERMINAL
----------------------
```
make
```
```
./lrc 
```
