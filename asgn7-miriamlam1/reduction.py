# Assignment 7: Reductions
# By Miriam Lam
# Input: 
# Output: 3 sat

import sys
import re
from graph import Graph
from subgraph_isomorphism import isomorphic_subgraph


''' input: a graph G and a natural number k
    output: a clique on k vertices within G, if one exists
'''

def clique(g, k):
    h = Graph() # let h be arbitrary clique of size k
    for i in range(k):
        h.add_vertex(i)
        for j in range(k):
            if j!= i:
                h.add_edge(i, j)
    # transform the instance of clique into an instance of subgraph_isomorphism
    return isomorphic_subgraph(g, h)
    # transform the solution to subgraph_isomorphism to a solution for clique


def get_graph(file):
    g = Graph()
    k = 0 # number of clauses

    f = open(file, "r")
    for line in f:
        statement = line.split()
    f.close()

    for word in statement:
        if (word == '('):
            k += 1
        if (word[0] == '~' or word[0].isalpha()):
            g.add_vertex(word+str(k))

    for vertex in g:
        for neighbor in g:
            if (vertex[:len(vertex)-1] != '~'+neighbor[:len(neighbor)-1] 
            and '~'+vertex[:len(vertex)-1] != neighbor[:len(neighbor)-1] and 
            vertex[len(vertex)-1] != neighbor[len(neighbor)-1]):
                g.add_edge(vertex,neighbor)

    return g, k
    

def main():
    g, k = get_graph(sys.argv[1])
    # g = Graph.from_file(sys.argv[1])
    result = clique(g, k)
    if result == None:
        print("No satisfying assignments.")
    else:
        print_list = []
        print("Satisfying assignment:")
        for v in result:
            temp = v[:len(v)-1]
            if temp not in print_list:
                print_list.append(temp)
        print_list = sorted(print_list, key = lambda a:(a[1:] if a[0] == "~" else a))
        print(", ". join(print_list))

if __name__ == "__main__":
    main()