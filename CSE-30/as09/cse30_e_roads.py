"""                                                                                                 
Utility module for finding the shortest paths from destinations in Europe in the international      
E-road network. Utilize Djikstra's algorithm to find the quickest route to each city and either     
prints the appropriate path or it prints out a url that will give you the quickest path on          
google maps.                                                                                        
"""                                                                                                 
from __future__ import annotations                                                                  
                                                                                                    
__author__ = 'Simon Lee in CSE 30, siaulee@ucsc.edu'                                                
                                                                                                    
from graph import Graph                                                                             
from graph import GraphDict                                                                         
import math                                                                                         
import sys                                                                                          
                                                                                                    
def read_cities():                                                                                  
    '''Read cities from the given file.'''                                                          
    cities = {}                                                                                     
    with open('vertex_names.txt', 'r') as input_file:                         
        for line in input_file:                                                                     
            city = line.split()                                                                     
            id, name = city[0], ' '.join(city[1:])                                                  
            cities[id] = name                                                                       
            cities[name] = id                                                                       
        return cities                                                                               
                                                                                                    
                                                                                                    
def read_paths():                                                                                   
    '''Read paths from the given file.'''                                                           
    paths = []                                                                                      
    with open('networks.txt', 'r') as input_file:                              
        for line in input_file:                                                                     
            paths.append(tuple(line.split()))                                                       
    return paths                                                                                    
                                                                                                    
                                                                                                    
def read_coords():                                                                                  
    '''Read city coordinates from the given file.'''                                                
    coords = {}                                                                                     
    with open('vertex_locations.txt', 'r') as input_file:                     
        for line in input_file:                                                                     
            key, lat, lon = line.split()                                                            
            coords[key] = float(lat), float(lon)                                                    
    return coords            


def haversine_distance(lat1, lon1, lat2, lon2):                                                     
    '''Calculate the distance between two points using the haversine formula.                       
    Based on: https://www.movable-type.co.uk/scripts/latlong.html'''                                
    R = 6371e3                                                                                      
    phi1 = lat1 * math.pi / 180                                                                     
    phi2 = lat2 * math.pi / 180                                                                     
    dp = (lat2 - lat1) * math.pi / 180                                                              
    dl = (lon2 - lon1) * math.pi / 180                                                              
                                                                                                    
    a = math.sin(dp / 2) * math.sin(dp / 2) + math.cos(phi1) * math.cos(                            
        phi2) * math.sin(dl / 2) * math.sin(dl / 2)                                                 
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))                                              
                                                                                                    
    return R * c                                                                                    
                                                                                                    
                                                                                                    
def Djikstras_algorithm(src, dst):                                                                  
        '''Find the shortest path between two vertices.'''                                          
        # special edge case where both src and dst are the same
        if src == dst:
          unique_path = []
          unique_path.insert(0, src)
          return unique_path

        # Djikstra's formula - based off Professor's pseudocode
        distance = {}                                                                               
        previous = {}                                                                               
        queue = []                                                                                  
        for v in graph.vertices():                                                                  
            distance[v] = 2 ** 32  # Tutor Connor Masterson helped me here                          
            previous[v] = 0                                                                         
        distance[src] = 0                                                                           
                                                                                                    
        queue.append((0, src))                                                                      
        while queue:                                                                                
            length, node = queue.pop(0)                                                             
            for neighbor in graph.neighbors(node):                                                  
                new_distance = length + graph[node][neighbor]                                       
                if new_distance < distance[neighbor]:                                               
                    distance[neighbor] = new_distance                                               
                    previous[neighbor] = node                                                       
                    queue.append((new_distance, neighbor))                                          
                                                                                                    
        path = []                                                                                   
        u = dst                                                                                     
        while previous[u]:                                                                          
            path.insert(0, u)                                                                       
            u = previous[u]                                                                         
                                                                                                    
        return path


def parse_args():                                                                                   
    '''Parse command line arguments.'''                                                             
    if len(sys.argv) < 3:                                                                           
        return None                                                                                 
    src, dst, maps = sys.argv[1], sys.argv[2], len(sys.argv) > 3                                    
    return src, dst, maps                                                                           
                                                                                                    
                                                                                                    
def error(err):                                                                                     
    '''Print to stderr'''                                                                           
    print(err, file=sys.stderr)                                                                     
                                                                                                    
                                                                                                    
if __name__ == '__main__':                                                                          
                                                                                                    
    '''Where the magic happens'''                                                                   
    # Read data from the files.                                                                     
    try:                                                                                            
        cities = read_cities()                                                                      
        paths = read_paths()                                                                        
        coords = read_coords()                                                                      
    except:                                                                                         
        error('Error reading data from the files.')                                                 
        sys.exit(1)                                                                                 
                                                                                                    
    # Create the graph and add the paths.                                                           
    graph = Graph()                                                                                 
    for path in paths:                                                                              
        lat1, lon1 = coords[path[0]]                                                                
        lat2, lon2 = coords[path[1]]                                                                
        distance = haversine_distance(lat1, lon1, lat2, lon2)                                       
        graph[path[0]][path[1]] = distance                                                          
        graph[path[1]][path[0]] = distance                                                          
                                                                                                    
    try:                                                                                            
        src_name, dst_name, maps = parse_args()                                                     
    except:                                                                                         
        error('Arguments should be in the form: python3.9 cse30_e_roads.py [src] [dst] [maps+]')                        
        sys.exit(1)


    try:                                                                                            
        src_id = cities[src_name]                                                                   
        dst_id = cities[dst_name]                                                                   
    except:                                                                                         
        error('One or both of the provided cities don\'t exist in the database.')                   
        sys.exit(1)                                                                                 

                                                                                                
    # Find the shortest path.                                                                       
    path = Djikstras_algorithm(src_id, dst_id)                                                      

    if not path:                                                                                    
        error(f'No path found from {src_name} to {dst_name}')                                       
        sys.exit(1)                                                                                 
    
    #if src and dst are the same and maps is opted in
    if (src_id == dst_id) and (maps):
        url = f'https://www.google.com/maps/dir'
        lat, lon = coords[src_id]
        url += f'/{lat:.3f},{lon:.3f}'
        print(url)
        sys.exit(1) 
    
    #if src and dst are the same print only once
    if src_id == dst_id:
        print(src_name)
        sys.exit(1)
                                                                                                
    # If maps, show the map URL. Otherwise print the city names.                                    
    if maps:                                                                                        
        url = f'https://www.google.com/maps/dir'                                                        
        path.insert(0, src_id)                                                                      
        for city in path:                                                                           
            lat, lon = coords[city]                                                                 
            url += f'/{lat:.3f},{lon:.3f}'                                                          
        print(url)                                                                                  
    else:                                                                                           
        print(src_name)                                                                             
        for city_id in path:                                                                        
            print(cities[city_id])        
