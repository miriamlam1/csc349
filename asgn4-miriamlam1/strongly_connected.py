# kosaraju's strongly connected algorithm
# input: a directed graph given in a list of edges connecting vertices
# output: lists of each vertex in a strongly connected component

from collections import defaultdict
import sys


def transpose(g):
    transposed = defaultdict(list)
    for i in g:
        for j in g[i]:
            transposed[j].append(i)
    return transposed


def dfs(g, v, visited_list, stack):
    if visited_list[v] == 0:
        visited_list[v] = 1
        for neighbor in g[v]:
            dfs(g, neighbor, visited_list, stack)
        stack = stack.append(v)


def visit2(g, visited_list, vertices_list):
    stack = []
    for v in vertices_list:
        dfs(g, v, visited_list, stack)
    return stack


def strongly_connected(g, vertices_list):
    visited_list = [0] * (len(vertices_list) + 1)
    stack = visit2(g, visited_list, vertices_list)
    transposed = transpose(g)
    visited_list = [0] * (len(vertices_list) + 1)

    scc = []
    while stack:
        v = stack.pop()
        if (visited_list[v] == 0):
            component = []
            dfs(transposed, v, visited_list, component)
            scc.append(component)

    print("%d Strongly Connected Component(s):" % len(scc))
    for i in range(len(scc)):
        print(str(scc[i]).strip('[]'))


def get_graph(file):
    f = open(file, "r")
    g = defaultdict(list)
    vertices_list = []
    for line in f:
        line = line.split()
        if line[0] not in vertices_list:
            vertices_list.append(int(line[0]))
        if line[1] not in vertices_list:
            vertices_list.append(int(line[1]))
        g[int(line[0])].append(int(line[1]))
    f.close()
    return g, vertices_list


def main():
    g, vertices_list = get_graph(sys.argv[1])
    strongly_connected(g, vertices_list)


if __name__ == "__main__":
    main()
