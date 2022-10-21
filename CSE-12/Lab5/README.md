Simon Lee
siaulee
Winter 2021
Lab 5: Functions & Graphics

-----------------------
DESCRIPTION
-This lab is our third one used on the MARS program. This one was not as complex in my opinion but very new in which we got to experience how to use a 128 x 128 bitmap display. So in this lab we are using a test file that gives us a set of instructions and we are instructed to code some macros, and subroutines, so then these instructions can be properly run. After each test they will give out what color address should be printed, and what color address you printed. If the addresses match as they expect you to, then you know you properly did the code. In the instructions we are asked to draw a green background followed by a yellow horizontal line, followed by a red vertical line, and finally asked to draw an indigo crosshair. If all are drawn and all memory addresses match you succeeded. Congrats you have finished all the labs in CSE 12!!! :)  
-----------------------
FILES

Lab5.asm
This file includes the MIPS assembly code which was made in design of the description
lab5_w21_test.asm
This file includes the MIPS assembly code which is supposed to test our program output


-----------------------
INSTRUCTIONS

As previously mentioned this program is run on (MARS). For this lab to run you first need to open both your Lab5.asm and the lab5_w21_test.asm which is the set of instructions for your program. Next you will need to be under the test program and click in the top section "tools". Under "tools" you will find "bitmap display" as your second option and you click that. Next you want to set the settings of the bitmap display. The lab is meant to be loading 1 pixel by 1 pixel on a 128 bit x 128 bit bitmap display. You also need to set the memory address to come from 0xffff0000 (which is the memory map). (You can also play around with the 4 x 4 pixels and the 512 x 512 bitmap so you can see your drawing a little bigger thanks to proportions.) Anyway lastly you assemble and your image should be drawn shortly. Congrats you are finished with CSE 12 Labs!!! :)