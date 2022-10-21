"""                                                                                                 
Utility module for verbalizing numbers                                                              
"""                                                                                                 
from __future__ import annotations                                                                  
                                                                                                    
__author__ = 'Simon Lee in CSE 30, siaulee@ucsc.edu'                                                
                                                                                                    
# making a list was not working so I made a dictionary                                              
f = open("/srv/datasets/number_names.txt", "r")                                                     
lines = f.readlines()                                                                               
data = {}                                                                                           
for line in lines:                                                                                  
    line = line.strip()                                                                             
    data[int(line.split()[1])] = line.split()[0]                                                    
                                                                                                    
                                                                                                    
# added an extra argument because I was having a weird error and it would append to same list       
def verbalize(value, result=None) -> list[str]:                                                     
                                                                                                    
    if not result:  # resets list every time this is called                                         
        result = [""]                                                                               
                                                                                                    
    if value < 20:  # just accessing dictionary                                                     
        result[-1] += data[value]                                                                   
        return result                                                                               
                                                                                                    
    elif value < 100:                                                                               
        if value % 10 != 0:  # hyphen checking conditional                                          
            result[-1] += (data[value - (value % 10)] + "-")                                        
            verbalize(value % 10, result)                                                           
            return result                                                                           
        else:  # else no hyphen                                                                     
            result[-1] += (data[value])                                                             
            return result                   

  elif value < 1000:                                                                              
        num1 = value // 100                                                                         
        num3 = value % 100                                                                          
        if num3 != 0:                                                                               
            verbalize(num1, result)                                                                 
            result[-1] += " " + data[100] + " "                                                     
            verbalize(num3, result)                                                                 
            return result                                                                           
        else:                                                                                       
            verbalize(num1, result)                                                                 
            result[-1] += " " + data[100]                                                           
            return result                                                                           
                                                                                                    
    order = (len(str(value)) - 1) // 3  # this equation finds the suffix thousand - centillion      
    leading_number = value // (1000 ** order)                                                       
    next_number = value % (1000 ** order)                                                           
                                                                                                    
    if next_number != 0:                                                                            
        verbalize(leading_number, result)                                                           
        result[-1] += (" " + data[1000 ** order])                                                   
        result.append("")                                                                           
        return verbalize(next_number, result)                                                       
                                                                                                    
    else:                                                                                           
        verbalize(leading_number, result)                                                           
        result[-1] += (" " + data[1000 ** order])                                                   
        return result                         
