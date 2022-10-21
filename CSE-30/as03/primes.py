"""                                                                                                 
Assignment 3: A module demonstrating generator functions and related concepts.                      
"""                                                                                                 
                                                                                                    
__author__ = "Simon Lee in CSE 30, siaulee@ucsc.edu"                                                
                                                                                                    
from collections.abc import Callable, Iterator  # For typing hints (we'll talk about "abc" later)   
                                                                                                    
                                                                                                    
def elements_under(sequence: Iterator[int], bound: int, predicate: Callable[[int], bool] = None) \  
    -> Iterator[int]:                                                                               
  """                                                                                               
  Yields a finite sequence of elements under a given bound, optionally matching a predicate.        
                                                                                                    
  :param sequence: an infinite sequence of integers, e.g. primes()                                  
  :param bound:  an exclusive upper bound for the yielded sequence                                  
  :param predicate: if present, the sequence includes only values for which this function returns   
  True                                                                                              
  """                                                                                               
  for num in sequence:                                                                              
    if num < bound:                                                                                 
      try:                                                                                          
        if predicate(num):                                                                          
          yield num                                                                                 
      except TypeError:                                                                             
        yield num                                                                                   
    else:                                                                                           
      break                                                                                         
                                                                                                    
                                          
def is_prime(n: int) -> bool:                                                                       
  """ Returns whether n is prime. """                                                               
  if n == 1:                                                                                        
    return False                                                                                    
  if n == 2:                                                                                        
    return True                                                                                     
  if n < 1:                                                                                         
    return False                                                                                    
  else:                                                                                             
    for i in range(2, n):                                                                           
      if n % i == 0:                                                                                
        return False                                                                                
    return True                                                                                     
                                                                                                    
                                                                                                    
def nth_element(sequence: Iterator[int], n: int) -> int:                                            
  """                                                                                               
  Returns the nth element of a possibly infinite sequence of integers.                              
                                                                                                    
  :param sequence: a sequence of integers, e.g. primes()                                            
  :param n: the sequence index desired                                                              
  :return: the value at index n of the sequence                                                     
  """                                                                                               
  counter = 0                                                                                       
  for num in sequence:  # this puts a limit to the amount of primes that can be printede            
    if counter == n:                                                                                
      return num                                                                                    
    counter += 1                                                                                    
                                                                                                    
                                                              
def primes() -> Iterator[int]:                                                                      
  """ Yields an infinite sequence of prime numbers. """                                             
  num = 2  # start at first prime number                                                            
  while True:  # infinite loop                                                                      
    if is_prime(num):                                                                               
      yield num                                                                                     
    num += 1                                                                                        
                                                                                                    
                                                                                                    
def prime_factors(n: int) -> list[int]:                                                             
  """ Returns a list of prime numbers with product n, in ascending order. """                       
  factors = []                                                                                      
  if n == 1:                                                                                        
    return factors                                                                                  
  else:                                                                                             
    divisor = 2                                                                                     
    while n > 1:                                                                                    
      if n % divisor == 0:  # finds rest of the divisors                                            
        factors.append(divisor)                                                                     
        n = n / divisor                                                                             
        divisor -= 1                                                                                
      divisor += 1                                                                                  
    return factors                                                                                  
                                                                                                    
                                                                                                    
def semiprimes() -> Iterator[int]:                                                                  
  """ Yields an infinite sequence of semiprimes. """                                                
  num = 4  # first semi-prime                                                                       
  while True:                                                                                       
    if len(prime_factors(num)) == 2:  # semi-primes are a number of 2 primes                        
      yield num                                                                                     
    num += 1                      


if __name__ == '__main__':                                                                          
  assert all(is_prime(n) for n in (2, 3, 5, 7))                                                     
  assert all(not is_prime(n) for n in (4, 6, 8, 9))                                                 
  assert list(elements_under(primes(), 10)) == [2, 3, 5, 7]                                         
  assert list(elements_under(semiprimes(), 10)) == [4, 6, 9]                                        
  assert nth_element(primes(), 2) == 5                                                              
  assert nth_element(semiprimes(), 2) == 9                                                          
  assert list(elements_under(primes(), 1386, lambda p: not 1386 % p)) == [2, 3, 7, 11]              
  assert prime_factors(1386) == [2, 3, 3, 7, 11]   
