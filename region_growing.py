import graph
import LP_relax as LP
import random

import math
# requires an networkx Graph G
def region_growing(G,d,st_pairs):
    L = sum([c[e]*x[e] for e in G.edges()])
    beta = 1.0/len(st_pairs)
    
    # k = 2
    # G = graph.Graph(n = 4, p = 1)
    def dist(u,v): # the inputs are two vertices
        if u == v: 
            return 0
        else:
            try:
                return d[(u,v)]
            except:
                return d[(v,u)]

    def ball(s,r):
        return [x for x in G.nodes() if dist(x,s) <= r]
    
    def is_boundary(e,B):
        # check if an e is in the boundary of a set b or not
        # otherwise, return None
        (u,v) = e

    def get_node_in_set(e,B):
        if is_boundary(e,B) == False:
            raise
        (u,v) = e
        if (u in b and v not in B):
            return u
        return v


    def is_internal(e,B):
        # check if e is internal to b
        (u,v) = e
        return (u in B and v in B)

    def boundary(s,r):
        delta = []
        b = ball(s,r)
        for e in G.edges():
            if is_boundary(e,b):
                delta.append(e)
        return delta
    
    def volume(s,r):
        B = ball(s,r)
        return (beta*L
                +sum([c[e]*x[e] for e in G.edges() 
                    if is_internal(e,B)])
                +sum([c[e]*(r-dist(s,get_node_in_set(e,B))) for e in G.edges() 
                    if is_boundary(e,B)])
                )
    def cost(B):
        return sum([c[e] for e in B])

    F = []
    for s,t in st_pairs:
        if nx.has_path(G, s, t): #2*i is soure_i
            print "called"
            r = 0
            for r_try in set(d.values()):
                if cost(boundary(s,r)) <= volume(s,r)*2*math.log((beta+1)/beta):
                    r = r_try
                    break
                
            B = boundary(s,r)
            #import pdb; pdb.set_trace()
            F = F + B
            G.remove_edges_from(B)
    return F

