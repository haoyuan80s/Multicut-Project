import pickle
import graph
import LP_relax as LP
import region_growing as rg
import naive as na
import random; random.seed(1)

# random graph
# G = graph.Graph(n = 100, p = 0.3,st = [(0,1),(2,3)])

# a naive grid
#dc = {0: [3,1],1:[2,0,4],2:[1,12,5],3:[0,4],4:[1,3,5],5:[2,4],10:[11],11:[10],12:[2] }
#G = graph.Graph(graph_dict = dc,st = [(0,1),(2,4)])
dc = {0: [1,2,3,4,5,6,7,8],1: [0],2: [0],3: [0],4: [0],5: [0],6: [0],7: [0],8: [0]}
G = graph.Graph(graph_dict = dc, st = [(1,2),(3,4),(5,6),(7,8)])
# facebook data 348.edges cf. https://snap.stanford.edu/data/egonets-Facebook.html
#pickle_in = open("facebook.pickle", "rb")
#g_dic = pickle.load(pickle_in)
#G = graph.Graph(graph_dict = g_dic, st = [(525, 528),(526, 549)])

LP_sol =  LP.multi_cut_LP_relax(G)
pickle_out = open("LP_result","wb")
pickle.dump(LP_sol, pickle_out)
pickle_out.close()
print LP_sol

#print rg.region_growing(G)
#print na.multi_cut_native(G)


