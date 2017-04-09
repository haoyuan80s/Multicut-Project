import graph
import region_growing as rg
import multi_cut_naive as na
import random; random.seed(1)
G = graph.Graph(n = 15, p = 0.3,st = [(0,1),(2,3)])
#G.remove_edges([(0,14),(5,12)])
#dc = {0: [1,2], []}
#dc = {0: [1,3],1:[0,2,4],2:[1,5],3:[0,4],4:[1,3,5],5:[2,4] }
#G = graph.Graph(graph_dict = dc,st = [(0,1),(2,4)])
#print G.is_connected(0,5)
#print rg.region_growing(G)
print na.multi_cut_native(G)
