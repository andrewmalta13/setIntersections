import networkx as nx
import random

def arbitrary_element(arr):
    return arr[random.randint(0, len(arr) - 1)]


def max_clique(G):
    clique = set()
    subgraph = G

    while len(subgraph.nodes()) > 0:
        node = arbitrary_element(subgraph.nodes())
        nbrs = nx.neighbors(subgraph, node)
        clique.add(node)
        subgraph = subgraph.subgraph(nbrs)

        if node in subgraph.nodes():
            subgraph.remove_node(node)


    return clique




