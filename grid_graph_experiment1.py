#import pickle
import graph
import LP_relax_v2 as LP2
#import region_growing as rg
import naive as na
#import random; random.seed(1)
import time
# random graph


### { grid graph with lots of fractional values
### To modify the grid graph, go to grid_graph.py for details 
import grid_graph
N = 10
L = 12
k = 3
p = 0.3

(G,M) = grid_graph.random_grid_graph(N,L,k,p)
import LP
x =  LP.solve(G)
print "LP objective value: "
print G.objective(x)
H = graph.copy_graph(G,x)
### }

import RG
F = RG.solve(G,H)
print "ALG objective value: ",
print len(F)
#print na.multi_cut_native(G)
#G.add_edge((0, 3))
#print G



### { uncomment this part for visualizing grid graph cuts 
### Output the results into the html files fractional.html and integral.html
from visualize_grid_graph import vgg, fill 
cuts = {e: (1 if e in F else 0) for e in G.edges()} 
vgg(G, N, L, x, M,'fractional.html')
vgg(G, N, L, cuts, fill(H,M),'integral.html')
### }

