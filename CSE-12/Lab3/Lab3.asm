#################################################################################
# Created by: Lee, Simon	`					      	#
# CruzID: siaulee								#
# 6 February 2021								#
#										#
# Assignment: Lab 3: ASCII-risks (Asterisks)					#
# CSE 12, Computer Systems and Assembly Language				#
# UC Santa Cruz, Winter 2021							#
#										#
# Description: This program prints a triangle based on the number you input  	#
#              The number is displayed sort of in a pyramind sequence where 	#
#	       once you hit the number it will once again decrememnt. 		#
#              Ex: 1 2 3 4 3 2 1.						#
#  	       However only the highest number in the pyramid sequence will 	#
#              be printed and the rest of the numbers will be represented	#
#              by asteriks "*". that spaces in between the asteriks and		#
#              numbers are represented by "tabs"				#
#										#
# Notes: This program is intended to be run from the MARS IDE.			#
#################################################################################


#PSEUDOCODE: 
#main:
#userInput - inputs a number above 0
#if userInput < 0 then it will rerun the sequence until appropritate input is enetered
#   also will print an invalid message
#   
#else they have enetered a valid input:
#   and it will continue the program 
#
# Next we initialize 1 so then 1 is the first value printed. 
# We also initialize 1 into another register to indicate number of stars printed.
#
# the first for loop will be in charge of printing everything
#   the second for loop will be printing first sequence of asteriks and tabs
#     then we will print the number in its appropriate index
#        the third for loop will be printing tabs and asteriks on the second sequence
#
# we will repeat this sequence until the first for loops sequence are met
#
# once the first for loops conditions are met it will prompt the end of the program


#REGISTERS INDEX
#$t1 - inital value - 1 used for the big for loop.
#$t2 - storing user input (integer)
#$t3 - initial value 1. Used for printing certain amount of asteriks.
#$v0 - used to prep certain syscalls
#$a0 - used for actual printing reserved to the assembler


.text
main:
#input
startInput: 				#will restart if user input is invalid
    li $v0 4				#syscall for printing string
    la $a0 questionPrompt		#pointing to label "question" which will display the question.
    syscall
  
#user input being read
  
    li $v0 11				#prepping to print character
    li $a0 0x9				#printing a tab to follow the lab format
    syscall
  
    li $v0, 5				#reading user input for integer				
    syscall
    move $t2, $v0			#moving value from register $v0 to $t2

#checking to see if input is valid
blez $t2 errorMessage			#checking to see if number is less than or equal to zero
    j initialCondition			#if input is valid it will begin to jump to next part of program
    nop					

#error message
errorMessage:				#if user input is incorrect it will jump to this label
    li $v0 4				#prepping to print string
    la $a0 invalidInput			#will print Invalid input message
    syscall

    li $v0 11				#preparing to print a new line for formality.
    li $a0 0xA				#printing new line
    syscall

j startInput				#after printing new line it will once again prompt you to put valid input
nop


initialCondition:
li $t1 1				#loading an initial value 1 for the most outer for loop

#conditional statement (for loop)	
loopRestart:				# wrote this in to reroute the loop since everything is manual
    li $t3 1 				#loading initial value for asterik and tab printing
    bgt $t1 $t2 WhenDoneFunction	#branch function taking initial value and value being read.
    j starLoop				#jumping to printing the asteriks and tabs in for the left side

#printing first sequence of * 			
    starLoop:				#need to create a variable to jump back up to simulate iterations.
        beq $t3 $t1 continueLoop 	#if branch equals incremented number then move to next part. if it doesn't print characters below
        li $v0 11			#prepping to print character
        li $a0 0x2A			#printing asterik
        syscall
        
        li $v0 11			#prepping to print characater
        li $a0 0x9			#printing a tab 	
        syscall
        
        addi $t3 $t3 1			#increment by 1
        
    j starLoop				#reiterate loop if condition is not met
    nop

#number being printed       
continueLoop:   
    li $t3 1				#re-initializing the value for the asteriks printed on the right side
    move $a0 $t1			#moving the iterated value to $a0 to be printed 
    li $v0 1				#preparing register to print the current iterated integer
    syscall
  
    j starLoop2				#we will now begin printing tabs and asteriks on the right side (tabs first. asteriks second)
    nop
    
#printing second sequence of *
    starLoop2:
    beq $t3 $t1 finishLoop	 	#same concept as star loop . if equal proceed. if not print asterik and tab
        
        li $v0 11			#prepping to print characater
        li $a0 0x9			#printing a tab. this is important because if we printed asterik the number and asterik would be touching 	
        syscall
        
        li $v0 11			#prepping to print character
        li $a0 0x2A			#printing asterik. The order is flip flopped because of explanation above. dont want number and asterik touching
        syscall
        
        addi $t3 $t3 1			#increment by 1 so then it performs like a for loop. once equal to the iterated value it will be proceed to the end of the sequence.
        
    j starLoop2				#reiterate loop if condition is not met
    nop

finishLoop:
    li $v0 11				#preparing to print a new line so each integer is printed on their own line.
    li $a0 0xA				#new line
    syscall
     
#increment feature of loop first loop
    addi $t1 $t1 1			# incrementing the loop by +1 for the next iteration. Notice that this increment is not the same as the starloop incrememnts.
   
j loopRestart 				#rerun the iteration  
nop


#properly ends program
WhenDoneFunction:			#when first for loops conditions are met, the final syscall is to end program appropriately
    li $v0, 10				#Exit Program
    syscall

.data 
questionPrompt: .asciiz "Enter the height of the pattern (must be greater than 0):"
invalidInput: .asciiz "Invalid Entry!"



