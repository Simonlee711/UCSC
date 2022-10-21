"""                                                                                                 
Utility module for dealing with readability metrics of English text.                                
"""                                                                                                 
from __future__ import annotations                                                                  
                                                                                                    
__author__ = 'Simon Lee in CSE 30, siaulee@ucsc.edu'                                                
                                                                                                    
import math                                                                                         
import re                                                                                           
import string                                                                                       
                                                                                                    
                                                                                                    
class Readability(str):                                                                             
  """                                                                                               
  Represents a string that can be assessed for readability metrics of English text.                 
  """                                                                                               
                                                                                                    
  def count_words(self):  # TA Donnie helped me                                                     
    """                                                                                             
    counts the number of words in the list                                                          
    """                                                                                             
    words = []                                                                                      
    words = re.split("[^A-Za-z0-9'-]", self)                                                        
    words = ["".join(c for c in self if c not in string.punctuation) for self in words]             
    words = [s for s in words if s not in ('', "'", '-')]                                           
    return words                                                                                    
                                                                                                    
  def create_dictionary(self):                                                                      
    word_dict = {}                                                                                  
    dataset = (open("syllables.txt", "r")).readlines()                                
    for line in dataset:                                                                            
      value = line[:-1]  # to remove \n courtest of Donnie                                          
      remove = ''.join(s for s in value if s != (";"))                                              
      key = remove                                                                                  
      word_dict[key] = value                                                                        
    return word_dict                               

  def count_characters(self):                                                                       
    characters = 0                                                                                  
    for word in self:                                                                               
      if word.isalpha():                                                                            
        characters += 1                                                                             
      elif word.isdigit():                                                                          
        characters += 1                                                                             
    return characters                                                                               
                                                                                                    
  def count_syllables(self):  # TA Donnie helped me with this but is not right                      
    syllable_dict = self.create_dictionary()                                                        
    words = self.count_words()                                                                      
    syllables = 0                                                                                   
    for word in words:                                                                              
      word = word.lower()                                                                           
      if word in syllable_dict or word[-1] in syllable_dict:                                        
        syllables += syllable_dict[word].count(';') + 1                                             
      else:                                                                                         
                                                                                                    
        syllables += 1                                                                              
    return syllables                                                                                
                                                                                                    
  def count_polysyllables(self):  # TA Donnie and tutor Kenneth helped me                           
    poly_dict = self.create_dictionary()                                                            
    polysyllables = 0                                                                               
    words = self.count_words()                                                                      
    for word in words:                                                                              
      word = word.lower()                                                                           
      if word in poly_dict or word[-1] in poly_dict:                                                
        if (poly_dict[word].count(';') + 1) > 2:                                                    
          polysyllables += 1                                                                        
    return polysyllables                      

  def count_sentences(self):                                                                        
    lines = 0                                                                                       
    sent = self.split()                                                                             
    for word in sent:                                                                               
      if word[-1] in ('.', '?', '!') and word != '.':                                               
        lines += 1                                                                                  
    return lines                                                                                    
                                                                                                    
  def automated_readability_index(self) -> float:                                                   
    """                                                                                             
    Calculates and returns the automated readability index of this text.                            
    See: https://en.wikipedia.org/wiki/Automated_readability_index                                  
    """                                                                                             
    words = len(self.count_words())                                                                 
    sentences = self.count_sentences()                                                              
    characters = self.count_characters()                                                            
    first = (characters / words)                                                                    
    second = (words / sentences)                                                                    
    ARI = (4.71 * first) + (0.5 * second) - 21.43                                                   
    return ARI                                                                                      
                                                                                                    
  def coleman_liau_index(self) -> float:                                                            
    """                                                                                             
    Calculates and returns the Coleman–Liau index of this text.                                     
    See: https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index                                   
    """                                                                                             
    words = len(self.count_words())                                                                 
    sentences = self.count_sentences()                                                              
    characters = self.count_characters()                                                            
    L = (characters / words) * 100                                                                  
    S = (sentences / words) * 100                                                                   
    CLI = (0.0588 * L) - (0.296 * S) - 15.8                                                         
    return CLI                                         

  def flesch_kincaid_grade(self) -> float:                                                          
    """                                                                                             
    Calculates and returns the Flesch–Kincaid grade level of this text.                             
    See: https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests                     
    #Flesch%E2%80%93Kincaid_grade_level                                                             
    """                                                                                             
    words = len(self.count_words())                                                                 
    sentences = self.count_sentences()                                                              
    syllables = self.count_syllables()                                                              
    first = (words / sentences)                                                                     
    second = (syllables / words)                                                                    
    FKG = (0.39 * first) + (11.8 * second) - 15.59                                                  
    return FKG                                                                                      
                                                                                                    
  def smog_grade(self) -> float | None:                                                             
    """                                                                                             
    Calculates and returns the SMOG grade of this text,                                             
    or None if the text contains fewer than 30 sentences.                                           
    See: https://en.wikipedia.org/wiki/SMOG                                                         
    """                                                                                             
    sentences = self.count_sentences()                                                              
    polysyllables = self.count_polysyllables()                                                      
    first = (30 / sentences) * polysyllables                                                        
    second = math.sqrt(first)                                                                       
    SMOG = (1.0430 * second) + 3.1291                                                               
    return SMOG                                    
