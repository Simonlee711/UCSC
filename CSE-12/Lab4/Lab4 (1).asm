#header:
#Lab4.asm
#by Rohit Cheruku 
#student id: rkcheruk
#checks if braces are matched
#############################################################################
#				pseudocode				    #
#program .data section defines all used labels
#.main:
#	print user input
#	check user input for validity
#	open_file	
#		if file not found(print error)
#	read_file
#		read content and store contents in buffer
#	next2
#		sets registers to desired value
#	check_brace
#		checks each brace and determines to push or pop
#		if (number of character in buffer == 0)
#			check stack to see if there are braces left
#		else(print stack)
#		if open brace -> push
#		if closed brace -> checkBrace 1 or 2
#			checkBrace 1 or 2
#				if mismatch -> print error
#				else-> print success
#	push
#		decrements stack pointer
#		increment buffer index
#		store byte and index
#		increments stack counter
#	pop	
#		increments stack pointer
#		decrements stack counter
#	Errors 1-4
#		prints error message depending on error
#	success	
#		prints success message if all requirements are met
#	exit
#		closes file
##		exits program

.data
	buffer  :	.space 128			#buffer
	space	:	.asciiz " "
	prompt1 : 	.asciiz "You entered the file: \n"#
	ifSuccess1:	.asciiz "SUCCESS: There are "
	ifSuccess2:	.asciiz " pairs of braces."
	stackBraces:	.asciiz "ERROR - Brace(s) still on stack: "
	mismatch:	.asciiz "ERROR - There is brace a mismatch: "
	at_index:	.asciiz " at index "
	newline : 	.asciiz "\n"			#
	Invalid :	.asciiz "ERROR - Invalid program argument."
	openb1  :	.byte 40			#ascii code for (
	openb2	:	.byte 91			#ascii code for [
	openb3	:	.byte 123			#ascii code for {
	closedb1:	.byte 41			#ascii code for )
	closedb2:	.byte 93			#ascii code for ]
	closedb3:	.byte 125			#ascii code for }
.text
main:
	la $a0, prompt1					#prints first prompt
	li $v0, 4
	syscall
	
	lw $t0, ($a1)					#loads word(program arguments) at address $a1 into $t0
	move $a0,$t0					#moves $t0 to $a0 to print
	li $v0, 4
	syscall						
		
	#jal print_newline				#prints newline
	jal print_newline				#prints newline
		
	#check to make sure first character in program arguments is valid
	## $t0 = loads byte at $t6 and checks inequalities for ascii code
	## $t1 = counter for number of characters in program argument. (cannot exceed 20)
	## $t3 = load word from address at $a1
	## $t4 = contains value of characters that were read from file
	## $t6 = contains the word stored at address $a1
	## $a1 = contains address of program arguments
	## $s0 = stores address of buffer string in $s0
	## $s6 = contains the file descriptor for later use
	
	lw $t6, ($a1)			#t6 has the word in the program argument
	check1:
		lb $t0, ($t6)
		ble $t0, 64, error1	#checks if number
		j check2
	check2:
		bge $t0, 123, error1	#checks end of ascii code
		j check3
	check3: 
		bge $t0, 91, check4	# checks in between A-Z and a-z
		li $t1, 0
		j loop1
	check4:
		ble $t0, 96, error1	# checks in between A-Z and a-z
		li $t1, 0
		j loop1
	error1:
		jal print_newline	#prints newline
		
		la $a0, Invalid
		li $v0, 4 		#prints invalid file name statement
		syscall 
		
		j exit			#exit
		
		#loops for checking the remaining bytes in the program argument
	loop1:
		addi $t1, $t1, 1	#increments counter
		addi $t6, $t6, 1	#increment on string
		lb $t0, ($t6)		#load byte from $t6 into $t0
		beqz $t0, next1		#check if $t0 == 0   checks for null terminating character
		ble $t0, 45, error1	#everything under period "."
		beq $t0, 47, error1	#ascii above period
		j loop2
	loop2:
		bge $t0, 58, loop7		#check if $t0 >= 58
		j loop1
	loop3:
		bge $t0, 91, loop4		#check if $t0 >= 91
		j loop1
	loop4: 
		ble $t0, 97, loop5		#check if $t0 <= 97
		j loop6
	loop5:
		beq $t0, 95, next1		#check if $t0 == 95  this is for "_"
		j error1
	loop6:	
		bge $t0, 123, error1		#check if $t0 >= 123
		j loop1
	loop7:
		ble $t0, 64, error1		#if its ascii code between numbers and capital letters
		j loop3
	next1:
		bgt $t1, 20, error1		#checks if file name is too long	
		
		j open_file
		
	#####################################################################################
	#### 			opening and reading from file				#####
	
	open_file:
		lw $t3, ($a1)			#load address of a1 into t3
		move $a0, $t3			#move address into a0
		li $a1, 0			#set flags to 0
		li $a2, 0			#set mode to 0
		li $v0, 13			#syscall code for OPEN file
		syscall
		blt $v0, $zero, error1		#jumps to error if test file is not found
		move $t0, $v0			#store the file descriptor
		move $s6, $t0			#stores file descriptor for later use
		j read_file
		
	read_file:
		move $a0, $s6			#move file descriptor into $a0
		la $a1, buffer			#address of input buffer
		li $a2, 128 			# max number of bytes to read
		li $v0, 14			#syscall code to READ file
		syscall
		
		move $t4, $v0			#stores number of characters read
		beqz $t4, read_again		#if there are no braces, prints "SUCCESS - There are 0 pairs of braces"
		move $s0, $a1			#stores address of buffer string in $s0
		
		jal print_newline		
		
		j next2				#jumps to next
	#####################################################################################
	#### 			iterating through the string buffer			#####
	
	#iterates through string buffer
	## $s0 = contains address of string buffer
	## $s2 = contains base address of stack pointer
	## $t0 = loads each byte from address pointing to each byte of buffer string
	## $t1 = address of labels for each bracket
	## $t2 = counter for index on string buffer
	## $t4 = contains value of characters that were read from file
	## $t5 = counter for braces in stack
	## $t6 = contains the word stored at address $a1
	## $t7 = address for brace index array. stores index of each brace using memory offset
	## $t8 = count for matched braces
	
	next2:	
		la $s2, ($sp)			#stores base address of stack in $s2
		li $t2, 0			#sets counter $t2 to 0. Counter for index in string buffer
		li $t0, 0			#resets $t0 to 0
		li $t5, 0			#sets stack counter to 0
		li $t8, 0			#sets matched brace count to 0
		j check_brace
	
	check_brace:
		beqz $t4, check_stack		#exits if number of characters in buffer gets to 0
		lb $t0, ($s0)		#loads byte(character) at address of $s0
		lb $t1, openb1		
		beq $t0, $t1, push	#if $t0 == openb1 then jump to push
		lb $t1, openb2
		beq $t0, $t1, push	#if $t0 == openb2 then jump to push
		lb $t1, openb3
		beq $t0, $t1, push	#if $t0 == openb3 then jump to push
		lb $t1, closedb1
		beq $t0, $t1, check_brace1	#if $t0 == closedb1 then jump to pop
		lb $t1, closedb2
		beq $t0, $t1, check_brace2	#if $t0 == closedb2 then jump to pop
		lb $t1, closedb3
		beq $t0, $t1, check_brace2	#if $t0 == closedb3 then jump to pop
		
		j increment_buffer	#if $t0 is not a brace, increment buffer
		
		
	push:	
		subi $sp, $sp, 8	#decrements stack pointer by 8(byte)
		sb $t1, 0($sp)		#stores brace in stack
		sw $t2, 4($sp)		#stores index
		addi $t5, $t5, 1	#increments counter for stack items
		j increment_buffer
		
	increment_buffer:
		addi $s0, $s0, 1	#increments address of string buffer
		addi $t2, $t2, 1	#increments index counter on string buffer
		subi $t4, $t4, 1	#decrements total number of characters read from file
		j check_brace
	
	pop:
		addi $sp, $sp, 8	#increments stack pointer
		subi $t5, $t5, 1	#decrements stack counter
		addi $t8, $t8, 1	#increments matched brace counter
		
		j increment_buffer	
		
	check_brace1:
		lb $t1, 0($sp)		#loads ascii code from stack
		subi $t0, $t0, 1	#if $t0 is 41 ")", it subtracts to 40 to match opening brace "("
		beq $t0, $t1, pop	#check to see if braces match
		addi $t0, $t0, 1	#sets $t0 back to original ascii value
		beqz $t5, error3	#if stack count is 0 and there is a closing brace
		j error2
		
	check_brace2:
		lb $t1, 0($sp)		#loads ascii code from stack
		subi $t0, $t0, 2	#if $t0 = 93 or 125, it subtracts to 91 or 123 respectively to match "[" or "{"
		beq $t1, $t0, pop	#if braces match, then pop
		addi $t0, $t0, 2	#sets $t0 back to original ascii value
		beqz $t5, error3	#if stack count is 0 and there is a closing brace
		j error2
		
	error2:
		la $a0, mismatch
		li $v0, 4		#prints "ERROR - There is a brace mismatch: "
		syscall
		
		move $a0, $t1
		li $v0, 11		#prints the opening brace that is mismatched
		syscall
		
		la $a0, at_index
		li $v0, 4		#prints "at index "
		syscall
		
		lb $t1, 4($sp)		#loads index number
		move $a0, $t1
		li $v0, 1		#prints index integer
		syscall
		
		la $a0, space
		li $v0, 4		#prints a space
		syscall
		
		move $a0, $t0
		li $v0, 11		#prints character close brace
		syscall
		
		la $a0, at_index
		li $v0, 4		
		syscall			#prints "at index "
		
		move $a0, $t2		#moves index on buffer to $a0
		li $v0, 1
		syscall			#prints index as integer
		
		j exit
	
	error3:
		la $a0, mismatch
		li $v0, 4		#prints "There is a brace mismatch: "
		syscall
		
		move $a0, $t0
		li $v0, 11		#prints character close brace
		syscall
		
		la $a0, at_index
		li $v0, 4		
		syscall			#prints "at index "
		
		move $a0, $t2		#moves index on buffer to $a0
		li $v0, 1
		syscall			#prints index as integer
		
		
		j exit			#exits
	
	error4:
		la $a0, stackBraces
		li $v0, 4		#prints "Braces still on stack: "
		syscall
		
		j print_stack
		
	print_stack:
		beqz $t5, exit		#checks if stack is empty
		lw $t1, 0($sp)		#loads brace from stack
		
		move $a0, $t1
		li $v0, 11		#prints brace
		syscall
		
		addi $sp, $sp, 8	#increments stack
		subi $t5, $t5, 1	#decrements number of braces on stack
		
		j print_stack		#loops until $t5 == 0
	
	check_stack:
		bnez $t5, error4
		j success			#reads again if stack is empty
	
	read_again:
		move $a0, $s6			#move file descriptor into $a0
		la $a1, buffer			#address of input buffer
		li $a2, 128 			# max number of bytes to read
		li $v0, 14			#syscall code to READ file
		syscall
		
		move $t4, $v0			#saves number of characters read
		beqz $t4, success		#if next buffer is 0, then success
		j check_brace			# jumps to check brace if there are more contents
	success:
		la $a0, ifSuccess1
		li $v0, 4		#prints "SUCCESS: There are "
		syscall			
		
		move $a0, $t8
		li $v0, 1		#prints number of matched braces 
		syscall
		
		la $a0, ifSuccess2
		li $v0, 4		#prints " pairs of braces."
		syscall
		
		j exit
	##procedure for printing newline
	print_newline:
		la $a0, newline
		li $v0, 4
		syscall
		jr $ra
		
	##exit procedure
	exit:
		jal print_newline
		move $a0, $s6		#moves file descriptor into $a0
		li $v0, 16		#close file
		syscall	
		
		li $v0, 10
		syscall			#syscall for exit program
		jr $ra				
		
