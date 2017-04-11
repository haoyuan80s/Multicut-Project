import graph
import math

# G is original graph with weights c, H is the LP solution graph with weights x*
def solve(G,H):
    c = G.weights()
    x = H.weights()
    
    L = sum([c[e]*x[e] for e in G.edges()])
    beta = 1.0/len(G.sts())
    
    def volume(d_s,r):
        B = [v for v in G.vertices() if d_s[v] <= r]
        Bs = frozenset(B)
        dB = [e for e in H.edges() if len(e & Bs) == 1]
        inner = (lambda e : set(e & Bs).pop())  # returns endpt of e belonging to B
        
        V = beta*L + sum([c[e]*x[e] for e in H.edges() if len(e & Bs) == 2]) \
                   + sum([c[e]*(r - d_s[inner(e)]) for e in dB])
        return (V,dB)
    
    def cost(S):
        return sum([c[e] for e in S])
    
    F = []
    for s,t in G.sts():
        d_s = H.dist_from(s)
        if d_s[t] < float("inf"):
            for r in sorted(set(d_s.values()) | {0.5}):
                V,dB = volume(d_s,r)
                if cost(dB) < V*2*math.log((beta+1)/beta):
                    F = F + dB
                    H.remove_edges(dB)
                    break
    return F

