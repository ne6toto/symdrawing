import argparse
import sys
import os
import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
#python main.py cs -prob -t 0.4 ../../../data/data_with_probabilities/adenine/adenine.txt -img
#This adds the necessary directories to find the other modules.
#current = os.getcwd()
#outer = os.path.dirname(os.getcwd())
#sys.path.append(current)
#sys.path.append(outer)



#import src.utils.verbose as verbose
#import src.utils.fileIO as io
#import src.parsing.cfm_annotate_parser as cfm_parse

def main():
    """
    some forays into networkx
    """

    #im = np.array([[0, 1, 0, 1],[1,0,1,0],[0,1,0,0],[1,0,1,0]]) #incidence matrix
    #am = (np.dot(im,im.T) > 0).asType(int) #adjacency matrix


    G=nx.Graph()
    positions = {1:(0,0), 2:(1,0), 3:(1,1), 4:(0,1)}
    #G.add_nodes_from([1,2,3,4,5,6,7,8,9,10,11])
    #G=nx.from_numpy_matrix(am)
    G.add_nodes_from(positions.keys())
    A=np.matrix([[0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],[0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0],[0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0],[0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0],[0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0],[0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0],[0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],[0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0],[0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0],[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0]])
    #G.add_edge(1,2)
    #G.add_edge(3,2)
    #G.add_edge(3,1)
    #G.add_edge(4,1)
    #G.add_edge(2,4)
    #G.add_edge(4,3)
    #G=nx.from_numpy_matrix(A)
    nx.draw(G,positions)
    #print G.edges()
    plt.show()
    print "done"

    #nx.draw(G,with_labels=True)

main()
