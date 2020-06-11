"""Provides an undirected Graph class.

The Graph class is iterable over its vertices.  For example, to iterate
over all edges in a graph, you may do:

graph = Graph()

# Fill in graph

for vertex in graph:
    for neighbor in graph[vertex]:
        # Do something
"""
# NOTE: Do not alter this file.
# CSC 349 Assignment 7


class Graph(dict):
    """A graph type using adjacency lists."""

    def __init__(self, *args, size: int = 0, start: int = 1, **kwargs):
        """Creates a graph.

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
        self[vertex] = set()
        return self[vertex]

    def add_vertex(self, vertex: int) -> None:
        """Adds a vertex to the graph if it doesn't already exist.

        Args:
            vertex: The vertex to add
        """
        self.setdefault(vertex, set())

    def add_edge(self, vertex1: int, vertex2: int) -> None:
        """Adds an undirected edge to the graph between vertex1 and
        vertex2.

        Args:
            vertex1: The first vertex
            vertex2: The second vertex
        """
        self[vertex1].add(vertex2)
        self[vertex2].add(vertex1)

    @classmethod
    def from_file(cls, file_name: str) -> 'Graph':
        """Reads and returns a graph from a file.

        The file is expected to be as an edge list.

        Args:
            file_name: The name of the file specifying the graph.

        Returns:
            The specified graph.
        """
        graph = cls()
        with open(file_name) as graph_file:
            for edge in graph_file:
                vertex1, vertex2 = (int(value) for value in edge.split())
                graph.add_edge(vertex1, vertex2)

        return graph