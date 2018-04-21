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

def angle_to_xy(theta):
    if theta >=0 and theta <= math.pi:
        y = math.sin(theta)
    else:
        y =  math.sin(theta)
    if theta >= math.pi/2 and theta <= 3*math.pi/2:
        x =  math.cos(theta)
    else:
        x = math.cos(theta)
    return x,y

def get_orbit_positions(aut):
    print "aut", aut
    orbit_pos = {}
    num_orbits = len(aut)
    orbit_size = len(aut[0])
    # add each element in the orbit to a location at 2pi(i + jn/k)/n.
    for i in range(num_orbits):
        for j in range(orbit_size):
            # place elements of the orbits, so that they are on a circle
#            theta = 2*math.pi*(i + j*num_orbits)/(num_orbits * (orbit_size))
            theta = 2*math.pi*(i + j*(num_orbits+1))/((num_orbits+1) * (orbit_size))            
            # get cartesian coordinates
            x,y = angle_to_xy(theta)
#            print theta*180/math.pi, x,y
            orbit_pos[aut[i][j]] = (x,y)
            #orbit_pos[aut[i][1]] = (-x,y)
    return orbit_pos

def get_orbit_positions_with_space(aut):
    print "aut", aut
    orbit_pos = {}
    num_orbits = len(aut)
    orbit_size = len(aut[0])
    num_of_locations = ((num_orbits+1) * (orbit_size))+2
    phi = 2*math.pi / num_of_locations
    sector_size = 2*math.pi / orbit_size
    # add each element in the orbit to a location at 2pi(i + jn/k)/n.
    for j in range(orbit_size):
        for i in range(num_orbits):
            # place elements of the orbits, so that they are on a circle
#            theta = 2*math.pi*(i + j*num_orbits)/(num_orbits * (orbit_size))
            theta = phi * i + j*sector_size            
            # get cartesian coordinates
            x,y = angle_to_xy(theta)
#            print theta*180/math.pi, x,y
            orbit_pos[aut[i][j]] = (x,y)
            #orbit_pos[aut[i][1]] = (-x,y)
    return orbit_pos


"""
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
#"""

def get_fixed_positions(graph, aut):
    fixed_pos = {}
    fix_g = find_fixed_points(graph, aut)
    num_fixed = len(fix_g)
    if num_fixed > 1:
        print "Error",
    dy = 2.0 / (num_fixed-1)
    for i in range(num_fixed):
        fixed_pos[fix_g[i]] = (0,0)
    return fixed_pos

def draw_dihedral(graph, autogroup):
    positions = {}
    # orbit points
#    print "orbit", get_orbit_positions(autogroup).keys()
    #positions.update(get_orbit_positions(autogroup))
    positions.update(get_orbit_positions(autogroup))
    # add fixed points
#    print "fixed", get_fixed_positions(graph,autogroup).keys()
    positions.update(get_fixed_positions(graph, autogroup))
    print positions.keys()
#    nx.draw(graph,positions,node_color='black',node_size=22)
    
    fig = plt.figure()
    fig.set_figheight(8)
    fig.set_figwidth(8)
#    plt.figaspect(1.0)
    nx.draw_networkx(graph,positions)
#    fig.savefig("partB2.png", format="PNG", bbox_inches="tight")

#    plt.savefig("partC.png", format="PNG", bbox_inches="tight")
    plt.show()
#    print positions
    print "done"

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
draw_rotation(graph, aut)
#"""

#"""
graph, aut = load_graph("garnick11b.txt")
draw_dihedral(graph, aut)
#"""
