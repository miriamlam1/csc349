# two colorable / bipartite / no odd cycles
# input: a graph given in a list of edges connecting vertices
# output: lists of each color if 2-colorable, else false


from collections import *
import sys


class Graph(): 
    def __init__(self): 
        self.graph = defaultdict(list)
  
    def add_edge(self,v1,v2): 
        self.graph[v1].append(v2) 
  
  
def bipartite(G): 
    red = []
    blue = []
    
    for start in sorted(G.graph): # checking all paths
        if start not in red and start not in blue: # to make sure we hit disconnected parts
            
            red.append(start)
            queue = [] 
            queue.append(start)

            while queue: 
                
                current_vertex = queue.pop()
                
                for neighbor in G.graph[current_vertex]: 
                    if neighbor not in red and neighbor not in blue:
                        queue.append(neighbor) 
                        
                        if current_vertex in red:
                            blue.append(neighbor)
                            
                        else:
                            red.append(neighbor)
                            
                    elif (current_vertex in red and neighbor in red) or\
                         (current_vertex in blue and neighbor in blue):
                        print ("Is not 2-colorable.")
                        return
                    
    print("Is 2-colorable:")
    print(", ".join(red)) 
    print(", ".join(blue)) 
  
  
def get_graph(file):
    f = open(file, "r")
    g = Graph()
    for line in f:
		line = line.split()
        g.add_edge(line[0], line[1])
    f.close()
    return g
    
    
def main():
    g = get_graph(sys.argv[1])
    bipartite(g)
    
    
if __name__ == "__main__":
    main()

