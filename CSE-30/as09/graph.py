"""                                                                                                 
Utility module for making a graph ADT in python                                                     
"""                                                                                                 
from __future__ import annotations                                                                  
                                                                                                    
__author__ = 'Simon Lee in CSE 30, siaulee@ucsc.edu'                                                
                                                                                                    
                                                                                                    
class GraphDict(dict):                                                                              
    '''This class is designed strictly to build the graph dictionary'''                             
    def __init__(self, graph):                                                                      
        '''Create a new GraphDict'''                                                                
        super().__init__()                                                                          
        self.graph = graph                                                                          
                                                                                                    
    def __setitem__(self, key, value):                                                              
        '''Add a new edge to the given vertex'''                                                    
        if key not in self.graph:                                                                   
            self.graph[key] = GraphDict(self.graph)                                                 
        super().__setitem__(key, value) 

class Graph:                                                                                        
    ''' this class provides all the functions of a graph ADT'''                                     
    def __init__(self):                                                                             
        '''Create a new Graph'''                                                                    
        self.graph = {}                                                                             
                                                                                                    
    def __getitem__(self, key):                                                                     
        '''Get the vertex with key. Create if non-existent.'''                                      
        if key not in self.graph:                                                                   
            self.graph[key] = GraphDict(self.graph)                                                 
        return self.graph[key]                                                                      
                                                                                                    
    def __setitem__(self, key, value):                                                              
        '''Set the vertex with key.'''                                                              
        if key not in self.graph:                                                                   
            self.graph[key] = value                                                                 
                                                                                                    
    def __delitem__(self, key):                                                                     
        '''Delete the vertex and all edges from, to it.'''                                          
        del self.graph[key]                                                                         
        for k in self.graph:                                                                        
            if key in self.graph[k]:                                                                
                del self.graph[k][key]                                                              
                                                                                                    
    def __len__(self):                                                                              
        '''Get the number of vertices.'''                                                           
        return len(self.graph)                                                                      
                                                                                                    
    def __contains__(self, key):                                                                    
        '''Check if a vertex is in the graph.'''                                                    
        return key in self.graph                                      


    def __str__(self):                                                                              
        '''String representation.'''                                                                
        s = ''                                                                                      
        for key in self.graph:                                                                      
            s += f'{key}: {self.graph[key]}\n'                                                      
        return s                                                                                    
                                                                                                    
    def clear(self):                                                                                
        '''Clear the graph.'''                                                                      
        self.graph.clear()                                                                          
                                                                                                    
    def copy(self):                                                                                 
        '''Make a copy of the graph.'''                                                             
        cp = Graph()                                                                                
        for key in self.graph:                                                                      
            cp[key] = self.graph[key].copy()                                                        
        return cp                                                                                   
                                                                                                    
    def vertices(self):                                                                             
        '''Get the set of vertices in the graph.'''                                                 
        return set(self.graph.keys())                                                               
                                                                                                    
    def edges(self):                                                                                
        '''Get the set of edges in the graph.'''                                                    
        e = set()                                                                                   
        for src in self.graph:                                                                      
            for dst in self.graph[src]:                                                             
                e.add((src, dst, self.graph[src][dst]))                                             
        return e

    def neighbors(self, vertex):                                                                    
        '''Get the set of neighbors of a given vertex.'''                                           
        n = set()                                                                                   
        for edge in self.graph[vertex]:                                                             
            n.add(edge)                                                                             
        return n                                                                                    
                                                                                                    
    def degree(self, vertex):                                                                       
        '''Get the degree of a vertex.'''                                                           
        return len(self.graph[vertex])                                                              
                                                                                                    
    def path_valid(self, vertices):                                                                 
        '''Check if a path is valid.'''                                                             
        for v in range(len(vertices) - 1):                                                          
            if vertices[v + 1] not in self.graph[vertices[v]]:                                      
                return False                                                                        
        return True                                                                                 
                                                                                                    
    def path_length(self, vertices):                                                                
        '''Get the length of the path given in vertices. None if invalid.'''                        
        if len(set(vertices)) <= 1 or not self.path_valid(vertices):                                
            return None                                                                             
        length = 0                                                                                  
        for v in range(len(vertices) - 1):                                                          
            length += self.graph[vertices[v]][vertices[v + 1]]                                      
        return length                                                                               
                                                                                                    
    def connected(self):                                                                            
        '''Check if a graph is connected.'''                                                        
        visited = {key: False for key in self.graph}                                                
        src = list(self.graph.keys())[0]                                                            
        self._dfs(src, visited)                                                                     
        return list(visited.values()).count(False) == 0    


    def _dfs(self, src, visited):                                                                   
        '''Run a recursive depth-first search in the graph.'''                                      
        visited[src] = True                                                                         
        for neighbor in self.graph[src]:                                                            
            if not visited[neighbor]:                                                               
                self._dfs(neighbor, visited)                                             
