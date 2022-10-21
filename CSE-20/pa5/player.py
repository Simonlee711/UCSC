# author: Simon Lee
# date: December 10,2020
# file: tictac.py a Python program that implements a tic-tac-toe game
# input: user responses (strings)
# output: interactive text messages and a tic-tac-toe board

class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
      def get_sign(self):
            return self.sign
      def get_name(self):
            return self.name
      def choose(self, board):
            while True:
                  cell = input(self.name +", " + self.sign + ": Enter a cell [A-C][1-3]: ").upper()
                  if cell in ("A1","A2","A3","B1","B2","B3","C1","C2","C3"):
                        if board.isempty(cell): 
                              board.set(cell, self.sign)
                              break
                        else:
                              print("You did not choose correctly.")
                              continue
                  else:
                        print("You did not choose correctly.")
                        continue
                  
                        
                  
            # prompt the user to choose a cell X
            # if the user enters a valid string and the cell on the board is empty, update the board X
            # otherwise print a message that the input is wrong and rewrite the prompt X
            # use the methods board.isempty(cell), and board.set(cell, sign) X
            # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
            # you can use a tuple ("A1", "B1",...) to obtain indexes 
            # you can do the conversion here in the player.py or in the board.py
            # this implementation is up to you

