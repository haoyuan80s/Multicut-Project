import graph
import LP_relax as LP
import random

def region_growing(G,k):
    # k = 2
    # G = graph.Graph(n = 4, p = 1)
    d = LP.multi_cut_LP_relax(G)
    def dist(u,v): # since our edge (u,v) always have u < v
        if u == v: 
            return 0
        else:
            return d[( min(u,v),max(u,v) )]

    def ball(s,r):
        return [x for x in G.vertices() if dist(x,s) <= r]

    def boundary(s,r):
        delta = []
        b = ball(s,r)
        for u,v in G.edges():
            if (u in b and v not in b) or (v in b and u not in b):
                delta.append((u,v))
        return delta

    F = []
    for i in range(k):
        s,t = 2*i, 2*i + 1

        if G.is_connected(s, t): #2*i is soure_i
            r = 1/3 # r < 1/2
            B = boundary(s,r)
            #import pdb; pdb.set_trace()
            F = F + B
            G.remove_edges(B)
    return F
