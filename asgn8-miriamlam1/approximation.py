# Assignment 8: Approximating Metric TSP
# Inputs: A weighted graph
# Output: Minimum Hamiltonian 

from graph import Graph
import sys

def dfs(v, visited, graph, v2):
    if v == v2:
        return False
    if visited[v] == 0:  # not visited
        visited[v] = 1  # mark visited
        for neighbor in graph[v]:  # dfs through neighbors
            if dfs(neighbor, visited, graph, v2) == False: # recurse
                return False

def check_cycle(g, e):
    sum = 1
    for v in g:
        sum +=1
    visited = sum * [0]
    return dfs(e[0], visited, g, e[1])


# input: weighted graph G
# output: minimum spanning tree
def kruskals(g, edge_list):
    #print(g)
    #print(edge_list)

    t = Graph() # subgraph of G
    for vertex in g:
        t.add_vertex(vertex)

    while(edge_list): # edge set is not empty
        e = edge_list[0]# lightest edge
        edge_list.remove(e)
        if check_cycle(t,e) != False:
            t.add_edge(e[0], e[1], e[2])
    return t

def skip_duplicate_vertices(t, g):
    s = Graph()
    sum = 1
    for v in g:
        sum +=1
    visited = sum * [0]
    #print(t)
    
    #weight = 0
    next = 1
    #print("LENG", len(g))
    while(next >= 1):
        if visited[next]!= 1:
            visited[next] = 1 # mark current node visited
            #print(next, t[next])
            #print("s is ", s)
            for neighbor in t[next]: # for the next node
                if visited[neighbor] != 1: # if its not visited
                    #print("pee",next, neighbor)
                    s[next][neighbor] = t[next][neighbor] # add to list
                    #weight += t[next][neighbor]
                    next = neighbor # now explore neighbor
                    break
                # else:
                #     next = -1
        else: 
            for vertex in g:
                
                #print("sdf", vertex)
                if visited[vertex] != 1:
                    #print(next)
                    s[next][vertex] = g[next][vertex] # add to list
                    #weight += g[next][neighbor]
                    next = vertex # now explore neighbor
                    break
                if vertex == len(g):
                    s[next][1] = g[next][1]
                    #weight += g[next][1]
                    return s#, weight
            
    #print("NOOOO")
    return s
    
def print_approximation(g):
    #print(g)
    weight = 0
    for vertex in g:
        for neighbor in g[vertex]:
            weight += g[vertex][neighbor]
    print("Hamiltonian cycle of weight " + str(weight) + ":")
    print(", ".join(str(key) for key in g)+ ", 1")

def sorted_graph(f_name):
    g = Graph()
    f = open(f_name, "r")
    file_list = []
    for line in f:
        l = line.split()
        l = list(map(int, l)) 
        file_list.append(l)  
    f.close()
    file_list = sorted(file_list, key = lambda a: a[2])
    for vertex in file_list:
        g.add_edge(vertex[0], vertex[1], vertex[2])
    return g, file_list

def main():
    g, edge_list = sorted_graph(sys.argv[1])
    t = kruskals(g, edge_list)
    res = skip_duplicate_vertices(t, g)
    print_approximation(res)
    
if __name__ == "__main__":
    main()
