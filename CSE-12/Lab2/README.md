# Lab 2


- Simon Lee (1724877)

- Winter 2021

- Lab 2 is a lab using MMLogic software, where we want to transfer bits of data throughout a sequential logic circuit. This lab demonstrates how we can transfer a hexadecimal number from a keypad to a group of 4 registers, which then moves to an ALU input which then performs an arithmetic left shift which is the new ALU output. This new output is then used as feedback to the 2 to 1 multiplexor which can now take the ALU result or the keypad. Then this sequence is repeated.

- Lab2.lgi

- This lab relies heavily on the keypad, the Read Register Address 1 & 2, the Write register address, the store select, update register, and clear register which are all parts that can be manipulated during this lab. The ALU result or the keyboard is what value gets transferred to the 4 registers which are then transferred to the ALU inputs, which then perform the arithmetic left shift, and the ALU output as mentioned earlier becomes feedback which goes back to the 2 to 1 multiplexor which then repeats the described action.
