import math
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(G):
    pos = {}

    nodes = G.nodes()
    num = len(nodes)
    for n in nodes:
        pos[n] = (math.cos(2*math.pi * n / num), math.sin(2*math.pi * n / num))

    nx.draw(G, pos = pos)
    plt.draw()
    plt.show()


def draw_2_graphs(g1, g2):
    pos = {}
    pos2 = {}

    nodes = g1.nodes()
    num = len(nodes)
    for n in nodes:
        pos[n] = (math.cos(2*math.pi * n / num), math.sin(2*math.pi * n / num))
        pos2[n] = (pos[n][0] + 3, pos[n][1])

    nx.draw(g1, pos = pos)
    nx.draw(g2, pos = pos2)
    plt.draw()
    plt.show()

