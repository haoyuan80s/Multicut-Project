import pickle
import graph
import LP
import RG
import IP_v2 as IP
import grid_graph

N = 5
L = 5
k = 3
p = 0.3

import random; random.seed(2)
(G,M) = grid_graph.random_grid_graph(N,L,k,p)

# G = graph.Graph(n=60,p=0.3, st = [(0,1),(2,3),(4,5)])
x_LP =  LP.solve(G)
OPT_LP =  G.objective(x_LP)
H = graph.copy_graph(G,x_LP)
### }

# 
# x_IP = IP.solve(G)
# OPT_IP = G.objective(x_IP)
# 



F = RG.solve(G,H)
ALG = len(F)



print "LP objective value: ",
print OPT_LP
# 
# print "IP objective value: ",
# print OPT_IP
# 
print "ALG objective value: ",
print ALG


### { uncomment this part for visualizing grid graph cuts 
### Output the results into the html files fractional.html and integral.html
from visualize_grid_graph import vgg, fill 
cuts = {e: (1 if e in F else 0) for e in G.edges()} 
vgg(G, N, L, x_LP, M,'fractional.html')
vgg(G, N, L, cuts, fill(H,M),'integral.html')
### }
