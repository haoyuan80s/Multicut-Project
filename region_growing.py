import graph
import LP_relax as LP
import random

def region_growing(G):
    """return the cuts F following the region_growing alg in sec 8.2 approx book"""
    d = LP.multi_cut_LP_relax(G)
    def dist(u,v):
        """return d-incuded-distance between u,v"""
        if u == v: 
            return 0
        else:
            return d[( min(u,v),max(u,v) )]

    def ball(s,r):
        """return vertices in ball(s,r)"""
        return [x for x in G.vertices() if dist(x,s) <= r]

    def boundary(s,r):
        """return boundary edges in ball(s,t)"""
        delta = []
        b = ball(s,r)
        for u,v in G.edges():
            if (u in b and v not in b) or (v in b and u not in b):
                delta.append((u,v))
        return delta

    def discretize_r():
        """return possive critical r values where F may change"""
#        import pdb; pdb.set_trace()
        rs = []
        for s,t in G.sts():
            for v in G.vertices():
                d = dist(s,v)
                if d not in rs and d < 1.0/2:
                   rs.append(d)
        rs.sort()
        return rs
    
    def get_F(r):
        """return F(r) c.f. alg 8.2 in approx alg book"""
        F = []
        for s,t in G.sts():
            if G.is_connected(s, t):
                B = boundary(s,r)
                F = F + B
                G.remove_edges(B)
        return F

    # return the smallest F(r)
    F = G.edges()
    for r in discretize_r():
        FF = get_F(r)
        if len(FF) < len(F): 
            F = FF

    return F
