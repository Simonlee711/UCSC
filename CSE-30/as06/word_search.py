"""                                                                                                 
Utility module for finding the solutions to a word search                                           
"""                                                                                                 
from __future__ import annotations                                                                  
import sys                                                                                          
import numpy as np                                                                                  
import bisect                                                                                       
import time                                                                                         
                                                                                                    
__author__ = 'Simon Lee in CSE 30, siaulee@ucsc.edu'                                                
                                                                                                    
                                                                                                    
def word_search_dict(dictionary, minimum_length): # slightly inspired by Andre's section            
  words = set()                                                                                     
  file = open(dictionary, 'r')                                                                      
  for line in file:                                                                                 
    line = line[:-1]                                                                                
    if len(line) >= minimum_length:                                                                 
        words.add(line.upper())                                                                     
  return words                                                                                      
                                                                                                    
def rows(matrix):                                                                                   
  row = []                                                                                          
  for line in matrix:                                                                               
    if line[-1] == '\n':                                                                            
      line = line[:-1]                                                                              
    row.append(line.upper())                                                                        
  return row  

def r_rows(matrix):  # reverse rows                                                                 
  r_row = []                                                                                        
  for line in matrix:                                                                               
    line = line[::-1]                                                                               
    r_row.append(line.upper())                                                                      
  return r_row                                                                                      
                                                                                                    
def columns(matrix, len):  # Connor Masterson helped me here                                        
  #matrix = np.asarray(matrix)                                                                      
  #for i in range(len):                                                                             
  #  print(matrix[:,i])                                                                             
  column = []                                                                                       
  currentCol = ''                                                                                   
  for j in range(len):                                                                              
    for i in range(len):                                                                            
      currentCol += matrix[i][j]                                                                    
    column.append(currentCol)                                                                       
    column.append(''.join(reversed(currentCol)))                                                    
    currentCol = ''                                                                                 
  return column                                                                                     
                                                                                                    
                                                                                                    
def diagonal_l_r(matrix, len):  # diagonal left to right                                            
  dlr = []  # lower-left-to-upper-right diagonals                                                   
  curr_dlr = ''                                                                                     
  for i in range(2 * len - 1):                                                                      
    for j in range(max(0, i - len + 1), min(i, len - 1) + 1):  # tutor Kenneth helped me here       
      curr_dlr += (matrix[i - j][j])                                                                
    dlr.append(curr_dlr)                                                                            
    dlr.append(''.join(reversed(curr_dlr)))                                                         
    curr_dlr = ''                                                                                   
  return dlr                                   

def diagonal_r_l(matrix, len):  # diagonal right to left                                            
  drl = []                                                                                          
  curr_drl = ''                                                                                     
  for i in range(2 * len - 1):                                                                      
    for j in range(max(0, i - len + 1), min(i, len - 1) + 1):                                       
      curr_drl += (matrix[len - i + j - 1][j])                                                      
    drl.append(curr_drl)                                                                            
    drl.append(''.join(reversed(curr_drl)))                                                         
    curr_drl = ''                                                                                   
  return drl                                                                                        
                                                                                                    
start_time = time.time()                                                                            
if __name__ == '__main__':                                                                          
  min_length = 0                                                                                    
  min_length = int(sys.argv[1])                                                                     
  dict_file = sys.argv[2]                                                                           
  word_search = word_search_dict(dict_file, min_length)                                             
  grid = rows(sys.stdin)                                                                            
  print(*grid, sep = "\n", file = sys.stdout)                                                       
  grid_len = len(grid)                                                                              
  everything = [grid, r_rows(grid), columns(grid, grid_len),                                        
                diagonal_l_r(grid, grid_len), diagonal_r_l(grid, grid_len)]                         
                                                                                                    
  # making one giant list                                                                           
  final = []                                                                                        
  for inner in everything:                                                                          
    for elem in inner:                                                                              
      if len(elem) < min_length:                                                                    
        continue                                                                                    
      final.append(elem)              

  #searching for words                                                                              
  words_found = []                                                                                  
  for word in word_search:                                                                          
    for directions in final:                                                                        
      if word in directions:                                                                        
        words_found.append(word)                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
  # sorts words in alphabetical order                                                               
  words_found.sort()                                                                                
  print(*words_found, sep = "\n", file = sys.stderr)                                                
  print("--- %s seconds ---" % (time.time() - start_time))   
