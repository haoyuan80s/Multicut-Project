#import pickle
import graph
import LP
#import region_growing as rg
import naive as na
#import random; random.seed(1)
import time
# random graph


# small case IP: random case
# with open("IP_solvable.txt",'w') as f:
#     times = {}
#     for i in range(16):
#         G = graph.Graph(n = i, p = 0.4,st = [(0,1),(2,3)])
#         a = time.time()
#         IP_sol = na.multi_cut_native(G)
#         b = time.time()
#         times[i] = b - a
#         f.write(str(i) + ", " + str(b - a) + "\n")




### { grid graph with lots of fractional values
### To modify the grid graph, go to grid_graph.py for details 
# import grid_graph
# N = 10
# L = 11
# k = 3
# p = 0.3
# 
# (G,M) = grid_graph.random_grid_graph(N,L,k,p)
import grid_graph as gg
import random
random.seed(2) # makes no sense
N = 12
L = 7
k = 12
G = gg.grid_graph(N,L)
M = gg.random_sts(G,N,L,k)
x =  LP.solve(G)
H = graph.copy_graph(G,x)
print "LP objective value: ",
print G.objective(x)
from pprint import pprint
pprint(G.sts())
print len(G.edges())
### }



# a naive grid
#dc = {0: [3,1],1:[2,0,4],2:[1,5],3:[0,4],4:[1,3,5],5:[2,4]}
#G = graph.Graph(graph_dict = dc,st = [(0,1),(2,4)])
#dc = {0: [1,2,3,4,5,6,7,8],1: [0],2: [0],3: [0],4: [0],5: [0],6: [0],7: [0],8: [0]}
#G = graph.Graph(graph_dict = dc, st = [(1,2),(3,4),(5,6),(7,8)])
# facebook data 348.edges cf. https://snap.stanford.edu/data/egonets-Facebook.html
#pickle_in = open("facebook.pickle", "rb")
#g_dic = pickle.load(pickle_in)
#G = graph.Graph(graph_dict = g_dic, st = [(525, 528),(526, 549)])
#LP_sol =  LP2.multi_cut_LP_relax(G)
#print LP_sol 
#LP_sol1 =  LP.multi_cut_LP_relax(G)
#print LP_sol1

import RG_dbg
Fs = RG_dbg.solve(G,H)
F = Fs[-1]
print "ALG objective value: ",
print len(F)
#print na.multi_cut_native(G)
#G.add_edge((0, 3))
#print G



### { uncomment this part for visualizing grid graph cuts 
### Output the results into the html files fractional.html and integral.html
from visualize_grid_graph import vgg, fill, vgganimate
def getCuts(F):
    return {e: (1 if e in F else 0) for e in G.edges()} 
vgg(G, N, L,k, x, M,'fractional.html')

cuts_series = map(getCuts,Fs)
vgganimate(G,N,L,k,cuts_series,M,'animateRG.html')
vgg(G, N, L,k, cuts_series[-1], M,'integral.html')
### }

