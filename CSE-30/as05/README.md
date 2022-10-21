PROGRAM DESCRIPTION
-------------------
Readability is the ease with which a reader can understand a written text. In natural language, the readability of text depends on its content (the complexity of its vocabulary and syntax) and its presentation (such as typographic aspects like font size, line height, character spacing, and line length).
Many formulas exist for estimating readability.

File syllables.txt  contains information about how various English words can be decomposed into their constituent syllables. Each line contains one term, with syllables separated by semicolons. Here are ten randomly chosen lines from the file:
```
un;he;do;nis;tic
cel;e;bra;tive
crunch;ing;ly
ex;he;dra
un;heed;ful
de;plor;a;bil;i;ty
sea;wards
tet;ra;va;len;cy
el;o;cu;tion
do;lo;mit;iz;ing
```

Any readability metrics requiring the total number of characters or letters shall consider that to be the number of characters in the text for which str.isalpha() or str.isdigit() returns True.

A word shall be any sequence of English letters, decimal digits, apostrophes, and hyphens, trimmed of leading and trailing apostrophes and hyphens.

The number of syllables in a word shall be dictated by the data in file syllables.txt, without regard to case. Any word not present in this dataset shall be considered a monosyllabic word. Some words appear multiple times in this dataset, with different syllable counts—in these cases, opt for the highest count.

A sentence shall be any sequence of one or more words, with the final word indicated by the presence of a period (.), question mark (?), or exclamation point (!):


HOW TO RUN PROGRAM
------------------
The main block above will print the results of calling the methods that implement the four readability formulas, using all of standard input as the body of text. Here are some expected outputs (including from my words() and sentences() methods):

```
if __name__ == '__main__':
  demo = Readability(sys.stdin.read())
  # My solution has some extra (helper) methods.
  # You don't have to implement these, but I recommend doing something like it.
  if hasattr(demo, 'words'):
    print(len(demo.words()), 'words: ', demo.words()[:5], '...')
  if hasattr(demo, 'sentences'):
    print(len(demo.sentences()), 'sentences: ', demo.sentences()[:5], '...')
  if hasattr(demo, 'num_syllables'):
    print(demo.num_syllables(), 'syllables')
  if hasattr(demo, 'polysyllabic_words'):
    print(len(demo.polysyllabic_words()), 'polysyllabic words: ',
          demo.polysyllabic_words()[:5], '...')
  print('ARI', demo.automated_readability_index())
  print('CLI', demo.coleman_liau_index())
  print('FKG', demo.flesch_kincaid_grade())
  print('SMOG', demo.smog_grade())
```
