"""Naive brute force solution to the subgraph isomorphism problem."""
# NOTE: Do not alter this file.
# CSC 349 Assignment 7
import argparse
import itertools

from typing import Optional

from graph import Graph

parser = argparse.ArgumentParser()
parser.add_argument('g_file')
parser.add_argument('h_file')


def isomorphic_subgraph(graph_g: Graph, graph_h: Graph) -> Optional[Graph]:
    """Finds a subgraph of g isomorphic to h if one exists.

    Args:
        graph_g: The graph g.
        graph_h: The graph h.

    Returns:
        The subgraph of g isomorphic to h if one exists, None otherwise.
    """

    # Look at all possible subgraphs and all vertex orders of g with the
    # same number of vertices as h.
    for g_vertices in itertools.permutations(graph_g, len(graph_h)):
        relabel = dict(zip(graph_h, g_vertices))
        relabeled_h = Graph(
            (relabel[vert], {relabel[neighbor] for neighbor in graph_h[vert]})
            for vert in graph_h)

        # If all edges in h are also in g (after relabeling h), then h
        # is isomorphic to the subgraph of g with those vertices (and
        # the edges from h).
        if all(relabeled_h[vert] <= graph_g[vert] for vert in relabeled_h):
            return relabeled_h

    return None


def main(g_file: str, h_file: str) -> None:
    """Finds and prints the subgraph of g isomorphic to h if one exists.

    Args:
        g_file: The file containing g (as an edge list).
        h_file: The file containing h (as an edge list).
    """
    graph_g = Graph.from_file(g_file)
    graph_h = Graph.from_file(h_file)

    subgraph = isomorphic_subgraph(graph_g, graph_h)

    if subgraph:
        print('Isometric vertices:')
        print(*sorted(subgraph), sep=', ')
    else:
        print('No isometric vertices.')


if __name__ == '__main__':
    args = parser.parse_args()
    main(args.g_file, args.h_file)