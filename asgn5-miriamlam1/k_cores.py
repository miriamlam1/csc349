# Assignment 5: Greedy Algorithms
# input: a graph as a list of vertices
# output: list of vertices in each k-core


from collections import defaultdict
import sys

sys.setrecursionlimit(10**8)


def dfs(v, visited, k, graph):
    if visited[v] == 0:  # not visited
        visited[v] = 1  # mark visited
        for neighbor in graph[v]:  # dfs through neighbors
            if len(graph[v]) <= k:  # if degree == k
                if v in graph[neighbor]:
                    graph[neighbor].remove(v)  # remove it from all neighbor's list
                    visited[neighbor] = 0
            dfs(neighbor, visited, k, graph)  # recurse


def print_k_core(degree, k):
    print_list = []
    for i in range(len(degree)):
        if len(degree[i]) > k:
            print_list.append(str(i))
    if print_list:
        print("Vertices in %d-cores:" % (k + 1))
        print(', '.join(print_list))
        return k + 1
    else:
        exit()


def k_core(degree):
    k = 0
    while(1):
        visited_list = [0] * (len(degree))  # init all v to not visited
        for v in range(len(degree)):  # for all vertices
            dfs(v, visited_list, k, degree)
        k = print_k_core(degree, k)


def get_graph(file):
    f = open(file, "r")
    degree = defaultdict(list)
    for line in f:
        line = line.split()
        degree[int(line[0])].append(int(line[1]))
        degree[int(line[1])].append(int(line[0]))
    f.close()
    degree = dict(sorted(degree.items()))
    graph = [[]] + [v for k, v in degree.items()]
    return graph


def main():
    degree = get_graph(sys.argv[1])
    k_core(degree)


if __name__ == "__main__":
    main()