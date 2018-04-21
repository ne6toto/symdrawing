import numpy as np
import networkx as nx
import argparse
import sys
import os
from matplotlib import pyplot as plt
import math
from partA import draw_reflection
from partB import draw_rotation

def load_graph(filename):
    f = open(filename)
    info = f.read().split("-------------------------------------------")
    adj = [ [int(x) for x in item[1:-1].split(",")] for item in info[1].strip().split("\n") ]
    aut = [ [int(x)-1 for x in item[1:-1].split(",")] for item in info[3].strip().split("\n") ]
    matrix = np.matrix(adj)
    graph = nx.from_numpy_matrix(matrix)
    return graph, aut

#matrix = np.matrix([[0,1,0,0,0,0,0,0,1,1,0],[1,0,1,0,0,1,0,0,0,0,0],[0,1,0,1,0,0,0,1,0,0,0],[0,0,1,0,1,0,0,0,0,0,1],[0,0,0,1,0,1,0,0,1,0,0],[0,1,0,0,1,0,1,0,0,0,0],[0,0,0,0,0,1,0,1,0,0,1],[0,0,1,0,0,0,1,0,1,0,0],[1,0,0,0,1,0,0,1,0,0,0],[1,0,0,0,0,0,0,0,0,0,1],[0,0,0,1,0,0,1,0,0,1,0]])
#graph2 = nx.from_numpy_matrix(matrix)
#aut2 = [[2,9],[3,8],[4,7],[5,6]]
#draw_reflection(graph, aut)
#print find_fixed_points(graph, aut)

"""
graph, aut = load_graph("garnick11b.txt")
draw_reflection(graph, aut)
#"""

"""
graph, aut = load_graph("demoG32c.txt")
#print graph.nodes()
#print graph.edges()
#print aut
#print "STARTING ALG"
#draw_rotation(graph, aut)
#"""

#"""
graph, aut = load_graph("garnick11b.txt")

#"""

print graph.nodes()
print graph.edges()
print aut

# an automorphism is an isomorphism of a graph to itself
GM = nx.algorithms.isomorphism.GraphMatcher(graph,graph)
print GM.is_isomorphic()
automorphs = GM.isomorphisms_iter()
# GraphMatcher returns automorphism generators as dictinaries
# we shall transform them into the more standard version of arrays of arrays.
for morph in automorphs:
    print "----"
    formated = []
    added_so_far = []
    for elem in morph.keys():
        if elem not in added_so_far and morph[elem] != elem:
            to_add = [elem]
            added_so_far.append(elem)
            cursor = morph[elem]
            while cursor != elem:
                to_add.append(cursor)
                added_so_far.append(cursor)
                cursor = morph[cursor]
            formated.append(to_add)
    if formated != []:
        print formated
