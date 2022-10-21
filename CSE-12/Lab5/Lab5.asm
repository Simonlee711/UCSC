#################################################################################
# Created by: Lee, Simon						      	#
# CruzID: siaulee								#
# 12 March 2021									#
#										#
# Assignment: Lab 5: Functions and Graphics					#
# CSE 12, Computer Systems and Assembly Language				#
# UC Santa Cruz, Winter 2021							#
#										#
# Description: In this lab you will be drawing on a 128 x 128 bitmap display.   #
#	       There is a specific pattern which will be drawn using the 	#
#	       lab5_w21_test.asm file. This file is responsible for drawing the #
#	       pattern and we are responsible for completing the subroutines &  #
#	       the macros to make this 128 x 128 image run properly.		#
#	      									#			
# Notes: This program is intended to be run from the MARS IDE.			#
#################################################################################
#PSEUDOCODE:
#There will be a series of tests that will take place
#First in the clear_bitmap which will paint the whole bitmap display to a sea green.
#	this will be done by calling the top left most bit 0xffff0000 and putting the sea green color value until 0xfffffffc which the bottom right bit
#second we will print a horizontal line 
#	this will get the address and mutiply it by 128 so you can print on the right row. there is a counter so it knows when to stop printing
#third will print a vertical line. 
#	This one is a little different in which you will add the XX value to find the right column to print. multiply
#	by 4 since all addresses are 4 bytes apart and add 128 in a loop so it prints on only that column. 
#	there is a counter in place so it knows when your done with the column
#lastly you will print a crosshair that uses both vertical and horizontal line functions
#	first you will find the color address and store into register $s4
#	next you will print the horizontal line as described in the second part of the function
#	next you will print the vertical line as described in the third part of the function
#	lastly you will used the equation output = origin + 4 * (x + 128 * y) to find the location of where to revert the color at the intersection
#your program is complete and the drawing is done!

# Winter 2021 CSE12 Lab5 Template
######################################################
# Macros for instructor use (you shouldn't need these)
######################################################

# Macro that stores the value in %reg on the stack 
#	and moves the stack pointer.
.macro push(%reg)
	subi $sp $sp 4
	sw %reg 0($sp)
.end_macro 

# Macro takes the value on the top of the stack and 
#	loads it into %reg then moves the stack pointer.
.macro pop(%reg)
	lw %reg 0($sp)
	addi $sp $sp 4	
.end_macro

#################################################
# Macros for you to fill in (you will need these)
#################################################

# Macro that takes as input coordinates in the format
#	(0x00XX00YY) and returns x and y separately.
# args: 
#	%input: register containing 0x00XX00YY
#	%x: register to store 0x000000XX in
#	%y: register to store 0x000000YY in
.macro getCoordinates(%input %x %y)					
#store x-value
	srl %x %input 16						#right logical shift by 16 bits which will leave 0x000000XX left
#store y-value
	addi %y %input 0						#adds 0 to input to put into y
	andi %y %y 0x000000FF						#no shift required just compare using bitwise AND operand to obtain coordinate y
 
	
.end_macro

# Macro that takes Coordinates in (%x,%y) where
#	%x = 0x000000XX and %y= 0x000000YY and
#	returns %output = (0x00XX00YY)
# args: 
#	%x: register containing 0x000000XX
#	%y: register containing 0x000000YY
#	%output: register to store 0x00XX00YY in
.macro formatCoordinates(%output %x %y)
	la %output (%x)							#loads address of %x into %output
	sll %output %output 16						#unlike getCoordinate it does the opposite and perfroms a left logical shift by 16
	add %output %output %y						#adds %y to the output to get it back into the format 0x00XX00YY
.end_macro 

# Macro that converts pixel coordinate to address
# 	output = origin + 4 * (x + 128 * y)
# args: 
#	%x: register containing 0x000000XX
#	%y: register containing 0x000000YY
#	%origin: register containing address of (0, 0)
#	%output: register to store memory address in
.macro getPixelAddress(%output %x %y %origin)
  lw $t1 originAddress							# register $t1 containing origin address
  getCoordinates($a0 $t2 $t3)						# getting the coordinates x and y at which to draw
  mul $t4 $t3 128							# multiply register $t3 by 128 which is the row size to get to the proper row to draw pixel
  add $t4 $t4 $t2							# add register $t2 to get to the column at which you want to draw
  mul $t4 $t4 4								# remember that registers are 4 bytes apart so you need to multiply by 4
  add $t4 $t4 $t1							# finally add the hex digit to get to proper address
  sw $a1 ($t4)								# store the color that is supposed to go into the address to color
.end_macro


.data
originAddress: .word 0xFFFF0000

.text
# prevent this file from being run as main
li $v0 10 
syscall

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Subroutines defined below
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#*****************************************************
# Clear_bitmap: Given a color, will fill the bitmap 
#	display with that color.
# -----------------------------------------------------
# Inputs:
#	$a0 = Color in format (0x00RRGGBB)
#	$t1 = the address of the start of the Bitmap
#	$t2 = the address of the end of the bitmap
# Outputs:
#	No register outputs
#*****************************************************
clear_bitmap: nop
  lw $t1 originAddress						#the start address
  li $t2 0xFFFFFFFC						#the end address
  j clearTheLoop
clearTheLoop:
  beq $t1, $t2, endTheLoop					#if register $t1 and $t2 are equal end loop. else store 0x00RRGGBB values into specific memory addresses
  sw $a0, ($t1)							#storing the value into the memory.
  addi $t1, $t1, 4						#add 4 bytes to memory address
  j clearTheLoop
endTheLoop:
   jr $ra

#*****************************************************
# draw_pixel: Given a coordinate in $a0, sets corresponding 
#	value in memory to the color given by $a1
# -----------------------------------------------------
#	Inputs:
#		$a0 = coordinates of pixel in format (0x00XX00YY)
#		$a1 = color of pixel in format (0x00RRGGBB)
#		$t1 = holds originalAddress or starting address 
#		$t2 = XX or column coordinate
#		$t3 = YY or row coordinate
#		$s4 = bitmap Display Address
#	Outputs:
#		No register outputs
#*****************************************************
draw_pixel: nop
  lw $t1 originAddress						# starts to draw at first pixel
  getCoordinates($a0 $t2 $t3)					# getting the coordinates x and y at which to draw
  mul $s4 $t3 128						# multiply register $t3 by 128 which is the row size to get to the proper row to draw pixel
  add $s4 $s4 $t2						# add register $t2 to get to the column at which you want to draw
  mul $s4 $s4 4							# remember that registers are 4 bytes apart so you need to multiply by 4
  add $s4 $s4 $t1						# finally add the hex digit to get to proper address
  sw $a1 ($s4)							# store the color that is supposed to go into the address to color
  jr $ra
	
#*****************************************************
# get_pixel:
#  Given a coordinate, returns the color of that pixel	
#-----------------------------------------------------
#	Inputs:
#		$a0 = coordinates of pixel in format (0x00XX00YY)
#		$a1 = color of pixel in format (0x00RRGGBB)
#		$t1 = holds originalAddress or starting address 
#		$t2 = XX or column coordinate
#		$t3 = YY or row coordinate
#		$t4 = bitmap Display Address
#	Outputs:
#		Returns pixel color in $v0 in format (0x00RRGGBB)
#*****************************************************
get_pixel: nop
  lw $t1 originAddress						# start at first pixel as always
  getCoordinates($a0 $t2 $t3)					# repeat process from drawPixel and get coordinate
  mul $t4 $t3 128						# multiply YY to get proper row
  add $t4 $t4 $t2						# add XX to get to proper column
  mul $t4 $t4 4							# multiply by 4 again because they addresses are 4 bytes apart 
  add $t4 $t4 $t1						# add number from $t1 to $t4 to get to the proper address 
  lw $v0 ($t4)							# load the color into reister $v0 
  jr $ra

#*****************************************************
# draw_horizontal_line: Draws a horizontal line
# ----------------------------------------------------
# Inputs:
#	$a0 = y-coordinate in format (0x000000YY)
#	$a1 = color in format (0x00RRGGBB)
#	$t0 = origin address 0xFFFF0000
#	$t1 = XX coordinates
#	$t2 = YY coordinates
#	$t3 = bitmap display address
#	$t4 = counter for how long a horizontal line should be a.k.a 128 bits
#	$s5 = holds stack pointer
#	$s0 = holds coordinate
#	$s1 = holds color
# Outputs:
#	No register outputs
#*****************************************************
draw_horizontal_line: nop

  push($ra)
  push($t1)
  push($t2)
  push($s0)
  push($s1)
  push($s5)
  move $s5 $sp
  move $s0 $a0
  move $s1 $a1
  lw $t0 originAddress						#the start address
  getCoordinates($a0 $t1 $t2)					#getting the coordinates
  
  mul $t3 $t2 128						#multiply the YY value to get to right row
  mul $t3 $t3 4
  add $t3 $t3 $t0						#add that value with the origin address to get in right position
  li $t4 128							#counter for 128 bits				
  j printlineloop
printlineloop:
  sw $s1 ($t3)							#store color to be printed in address
  addi $t3 $t3 4 						#add 4 to memory addresses
  addi $t4 $t4 -1						#subtract -1 from the 128 counter
  bnez $t4 printlineloop					#if $t4 is not zero keep storing color in new bit
  move $sp $s5
  pop($s5)
  pop($s1)
  pop($s0)
  pop($t2)
  pop($t1)
  pop($ra)
  jr $ra


#*****************************************************
# draw_vertical_line: Draws a vertical line
# ----------------------------------------------------
# Inputs:
#	$a0 = x-coordinate in format (0x000000XX)
#	$a1 = color in format (0x00RRGGBB) 
#	$t0 = origin address 0xFFFF0000
#	$t1 = XX coordinates
#	$t2 = YY coordinates
#	$t3 = bitmap display address
#	$t4 = counter for how long a horizontal line should be a.k.a 128 bits
#	$s5 = holds stack pointer
#	$s0 = holds coordinate
#	$s1 = holds color
# Outputs:
#	No register outputs
#*****************************************************
draw_vertical_line: nop
  push($ra)							#push all values
  push($t1)							#pushing $t1
  push($t2)							#pushing $t2
  push($t3)							#pushing $t3
  push($s0)							#pushing $s0
  push($s1)							#pushing $s1
  push($s5)							#pushing $s5
  push($s3)							#pushing $s3
  move $t3 $s3
  move $s5 $sp
  move $s0 $a0
  move $s1 $a1
  move $t2 $s3
  move $t1 $s2
  
  la $t0 0xffff0000						#the start address
  getCoordinates($a0 $t1 $t2)					#getting the coordinates
  add $t3 $t3 $t1						#adds XX to the bitmap display address
  mul $t3 $t3 4							#need to multiply by 4 since addresses are separated by 4bytes
  add $t3 $t3 $t0						#add the column location to the origin Address 0xFFFF0000
  li $t4 128							#counter for the printing the column
  j vertline
vertline:
  sw $s1 ($t3) 							#print color in address
  add $t3 $t3 512						#Not sure why but it won't print whole column unless its 512
  addi $t4 $t4 -1						#decrement counter
  bnez $t4 vertline						#if counter does not reach zero keep putting color into addresses
  move $sp $s5							#move stack pointer back
  move $s3 $t3						
  pop($s3)
  pop($s5)
  pop($s1)
  pop($s0)
  pop($t3) 
  pop($t2)
  pop($t1)
  pop($ra)
  jr $ra


#*****************************************************
# draw_crosshair: Draws a horizontal and a vertical 
#	line of given color which intersect at given (x, y).
#	The pixel at (x, y) should be the same color before 
#	and after running this function.
# -----------------------------------------------------
# Inputs:
#	$a0 = (x, y) coords of intersection in format (0x00XX00YY)
#	$a1 = color in format (0x00RRGGBB) 
#	$s0 = coordinate holder 
#	$s1 = color address holder
#	$s2 = XX coordinate
#	$s3 = YY coordinate
#	$s4 = bitmap display address
#	$s5 = stack pointer holder
#	$s7 = original address holder 
# Outputs:
#	No register outputs
#*****************************************************
draw_crosshair: nop
	push($ra)
	push($s0)
	push($s1)
	push($s2)
	push($s3)
	push($s4)
	push($s5)
	move $s5 $sp							#move $sp which is the stack pointer to $sp
	move $s0 $a0  # store 0x00XX00YY in s0				#store coordinate in $s0
	move $s1 $a1  # store 0x00RRGGBB in s1				#store color address in $s1
	la $s7 originAddress
	getCoordinates($s0 $s2 $s3)  					# store x and y in s2 and s3 respectively
	mul $s4 $s3 128							# multiply register $t3 by 128 which is the row size to get to the proper row to draw pixel
  	add $s4 $s4 $s2							# add register $t2 to get to the column at which you want to draw
 	mul $s4 $s4 4							# remember that registers are 4 bytes apart so you need to multiply by 4
 	add $s4 $s4 $s7							# finally add the hex digit to get to proper address
 	lw $s1 ($s4)
	
	# get current color of pixel at the intersection, store it in s4
	move $s4 $s1							#move the color stored into register $s4 like described
	
	# draw horizontal line (by calling your `draw_horizontal_line`) function
	jal draw_horizontal_line					#calls horizontal line function

	# draw vertical line (by calling your `draw_vertical_line`) function
	li $s3 0							#reset address to 0 before drawing vertical line
	jal draw_vertical_line						#calls vertical line function
	
	# restore pixel at the intersection to its previous color
	la $a1 0x003cb371						#hard coded value for green
	getCoordinates($s0 $s2 $s3)  					# store x and y in s2 and s3 respectively
	mul $s4 $s3 128							# multiply register $t3 by 128 which is the row size to get to the proper row to draw pixel
  	add $s4 $s4 $s2							# add register $t2 to get to the column at which you want to draw
 	mul $s4 $s4 4							# remember that registers are 4 bytes apart so you need to multiply by 4
 	add $s4 $s4 $s7							# finally add the hex digit to get to proper address
 	sw $a1 ($s4)							#store the green pixel at address for intersection
	jal draw_pixel							#call to print on bitmap display.
	
	
	move $sp $s5							#move stack pointer back to register $sp from $s5
	pop($s5)
	pop($s4)
	pop($s3)
	pop($s2)
	pop($s1)
	pop($s0)
	pop($ra)
	jr $ra
