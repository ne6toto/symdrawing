import numpy as np
import networkx as nx
import argparse
import sys
import os
from matplotlib import pyplot as plt
import math

def load_graph(filename):
    f = open(filename)
    info = f.read().split("-------------------------------------------")
    adj = [ [int(x) for x in item[1:-1].split(",")] for item in info[1].strip().split("\n") ]
    aut = [ [int(x)-1 for x in item[1:-1].split(",")] for item in info[3].strip().split("\n") ]
    matrix = np.matrix(adj)
    graph = nx.from_numpy_matrix(matrix)
    return graph, aut

def find_fixed_points(graph, autogroup):
    fixed = [node for node in graph.nodes() if node not in reduce(lambda x,y: x+y, aut)]
    return fixed

def get_orbit_positions(aut):
    orbit_pos = {}
    num_orbits = len(aut)
    # add each element in the orbit to an equally-spaced position wrt y-axis
    # on the outer circle
    dy = 2.0 / (num_orbits+1)
    print dy
    for i in range(num_orbits):
        # equally space y and set x so that they are on circle
        y = 1.0 - dy*(i+1)
        # this is well defined in I and IV quadrant
        x = math.cos(math.asin(y))
        orbit_pos[aut[i][0]] = (x,y)
        orbit_pos[aut[i][1]] = (-x,y)
    return orbit_pos

def get_orbit_positions_arclength(aut):
    orbit_pos = {}
    num_orbits = len(aut)
    # add each element in the orbit to an equally-spaced position
    # on the outer circle
    dy = math.pi / (num_orbits+1)
    print dy
    for i in range(num_orbits):
        # equally space y and set x so that they are on circle
        angle = math.pi/2 - dy*(i+1)
        # this is well defined in I and IV quadrant
        x = math.cos(angle)
        y = math.sin(angle)
        orbit_pos[aut[i][0]] = (x,y)
        orbit_pos[aut[i][1]] = (-x,y)
    return orbit_pos

def get_fixed_positions(graph, aut):
    fixed_pos = {}
    fix_g = find_fixed_points(graph, aut)
    num_fixed = len(fix_g)
    dy = 2.0 / (num_fixed-1)
    subgraph = graph.subgraph(fix_g)
    i = 0
    for edge in subgraph.edges():
        fixed_pos[edge[0]] = (0, 1.0 - dy * i)
        i += 1
        fixed_pos[edge[1]] = (0, 1.0 - dy * i)
        i += 1
    for vertex in fix_g:
        if vertex not in fixed_pos:
            fixed_pos[vertex] = (0, 1.0 - dy * i)
            i += 1
    return fixed_pos

def draw_reflection(graph, autogroup):
    positions = {}
    # orbit points
    #positions.update(get_orbit_positions(autogroup))
    positions.update(get_orbit_positions_arclength(autogroup))
    # add fixed points
    positions.update(get_fixed_positions(graph, autogroup))
#    nx.draw(graph,positions,node_color='black',node_size=22)
    nx.draw_networkx(graph,positions)
    plt.show()
    #print positions
    print "done"

matrix = np.matrix([[0,1,0,0,0,0,0,0,1,1,0],[1,0,1,0,0,1,0,0,0,0,0],[0,1,0,1,0,0,0,1,0,0,0],[0,0,1,0,1,0,0,0,0,0,1],[0,0,0,1,0,1,0,0,1,0,0],[0,1,0,0,1,0,1,0,0,0,0],[0,0,0,0,0,1,0,1,0,0,1],[0,0,1,0,0,0,1,0,1,0,0],[1,0,0,0,1,0,0,1,0,0,0],[1,0,0,0,0,0,0,0,0,0,1],[0,0,0,1,0,0,1,0,0,1,0]])
graph2 = nx.from_numpy_matrix(matrix)
aut2 = [[2,9],[3,8],[4,7],[5,6]]
#draw_reflection(graph, aut)
#print find_fixed_points(graph, aut)

"""
graph, aut = load_graph("garnick11b.txt")
draw_reflection(graph, aut)
#"""

"""
graph, aut = load_graph("demoG32a.txt")
#print graph.nodes()
#print graph.edges()
#print aut
#print "STARTING ALG"
draw_reflection(graph, aut)
#"""
