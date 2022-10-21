"""                                                                                                 
Contains class Protein for working with protein-related information.                                
"""                                                                                                 
                                                                                                    
__author__ = 'Simon Lee in CSE 30, siaulee@ucsc.edu'                                                
                                                                                                    
                                                                                                    
class Protein:                                                                                      
  """ Represents an immutable sequence of amino acids. """                                          
  def dataset(self):                                                                                
    mass_dict = {}  # start with empty dictionary                                                   
    with open("amino-monoisotopic-mass.txt", "r") as mass_file:                           
      for lines in mass_file:                                                                       
        data = lines.split()                                                                        
        amino = data[0]                                                                             
        # straight from the website to convert dna to rna                                           
        mass_dict[amino] = float(data[1])                                                           
      return mass_dict                                                                              
                                                                                                    
  # amino = dataset()    

  def __init__(self, aminos=None):                                                                  
    """                                                                                             
    Constructs a protein from a sequence of amino acids.                                            
    See: http://rosalind.info/problems/prot/                                                        
                                                                                                    
    :param aminos: A sequence of single-character strings, expected to be in the amino-acid alphabet
    :raise: ValueError if aminos contains characters not found in the amino-acid alphabet           
    """                                                                                             
    # based off Professor Bergamini's example from class                                            
    self._aminos = list(aminos) if aminos else[]                                                    
    self.dictionary = self.dataset()                                                                
    if any(base not in 'ACDEFGHIKLMNPQRSTVWY' for base in self._aminos):                            
      # checking for letters not in alphabet                                                        
      raise ValueError('not found in amino-acid alphabet')                                          
                                                                                                    
  def __add__(self, addition):                                                                      
    """                                                                                             
    The + operator concatenates two proteins.                                                       
                                                                                                    
    :param addition: a sequence of single-character strings in the amino-acid alphabet              
    :return: a new Protein object representing the concatenation of this protein and the addition   
    :raise: ValueError if addition contains characters not found in the amino acid-alphabet         
    """                                                                                             
    # essentially this is a string concatenation where two strings are added together               
    self._addition = list(addition) if addition else []                                             
    if any(base not in 'ACDEFGHIKLMNPQRSTVWY' for base in self._addition):                          
      raise ValueError('not found in amino-acid alphabet')                                          
    return Protein(self._aminos + list(addition))  # based off Professor Bergamini's example  

  def __eq__(self, other):                                                                          
    """                                                                                             
    Two proteins will be equal if they represent the same sequence of amino acids.                  
                                                                                                    
    :param other: a sequence of single-character strings in the amino-acid alphabet                 
    :return: whether this protein is equal to the other                                             
    """                                                                                             
    # if two sequences contain the same characters it will return True                              
    if isinstance(other, Protein):                                                                  
      return self._aminos == other._aminos  # based off Professor Bergamini's example               
    else:                                                                                           
      return self._aminos == list(other)                                                            
                                                                                                    
  def __getitem__(self, key):                                                                       
    """                                                                                             
    The [] operator allows users to retrieve individual amino acids in a protein by index,          
    or a Protein object representing a slice of this protein.                                       
                                                                                                    
    :param key: an index or slice                                                                   
    :return: a single-character string (if key was an index) or a Protein (if key was a slice)      
    :raise: IndexError if index is out of range                                                     
    """                                                                                             
    # try and except statement made so if a slice of the string is not there, it fails              
    try:                                                                                            
      if isinstance(key, slice):                                                                    
        return Protein(self._aminos[key])                                                           
      else:                                                                                         
        return self._aminos[key]                                                                    
    except IndexError:                                                                              
      raise IndexError("index is out of range")                  

  def __len__(self):                                                                                
    """ Returns the length of this protein, i.e. its number of amino acids. """                     
    # returns length of the user inputted protein                                                   
    return len(self._aminos)  # based off Professor Bergamini's example                             
                                                                                                    
  def __repr__(self):                                                                               
    """ Returns a string that would result in reproducing this protein when interpreted. """        
    # returns an f string in a certain format seen below                                            
    return f"Protein('{self}')"  # based off Professor Bergamini's example                          
                                                                                                    
  def __str__(self):                                                                                
    """ Returns a string containing the amino-acid letters for this protein. """                    
    return ''.join(self._aminos)  # based off Professor Bergamini's example                         
                                                                                                    
  def mass(self):                                                                                   
    """                                                                                             
    Returns the mass of this protein (in Daltons), according to the monoisotopic mass table.        
    See: http://rosalind.info/problems/prtm/                                                        
    """                                                                                             
    p_mass = 0.0                                                                                    
    for i in range(len(self._aminos)):                                                              
      p_mass += self.dictionary[self._aminos[i:i + 1][0]]                                           
    return p_mass                                                                                   
                                                                                                                            104,1         Bot

