PROGRAM DESCRIPTION
-------------------
You shall write a Python 3 program (compatible up to Python 3.9) that reads a word-search grid from standard input, and prints all valid words in the grid to standard output. Specifically:

Use cse30_word_search as the name the module intended to be run as __main__.
The grid will consist of any number of lines of text on standard input, containing uppercase English letters.
You may assume that the length of each line is also the total number of lines, i.e. that the grid is square.
The program shall expect two command-line arguments, which together dictate the characteristics of a valid word:
Argument 1 shall be a positive integer indicating the minimum length of a valid word.
Argument 2 shall be a path to a spell-checking dictionary file.
You may assume that the dictionary file contains one word per line, though there are no guarantees on case or contents otherwise.
The output shall consist of all unique valid words in the grid, one per line, in alphabetical order.
Words may be oriented in any horizontal, vertical, or diagonal direction from the initial letter (i.e., 8 possible orientations).

Make sure that you choose an approach with appropriate data types and algorithms so that the time complexity of your solution is:

Good enough as a baseline to terminate within 5 seconds given 20×20 grids and dictionary sizes up to 1 million words.
O(n) or better where n is the total size of the grid
O(log n) or better where n is the total size of the dictionary
O(n) or better where is the difference between the dimension of the grid and the minimum length of a valid word (e.g. 8 for a 10×10 grid with a minimum length of 2)

HOW TO RUN PROGRAM
------------------
As mentioned previously the first argument it takes is the min length word that can be accounted for by a dicitonary.
The second argument is the dictionary from which it reads, and the third will be a grid of some sort unless you want to
type it from standard input. Follow the format below and I will provide test grids and a dictionary:
```
python3.9 word_search.py 5 /usr/share/dict/american-english <test_grid
```

