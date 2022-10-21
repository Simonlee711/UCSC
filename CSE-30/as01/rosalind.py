#!/usr/bin/env python3                                                                              
"""                                                                                                 
Calculating the percentage of the C's and G's in a particular DNA Strand                            
                                                                                                    
Remember: chmod +x assignment_01.py                                                                 
                                                                                                    
Try e.g.                                                                                            
python3 assignment_01.py <<<GATTACA                                                                 
python3 assignment_01.py </sars-cov-2.txt                                                  
python3 assignment_01.py </brca1.txt                                                       
python3 assignment_01.py </chromosome4.txt                                                 
python3 assignment_01.py </chromosome11.txt                                                
python3 assignment_01.py </joyce-finnegans-wake.txt                                    
"""                                                                                                 
__author__ = 'Simon Lee for CSE30 Spring 2021, siaulee@ucsc.edu' 

# START OF PROGRAM                                                                                  
import sys                                     # importing sys to help with readability             
Total_count = 0                                # initializing counters for programs                 
C_count = 0                                                                                         
G_count = 0                                                                                         
for data in sys.stdin:                                                                              
  C_count += data.count('C')                                                                        
  G_count += data.count('G')                                                                        
  Total_count += data.count('A')                                                                    
  Total_count += data.count('C')                                                                    
  Total_count += data.count('G')                                                                    
  Total_count += data.count('T')                                                                    
                                                                                                    
try:                                                                                                
  C_and_G = C_count + G_count                  # since we are seeking percentage of C and G         
  percentage = C_and_G / Total_count * 100     # percentage algorithm                               
except ZeroDivisionError:                                                                           
  percentage = 0.000000                                                                             
print(round(percentage, 6))                    # expected output      
