PROGRAM DESCRIPTION
--------------------
This assignment we got to explore the graphs ADT, and also learn about the 
shortest path finding algorithm known as Depth-First Search or (DFS). DFS 
as explained in lecture utilizes the stack, while there is also Breadth 
First, Search which utilizes the queue but that has nothing to do with this
assignment. So in this assignment we had to find a Hamiltonian cycle which is 
when you visit every vertex of a graph once, and the last vertex has an edge
right back to the origin. refer to the following coordinates: <A,B,5>, 
<B,C,2>, and <C,A,3>.

Quick lesson on graph theory but A,B,C represent the vertices, and the numbers
5,2,3 represent the edges connecting from nodes i to j. Above we have how we 
will be reading the adjancency matrix "coordinates". This graph represents a 
hamiltonian cycle because theres a path from: A-B-C-A. However graphs can also
be undirected meaning each edge is bidirectional. We can also have a case where
there is no hamiltonian cycle at all and that will cause an infinite loop within
the dfs algorithm. Anyway you can have up to a 26 x 26 adjancency matrix and you
can have as many edges as possible. The dfs does all the work in finding the path 
and will print all the paths or just the shortest path based on which command line
arguments are selected. I will note that my one little error I have is that I was
unable to have the path printed on one line because I believe the file prints a new
line character after it reads from it. Other than that code should run smoothly.
 
HOW TO BUILD PROGRAM
--------------------
In order to build the program it is very similar to the previous assignment
where we are restricted to a specific amount of command line arguments that
we can run in order to see whether the output is correct. However as always
there is a makefile that links all my c files together so the program works
properly. In total I believe there were 8 files not involving the README.md,
DESIGN.pdf, and Makefile that were needed for this assignment.
So it was crucial to link all the files in the Makefile. Lastly like always
you can compile the program by simply running "make sorting" in the terminal.

HOW TO RUN PROGRAM
------------------
Lastly as always here I will disclose how to run specific feature of a program.
We have 5 command line arguments those being -h for helper message, -u for
an undirected graph, -v for verbose printing, -i for a specific input file to 
be read, and -o for a specific file to be written in. As previously mentioned
use the -u at your own discretion as when i tried running the texas.graph as an
undirected graph the dfs algorithm was unable to find the shortest path therefore
infinitely looping. But after running the resources version it did the same 
so I can assume that not all undirected graphs have hamiltonian cycles. This 
assignment was tedious debugging segmentation faults but after completing it 
with a few minor errors including the one mentioned at the end of the 
(PROGRAM DESCRIPTION), I am happy with the result. This class has been ridiculouly
challenging but after completing these assignments, I do feel alot of satisfaction
for the hard work I put in. cool beans!

WHAT TO PUT IN TERMINAL
-----------------------
```
make
```
```
./tsp [-u] [-v] [-h] [-i infile] [-o outfile]
```
