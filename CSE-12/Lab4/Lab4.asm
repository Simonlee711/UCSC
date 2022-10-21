#################################################################################
# Created by: Lee, Simon						      	#
# CruzID: siaulee								#
# 16 February 2021								#
#										#
# Assignment: Lab 4: Syntax Checker						#
# CSE 12, Computer Systems and Assembly Language				#
# UC Santa Cruz, Winter 2021							#
#										#
# Description: In this lab you will be feeding the program a txt. file     	#
#	       and it will be checked for a balanced amount of braces		#
#	       brackets, and parantheses. There are a lot of conditions 	#
#	       that need to pass but that will all be accounted for in 		#
#	       the pseudocode.							#			
# Notes: This program is intended to be run from the MARS IDE.			#
#################################################################################

#Pseudocode
#first input some txt files using the program arguments
#there are a few conditions that have to be met: cannot start with integer, & cannot be longer than 20 characters
#next you will open up the file and read the .txt files.
#after doing so we will run through the txt file one by one putting braces, brackets, and parantheses in the stack
#we will have a counter to keep track of the index and will also have counters for the braces, brackets, and parantheses
#if there are mismatches it will indicate where using the push and pop features of the stack
#I will always push however many (, {, [ there are onto the stack 
#I will pop ),},] but if there is nothing to pop there is an error, or if there is still something left on the stack there is an error
#if there are only open braces: (,{,[ and no closing braces, it will tell you that these are on the stack
#a successful run will be if each paranthese, bracket, and brace has an opening and closing (push and pop)
#I will close file 
#I will end program appropriatley

#REGISTER INDEX:
#$a0 - storing the program argument
#$a2 - storing index 0 to be checked whether if its integer or letter
#$t0 - intializing to check if its a number because any number less than 10 is a digit in the first index (0-9)
#$t1 - initializing upper case A to check if its a upper case letter
#$t2 - intializing upper case Z to check if its a upper case letter
#$s1 - initializing lower case a to check if its a lower case letter
#$s2 - initializing lower case z to check if its a upper case letter
#$t1(2) - initializing a maximum limit for a user input through program argument
#$t2(2) - counter for stack pointer to know index
#$t0(2) - counter for determining string length
#$t3(2) - where character is loaded to be compared to see if the rest of the program argument is valid

########################################################################################################################
######## Part1: Checking if Program Argument is Valid Or not ##########################################################  
########################################################################################################################
.data
buffer: .space 128
YouEnteredPrompt: .asciiz "You entered the file:"
InvalidInput: .asciiz "ERROR: Invalid program argument."
SuccessMessage1: .asciiz "SUCCESS: There are "
SuccessMessage2: .asciiz " pairs of braces."
char1open: .byte 0x5B				#ascii hex value for [
char2open: .byte 0x28				#ascii hex value for (
char3open: .byte 0x7B				#ascii hex value for {
char1close: .byte 0x5D				#ascii hex value for ]
char2close: .byte 0x29				#ascii hex value for )
char3close: .byte 0x7D				#ascii hex value for }
leftovers: .asciiz "ERROR - Brace(s) still on stack: "
notbalanced: .asciiz "ERROR - There is a brace mismatch: "
error2message: .asciiz " at index "

.text 
main:
ReadUserInput:

  li $v0 4					#loading register to print string			
  la $a0 YouEnteredPrompt			#printing the prompt
  syscall
  
  li $v0 11					#preparing to print a new line for formality.
  li $a0 0xA					#printing new line
  syscall	
  
  lw $s0 ($a1)					#storing the program argument into the $s0 register 
  move $a0 $s0					#moving the program argument input into $a0 so it can be printed
  li $v0 4					#loading register to print string of characters a.k.a the txt file
  syscall
  
  li $v0 11					#preparing to print a new line for formality.
  li $a0 0xA					#printing new line
  syscall	
  
  li $v0 11					#preparing to print a new line for formality.
  li $a0 0xA					#printing new line
  syscall
  
  jal UserInputCorrectness			#jumping to the next part of the program
  nop
  
UserInputCorrectness:				#this part of the program checks if program argument is valid
  
  lb $a0 0($s0)					#taking index 0 to be checked if it starts with a number or not
  move $a2 $a0					#move value index 0 to register $a2
										
NUMcondition:
#condition if it starts with number
  li $t0 10					#initiallizing value to 10 so if any number is printed 0-9 the program will fail
  ble $t0 $a2 nextCheckLetter			#checking to see if number is less than or equal to zero because program argument cant start with integer
    nop	
    
#if index 0 is a letter jump to next condition if not then check to see if its a number
nextCheckLetter:
  li $t1 0x41					#initializing the range of the a-z & A-Z to identify index 0 as letter
  li $t2 0x5A					#This initializes right of range to Z for range (A-Z)
  li $s1 0x61					#This initializes left of range to a for range (a-z)
  li $s2 0x7A					#This initializes right of range to z for range (a-z)
  
  ble $a2 $t1 errorMessage			# if index 0 is less than hex value 'A' then it is not a letter 
    j Zcheck					# jump to next check to see if it is in range of (A-Z)
    nop
  Zcheck:
  bge $a2 $t2 acheck				#if index 0 is greater than hex value 'Z' then it still can be a letter but not in range (A-Z)
    j NextCondition				#if it is in range check for next condition
    nop
  acheck:
  ble $a2 $s1 errorMessage			#if index 0 is less than hex value 'a' it most definatley not letter
    j zcheck					#jump to see if value is in range (a-z)
    nop
  zcheck:
  bge $a2 $s2 errorMessage			#if index 0 is greater than hex value 'z' there is no way its a letter
   j NextCondition				#if input is valid it will begin to jump to next part of program
   nop
   
errorMessage:
  li $v0 4					#loading register to print string			
  la $a0 InvalidInput				#printing the prompt
  syscall
  
  jal ProgramEnd
  nop
  
NextCondition: 
#check if input is longer than 20 words
  li $t0 1 					# initializing  counter to determine string length starting at 1
  li $t1 21					#initializing max length
  
  stringcountloop:
  addi $s0 $s0 1				# incremement the characters 1 by 1 through the counter loop
  addi $t0 $t0 1				# increment the total count to know how many iterations have gone through
  lb $a0 0($s0)					# taking index 0 to be checked if it starts with a number or not
  move $t3 $a0					# moving index 0 to register $a2 to remain consistent with register index
  beqz $t3 doneLoop 				# check for the null character and if done iterating through string 
  ble $t3 0x2D errorMessage			# If ascii value is below the period there is an error since it shouldn't go between there
  beq $t3 0x2F errorMessage			# error if the ascii value is a / and this confirms that everything is above hex value 0x2F 
  j isNotinRange 					# check next condition of the iteration.
  nop
#########################################################################################3############  
#########checking the leftover characters to see if they are valid A-Z, a-z, number, "_" or ".". #####
######################################################################################################
isNotinRange:
  bge $t3 0x3A isNotinRange2			#if file name character is greater than or equal to hex value : then it is invalid because it is not in range of digit or letter				
  j stringcountloop				# since it is valid jump back to string loop to check next character
  nop
isNotinRange2:
  ble $t3 0x40 errorMessage			#if value is less than hex value @ it is invalid because it is not in range  			
  j Forbiddenrange				#jump to next check to see if it is in another range that wouldn't qualify "[" -> "'"
  nop
Forbiddenrange:
  bge $t3 0x5B Forbiddenrange2			#if file name character is greater than or equal to hex value [ print error 			
  j stringcountloop				# since it is valid jump back to string loop to check next character
  nop
Forbiddenrange2: 			
  ble $t3 0x61 underscoreCheck			# if file name character is less or equal to than hex value "'" then it is in a invalid range 			
  j Forbiddenrange3				# if not jump to the last set of ranges that the characters are not allowed to be
  nop
Forbiddenrange3:	
  bge $t3 0x7B errorMessage			# if file name character is greater than or equal to hex value { then it is in invalid range  
  j stringcountloop				# else it is a valid character
  nop
underscoreCheck:
  beq $t3 0x5F stringcountloop			# if file name character is equal to "_" it is valid and you can add it to the count 
  j errorMessage				# else it is an error
  nop


doneLoop:
  ble $t0 $t1 startProgram			#if the count of characters is less than 20 it can start the program
  j errorMessage				#if program argument is longer than 20 it will end program 
  nop

  
    
########################################################################################################################
######## Part 2: opening and reading files  ############################################################################  
########################################################################################################################

#Register Index for second half of program:
#$s1 - storing program argument to be read 
#$s2 - storing the file descriptor
#$t2 - stores the amount of letters read when traversing through string character by character.
#$s5 - stores the address of the buffer string

startProgram:
#opening file

  lw $s1 ($a1)					# loading .txt file into register $s1 to be 
  move $a0 $s1					# moving .txtfile into register $a0 to be printed
  li $v0 13					# syscall to open file 
  li $a1 0					# flag 0 indicates that file is being read
  li $a2 0					# prompt this to 0 to properly open file
  syscall		
	
  blt $v0 $zero errorMessage			#if it is invalid test file it will display the error message
  move $t0 $v0					#store the file descriptor
  move $s2 $t0					#stores file descriptor into $s2 for later use
  j readFile
  nop
	
readFile:
  move $a0 $s2					#move the file descriptor to begin reading on register $a0
  li $v0 14					#syscall to READ file
  la $a1 buffer					#Use buffer to read certain amount of bytes at a time
  li $a2 1000000 					#hard coded maximum of bytes to read
  syscall
		
  move $t2 $v0					#stores the amount of characters contained in the text file.
  beqz $t2 reRead				#if the file contains no braces, brackets, and parantheses reread buffer and print success message
  move $s5 $a1					#stores the address of the read string in $s5
  
  j checkingCharacter
  nop
  
reRead:
  move $a0 $s2					#move the file descriptor to begin reading on register $a0
  li $v0 14					#syscall to READ file
  la $a1 buffer					#Use buffer to read certain amount of bytes at a time
  li $a2 128 					#hard coded maximum of bytes to read
  syscall
  
  move $t2 $v0					#stores number of characters into register $t2 like the first time
  beqz $t2 Success				#if this buffer is still zero, you can print the success message
  j checkForCondition				#if on this second read you find braces, brackets, or parantheses proceed to checking if they are balanced.
  nop
 
########################################################################################################################
######## Part 3: checking the actual braces on the Stack ###############################################################  
########################################################################################################################

#Register Index for second half of program:
#$s1 - storing program argument to be read 
#$s2 - storing the file descriptor
#$t2 - stores the amount of letters read when traversing through string character by character.
#$s5 - stores the address of the buffer string
#$s0 - contains the first character of the file name 
#$s4 - storing stack address into the address $s4     
#$t0 - counter #1 to see the index of the buffer string
#$t1 - this is loading byte by byte of the buffer string
#$t3 - counter #2 to see whats on the stack
#$t4 - counter #3 to see how many pairs of matching braces, brackets, strings exist
#$t5 - when a brace bracket or paranthases gets stored in the stack the address is held in this register

checkingCharacter:	
  la $s4 ($sp)					#stores base address of the stack pointer in $s2
  li $t0 0					#This is a counter to see where the pointer is in the buffer string
  li $t1 0					#register $t1 is now reading the string byte by byte
  li $t3 0					#counter in the stack is set to 0
  li $t4 0					#the counter to see how many matched braces exist.
  j checkForCondition
  nop
  
  
checkForCondition:
  beqz $t2 checkTheStack			#jumps to CheckTheStack when it has iterated through the whole buffer string
  lb $t1 ($s5)					#loads character(byte by byte) from the address of $s5 which stored the address
  lb $t5 char1open				#load the ascii value [ to register $t5 to be compared
  beq $t1 $t5 PUSH				#if $t1 and char1open are equal then jump to push
  lb $t5 char2open				#load the ascii value ( to register $t5 to be compared
  beq $t1 $t5 PUSH				#if $t1 and char2open are equal then jump to push
  lb $t5 char3open				#load the ascii value { to register $t5 to be compared	
  beq $t1 $t5 PUSH				#if $t1 and char3open are equal then jump to push
  lb $t5 char1close				#load the ascii value ] to register $t5 to be compared
  beq $t1 $t5 checkBracketsBrace		#if $t1 and char1close are equal then jump to parantheses check and if successful will pop
  lb $t5 char2close				#load the ascii value ) to register $t5 to be compared
  beq $t1 $t5 checkParantheses			#if $t1 and char2close are equal then jump to check for braces and brackets then pop
  lb $t5 char3close				#load the ascii value } to register $t5 to be compared
  beq $t1 $t5 checkBracketsBrace		#if $t1 and char3close are equal then jump to check for braces and brackets then pop
						
  j bufferCounter				#if $t1 is not pushed or popped just add to the buffer counter to track buffer index
  nop
  
bufferCounter:
  addi $s5 $s5 1				#add +1 to the string buffer address
  addi $t0 $t0 1				#add +1 to the counter to keep track of the buffer index
  subi $t2 $t2 1				#subtract -1 to the total number of characters read by the buffer to keep organized
  j checkForCondition					
  nop
  
PUSH: 
  addi $sp $sp -8				#decrements stack pointer by 8 to properly store the value
  sb $t5 0($sp)					#Using the stack you can store the parantheses bracket or brace
  sw $t0 4($sp)					#to keep track of the index of the { [ ( that was stored
  addi $t3 $t3 1				#adds +1 to the the amount of objects in the stack
  j bufferCounter				#make sure to increment everything else properly as well
  nop
  
checkParantheses:
  lb $t5 0($sp)					#loads the ascii value to register $t5
  subi $t1 $t1, 1				#since ascii value ) is 0x28. if you subtract -1 you can compare the two values ( & )
  beq $t1 $t5, POP				#if ( == ( then POP the parantheses
  addi $t1 $t1, 1				#if it fails condition revert ascii value incase it needs to be printed: from "(" -> ")" 
  beqz $t3 error2				#this error occurs if there is nothing left on the stack to pop 
  j error3					#this error occurs if there is an actual parantheses mismatch
  nop
		
checkBracketsBrace:				#same thing but a little different since the bracket and brace are seprated by 2 on the ascii table
  lb $t5 0($sp)					#load ascii values from stack pointer to $t5 to get compared
  subi $t1 $t1, 2				#subtract value of ] 0x5D and } 0x7D by 2 to get [ 0x5B and { 0x7D
  beq $t1 $t5, POP				#compare values if they match then POP the value
  addi $t1 $t1, 2				#if not popped revert value to be printed for error
  beqz $t3 error2				#this error occurs if there is nothing left on the stack to pop 
  j error3					#this error occurs if there is an actual brace and bracket mismatch
  nop

checkTheStack:
  bnez $t3, error1 				#will direct you to an error if stuff left on the stack
  j Success					#else it is successful
  nop
 
POP:
  addi $sp, $sp, 8				#adds 8 back to stack pointer 
  subi $t3, $t3, 1				#subtracts 1 on the counter which is tracking [ { ( left on the stack
  addi $t4, $t4, 1				#adds +1 to the matched brace counter so if successful this number can be printed.	
  j bufferCounter				#properly keeping track of index and stuff incase of error.
  nop

########################################################################################################################
######## error 1: no closing brackets, braces, parantheses so the stack is printed###################################### 
########################################################################################################################
error1:
  li $v0 4					#preparing to print string
  la $a0 leftovers				#prints message that tells you that there are still things left on the stack				
  syscall	
  j printTheStack				#print remaining stuff on stack
  nop

########################################################################################################################
######## error 2: brace mismatch. There is a brace mismatch because there is nothing to pop left in the stack ##########
########################################################################################################################
error2:
  li $v0 4					#syscall to print string	
  la $a0 notbalanced				#prints the error message of the unmatched braces
  syscall
		
  move $a0 $t1					#loads the byte with the mismatch to be printed
  li $v0 11					#prints the character brace that is mismatched.
  syscall						

  li $v0 4					#syscall to print string
  la $a0 error2message				#prints the rest of the error message 
  syscall						
		
  move $a0 $t0					#moves the stack pointer index counter to be printed to tell where error occured
  li $v0 1					#syscall to print integer 
  syscall						
		
  j ProgramEnd					#jump to the end of the program
nop

########################################################################################################################
######## error 3: brace mismatch. there is a literal mismatch between braces that occur ################################ 
########################################################################################################################
error3:

  li $v0 4					#loading syscall to print string
  la $a0 notbalanced				#print error message
  syscall
		
  move $a0 $t1					#moving the character in that byte to register $a0 to be printed 
  li $v0 11					#prints one of the brace bracket or parantheses that are mismatched
  syscall
		
  li $v0 4					#syscall to print string
  la $a0 error2message				#prints the second part of the error message 				
  syscall			
		
  li $v0 1					#syscall to print integer
  move $a0 $t0					#moves index counter to $a0 to print where the error actually occured
  syscall			
		
  j ProgramEnd
  nop

########################################################################################################################
######################################################################################################################## 
########################################################################################################################


printTheStack:
  beqz $t3 ProgramEnd				#checking to see if stack is empty. if empty end program
  lw $t5 0($sp)					#loads the leftover brace, bracket or parantheses from the stack	
  move $a0 $t5					#moving register $t5 to $a0 so remaining braces can be printed
  li $v0, 11					#prints brace, bracket, and/or parantheses
  syscall
		
  addi $sp, $sp, 8				#incrementing the next character to be printed if there are any left on the stack
  subi $t3, $t3, 1				#decrements number of braces brackets and parantheses still left on the stack
		
  j printTheStack				#loops until stack is at zero
  nop
  

Success:
  li $v0 4					#syscall to print string
  la $a0 SuccessMessage1			#prints the first part of the success message "SUCCESS: There are "					
  syscall			
		
  move $a0 $t4					#the counter for amount of balanced braces is moved to $a0 to prepare for printing
  li $v0 1					#prints integer number of matched braces 
  syscall
		
  la $a0 SuccessMessage2			#syscall to print remainder of string success message
  li $v0 4					#prints the second half of the success message " pairs of braces."
  syscall	
  
  jal ProgramEnd				#jumping to the ending program
  nop
  

ProgramEnd:					
  move $a0, $s2					#moving file descriptor back to $a0
  li $v0, 16					#syscall used to close file properly
  syscall
  
  li $v0 11					#preparing to print a new line for formality.
  li $a0 0xA					#printing new line
  syscall	

  li $v0 10					#syscall to properly end the program
  syscall 					




