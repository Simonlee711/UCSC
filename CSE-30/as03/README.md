PROGRAM DESCRIPTION
-------------------
You should know that any natural number is either prime or composite. A prime number has exactly two factors, viz. 1 and itself. All other natural numbers are composite numbers, which can be expressed as a product of a unique collection of two or more primes. This fact is otherwise known as the fundamental theorem of arithmetic. A semiprime is the product of two prime numbers.

Prime numbers have been of interest to mathematicians for a very long time, but they also have a practical and ubiquitous use in the digital age. The security of much of the encrypted traffic on the internet (including your communication right now with our server!) is predicated on the fact that it is computationally difficult to find the factors of large semiprimes.

HOW TO RUN PROGRAM
------------------
Using these assert tests should be plenty to know whether the functionality of the program works.
I highly recommend also reading the docstrings of the functions to understand how to run this program
appropriatley. I also highly recommend, running this program on A python IDE again.
```
if __name__ == '__main__':
  assert all(is_prime(n) for n in (2, 3, 5, 7))
  assert all(not is_prime(n) for n in (4, 6, 8, 9))
  assert list(elements_under(primes(), 10)) == [2, 3, 5, 7]
  assert list(elements_under(semiprimes(), 10)) == [4, 6, 9]
  assert nth_element(primes(), 2) == 5
  assert nth_element(semiprimes(), 2) == 9
  assert list(elements_under(primes(), 1386, lambda p: not 1386 % p)) == [2, 3, 7, 11]
  assert prime_factors(1386) == [2, 3, 3, 7, 11]
```
