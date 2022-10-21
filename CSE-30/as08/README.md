PROGRAM DESCRIPTION
-------------------
Develop a data type with a Pythonic API suitable for representing graphs that are any combination of directed/undirected and weighted/unweighted.
Make strategic use of Python's built-in types, OOP features, and standard library to accomplish the above goal.

Vertices shall be any set of values that meet the criteria for dict keys, namely that they are immutable, e.g. strings and numbers. The class may assume that all vertices are of the same type, and comparable to each other (i.e., one_vertex == another_vertex is a valid and meaningful comparison). The examples below use strings as vertex values, but your class should not assume this.

Methods in class Graph shall consist of at least the following. If you have any questions regarding the expected behavior, note their use and expected results in the Testing section below.

__init__() shall accept no arguments and result in an empty graph containing no vertices or edges:
```
g = Graph()
```
Vertices and edges shall be added and removed using a combination of __getitem__(), __setitem__(), and __delitem__() syntax, similar to the examples shown in class using collections.defaultdict:
The following __getitem__() syntax shall add a vertex with value 'new_vertex' to the graph, disconnected from all other vertices:
```
g['new_vertex']
```
The following __setitem__() shall add/replace an edge from vertex 'a' to vertex 'b' with weight 10, simultaneously adding both of these vertices to the graph, if not already present:
```
g['a']['b'] = 10
```
Note that an edge weight such as True could serve to represent edges in an unweighted graph, and that complementary edges from a to b and from b to a could serve to represent an undirected graph.
Vertices and edges shall be removed using __delitem__() syntax:
```
del g['a']  # Removes vertex 'a' and all associated edges
del g['b']['c']  # Removes edge from vertex 'b' to vertex 'c', but not the vertices themselves
```
__len__() shall return the number of vertices in the graph:
```
len(g)  # determines the number of vertices
```
__contains__() shall return whether a vertex or edge exists in the graph:
```
'a' in g  # determines whether vertex 'a' exists
'b' in g['a']  # determines whether there is an edge from vertex 'a' to vertex 'b'
```
clear(), and copy() shall behave similarly to dict.clear() and dict.copy(), clearing all vertices and edges from a graph, and returning a shallow copy of a graph (i.e., with the same vertices and edges, but adding or removing vertices and edges in the copy will not affect the original):
```
g2 = g.copy()  # g is now a copy of g2
g2['c']['b'] = -9  # Modifies g2 but not g
g.clear()  # g is now empty
```
vertices() shall return a set of all vertices in the graph.
edges() shall return a set of all edges in the graph, as 3-tuples in the form (src, dst, weight).
adjacent(src, dst) shall return whether an edge from src to dst exists.
neighbors(vertex) shall return a set of all vertices adjacent to the given vertex.
degree(vertex) shall return the number of edges incident on the given vertex.
path_valid(vertices) shall return whether a sequence of vertices is a valid path in the graph.
path_length(vertices) shall return the path length of a sequence of vertices, or None if the path is invalid or trivial (one vertex). The length shall the be sum of all edge weights (you may assume that any_weight + any_other_weight is a valid expression).
is_connected() shall return whether the graph is connected).

HOW TO RUN PROGRAM
------------------
Like always run it the same way using an IDE or whatnot and you can run these assert tests to see if they are right.
```
if __name__ == '__main__':
  g = Graph()
  assert len(g) == 0
  assert 'wat' not in g
  assert not g.vertices()
  edges = ('a', 'c', 8), ('a', 'd', 4), ('c', 'b', 6), ('d', 'b', 10), ('d', 'c', 2)
  for (v_from, v_to, weight) in edges:
    g[v_from][v_to] = weight
  assert len(g) == 4
  assert 'a' in g
  assert 'c' in g['a']
  assert g.vertices() == set('abcd')
  assert g.edges() == set(edges)
  assert g.degree('d') == 2 and not g.degree('b')
  assert g.adjacent('a', 'c')
  assert not g.adjacent('c', 'a')
  assert g.path_valid(('a', 'c', 'b'))
  assert not g.path_valid(('c', 'b', 'a'))
  assert not g.is_connected()
  g['b']['a'] = 1
  assert g.degree('b') == 1 and g.degree('a') == 2
  assert g.path_valid(('c', 'b', 'a'))
  assert g.path_length(('c', 'b', 'a')) == 7
  assert g.is_connected()
  del g['a']
  assert not g.is_connected()
  assert g.vertices() == set('bcd')
  assert g.degree('b') == 0
 
  g2 = g.copy()
  assert g2 == g
  g2['b']['e'] = 1
  assert g2 != g
  assert g2.vertices() == set('bcde')
  g2['e']['d'] = 15
  assert g2.is_connected()
  assert g2.path_length(('e', 'd', 'c', 'b')) == 23
  del g2['e']['d']
  assert g2.degree('e') == 0
  assert g2.vertices() == set('bcde')
  assert not g2.is_connected()
  g.clear()
  assert len(g) == 0
  assert len(g2) == 4
```

