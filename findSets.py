import networkx as nx
import pickle as pkl
from approxMaxClique import max_clique


# generate a binary string that represents the edges in a subgraph of 
# the graph g in main.
def num_to_bit_string(num, bs_dict):
    tmp = bin(num)[2:]
    return ("0" * (len(bs_dict) - len(tmp))) + tmp
    
# returns true if the two bitstring representations of a graph share a path
# of at least length 3.
def shares_path(num1, num2, g, bs_dict):
    intersection = num1 & num2
    bitstring = num_to_bit_string(intersection, bs_dict)

    if sum([int(val) for val in bitstring]) > 4:
        return True

    # bs1 = num_to_bit_string(num1, bs_dict)
    # bs2 = num_to_bit_string(num2, bs_dict)
    # g1 = graph_from_bitstring(bs1, bs_dict, g)
    # g2 = graph_from_bitstring(bs2, bs_dict, g)
    
    # if len(g1.edges()) < 6 or len(g2.edges()) < 6:
    #     return False

    G = graph_from_bitstring(bitstring, bs_dict, g)

    for edge in G.edges():
        src, dest = edge
        n1, n2 = set(G.neighbors(src)), set(G.neighbors(dest))
        if len(n1) >= 2 and len(n2) >= 2 and len(n1.union(n2)) >= 4:
            return True

    return False

# create a graph with the same number of nodes as g from the 
# the specified bitstring using the edge numbering specified
# in the bs_dict dictionary.
def graph_from_bitstring(bitstring, bs_dict, g):
    G = nx.Graph()
    G.add_nodes_from(g.nodes())

    for i, b in enumerate(bitstring):
        if b == "1":
            src, dest = bs_dict[i]
            G.add_edge(src, dest)

    return G


def gen_bitstring_dict(g):
    d = {}
    for i, e in enumerate(g.edges()):
        d[i] = e

    return d

def gen_pairs(m):
    for i in xrange(2**m):
        for j in xrange(i, 2**m):
            yield (i, j)

if __name__ == "__main__":
    max_len = -float("inf")
    for _ in xrange(100):
        print "Random graph number: {}".format(_ + 1)
        g = nx.gnm_random_graph(6, 9)
        m = len(g.edges())
        n = len(g.nodes())
        bs_dict = gen_bitstring_dict(g)

        BigBoi = nx.Graph()
        BigBoi.add_nodes_from(range(2**m))

        # print_count = 0
        for pair in gen_pairs(m):
            # if print_count % 100000 == 0:
                # print "completed {}".format(print_count / float(2**m))

            # print_count += 1
            if shares_path(pair[0], pair[1], g, bs_dict):
                BigBoi.add_edge(pair[0], pair[1])

      
        # for _ in xrange(10000):
        for clique in nx.algorithms.find_cliques(BigBoi):
            # clique = max_clique(BigBoi)
            if len(clique) > max_len:
                for n in clique:
                    print num_to_bit_string(n, bs_dict)
                max_len = len(clique)
                print float(len(clique))
    print max_len


