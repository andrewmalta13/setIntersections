from drawGraph import *
from findSets import *
import random
import networkx as nx

# takes in a bit string for a graph of 6 nodes and returns
# the bitstring of the rotation of this graph in a 
def rotate(bs):
    rotation_dict = {0:5, 5:9, 9:12, 12:14, 14:4, 4:0,
                     1:10, 10:3, 3:1,
                     6:13, 13:8, 8:6,
                     2:11, 11:7, 7:2}

    new_string = ""
    for i in xrange(len(bs)):
        new_string += bs[rotation_dict[i]]

    return new_string


def filter_bitstrings(filter_string, bitstrings):
    new_bitstrings = []

    for b in bitstrings:
        for i in xrange(len(b)):
            if filter_string[i] > b[i]:
                new_bitstrings.append(b)
                break

    return new_bitstrings, set(new_bitstrings)

def shares_path(bs1, bs2, g, bs_dict):
    g1 = graph_from_bitstring(bs1, bs_dict, g)
    g2 = graph_from_bitstring(bs2, bs_dict, g)
    
    G = nx.intersection(g1, g2)

    for edge in G.edges():
        src, dest = edge
        n1, n2 = set(G.neighbors(src)), set(G.neighbors(dest))
        if len(n1) >= 2 and len(n2) >= 2 and len(n1.union(n2)) >= 4:
            return True

    return False

if __name__ == "__main__":
    with open("clique1", "r") as f:
        bitstrings = f.read().split("\n")


    # bitstrings = sorted(bitstrings, key=lambda x: sum([int(i) for i in x]))
    # bitstrings_set = set(bitstrings)

    # while len(bitstrings) > 0:
    #     string = bitstrings[0]

    #     indices = []
    #     tmp = bitstrings
    #     for i in xrange(6):
    #         if string in bitstrings_set:
    #             indices.append(i)
    #             bitstrings, bitstrings_set = filter_bitstrings(string, bitstrings)

    #         string = rotate(string)

    #     print "{}, {}: {}".format(string, sum([int(i) for i in string]), indices)
        # draw_graph(graph_from_bitstring(string))

    g = nx.complete_bipartite_graph(3,3)
    compg = nx.complete_graph(6)
    m = len(g.edges())
    n = len(g.nodes())
    bs_dict = gen_bitstring_dict(compg)
    # for _ in xrange(100):
    #     r1 = random.randint(0, len(bitstrings) - 1)
    #     r2 = random.randint(0, len(bitstrings) - 1)
    #     if r1 != r2:
    #         g1 = graph_from_bitstring(bitstrings[r1], bs_dict, g)
    #         g2 = graph_from_bitstring(bitstrings[r2], bs_dict, g)
    #         # draw_2_graphs(g1, g2)
    #         draw_graph(nx.intersection(g1,g2))

    count = 0
    s = set()
    for bs in bitstrings:
        for bs2 in bitstrings:
            if not shares_path(bs, bs2, g, bs_dict):
                # g1 = graph_from_bitstring(bs, bs_dict, g)
                # g2 = graph_from_bitstring(bs2, bs_dict, g)
                # draw_2_graphs(g1, g2)
                count += 1
    print len(s)










       






