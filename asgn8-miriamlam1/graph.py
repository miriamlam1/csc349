"""Provides an undirected weighted Graph class.

The Graph class is iterable over its vertices.  For example, to iterate
over all edges in a graph, you may do:

graph = Graph()

# Fill in graph

for vertex in graph:
    for neighbor in graph[vertex]:
        # Do something
"""
# NOTE: Do not alter this file.
# CSC 349 Assignment 8


class Graph(dict):
    """A graph type using adjacency lists."""

    def __init__(self, *args, size: int = 0, start: int = 1, **kwargs):
        """Creates a weighted graph.

        If specified, the graph will be initialized with `size` vertices
        starting from `start`.

        Args:
            size: the initial number of vertices to create
            start: the number of the first vertex
        """
        super().__init__(*args, **kwargs)

        if size:
            for vertex in range(start, start + size):
                self.add_vertex(vertex)

    # Trying to access a vertex in the graph will create it if it didn't
    # already exist.
    def __missing__(self, vertex):
        self[vertex] = {}
        return self[vertex]

    def add_vertex(self, vertex: int) -> None:
        """Adds a vertex to the graph if it doesn't already exist.

        Args:
            vertex: The vertex to add
        """
        self.setdefault(vertex, {})

    def add_edge(self, vertex1: int, vertex2: int, weight: int) -> None:
        """Adds an undirected weighted edge to the graph between the
        given vertices of the given weight.

        Args:
            vertex1: The first vertex
            vertex2: The second vertex
            weight: The weight of the edge
        """
        self[vertex1][vertex2] = weight
        self[vertex2][vertex1] = weight

    @classmethod
    def from_file(cls, file_name: str) -> 'Graph':
        """Reads and returns a graph from a file.

        The file is expected to be as an edge list with weights.

        Args:
            file_name: The name of the file specifying the graph.

        Returns:
            The specified graph.
        """
        graph = cls()
        with open(file_name) as graph_file:
            for edge in graph_file:
                vert1, vert2, weight = (int(value) for value in edge.split())
                graph.add_edge(vert1, vert2, weight)

        return graph
