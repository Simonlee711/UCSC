PROGRAM DESCRIPTION
-------------------
You shall define a function named verbalize, in a module named verbalize.

The function shall accept one argument, assumed to be a nonnegative int, and shall return a list[str] containing the verbal equivalent of each order of magnitude of the argument, as described in the following code and docstring.Make sure your module loads data from number_names.txt only once, regardless of how many times verbalize() is called. Make sure you solve this problem recursively: You are allowed one loop total in the module (for or while) without penalty, which you will probably use for loading the contents of the number_names.txt file. Using recursion and built-in functions like next(), reversed(), sorted(), etc. will allow you to accomplish the rest without loops. Each subsequent loop will reduce your grade by 20%.

```
def verbalize(value: int) -> list[str]:
  """
  Returns a list of the verbalized orders of magnitude of a natural number, e.g.:
 
  verbalize(0) --> ['zero']
  verbalize(42) --> ['forty-two']
  verbalize(101) --> ['one hundred one']
  verbalize(9999) --> ['nine thousand', 'nine hundred ninety-nine']
  verbalize(1234567) -->
      ['one million', 'two hundred thirty-four thousand', 'five hundred sixty-seven']
  """
```
HOW TO RUN PROGRAM
------------------
A sample executable named cse30_integer_verbalizer exists on the server. It demonstrates the output expected of your verbalize module, were you to add the following main block:
```
if __name__ == '__main__':
  print('\n'.join(verbalize(int(sys.argv[1]))))
```
The following Bash commands create a variable named num containing a randomly generated 100-digit number, display it on standard output, and compare the output of the sample executable with that of the above main block:
```
num=$(python3 -c 'import random; print("".join(random.choice("0123456789") for _ in range(100)))')
echo $num
diff -u <(cse30_integer_verbalizer $num) <(./verbalize.py $num)
```
