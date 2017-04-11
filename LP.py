import graph
from itertools import *
from gurobipy import *

def solve(g):
    """ 
    solve the multi_cut_LP relaxation problem, return the LP solution
    Input: graph g, and number of (s,t) pairs by convension s1 = 0, t1 = 1; s2 = 3, t2 = 4, etc...
    Output: a list of [edge, fraction_cut]. i.e. [[(0,1) 0.3], [[2,3],1.00]]
    """
    vertices = g.vertices()
    edges = g.edges()
    weights = g.weights()
    sts = g.sts()
    # Create a new model
    m = Model("muticut")
    # Create variables
    cuts = {}
    for e in edges:
        cuts[e] = m.addVar(vtype=GRB.CONTINUOUS) # cuting edge e; >=0 by default
    dist = {}
    for u in vertices:
        dist[frozenset([u])] = m.addVar(vtype=GRB.CONTINUOUS)
    for e in combinations(vertices,2):
        e = frozenset(e)
        dist[e] = m.addVar(vtype=GRB.CONTINUOUS) # add distance variable
    # Integrate new variables
    m.update()
    # Set objective
    m.setObjective(sum([cuts[e]*weights[e] for e in edges]), GRB.MINIMIZE) # minimize cut-cost
    # Add constraints: WLOG source-sink pairs are (0,1),(2,3) ....
    for u,v in sts:
        uv = frozenset([u,v])
        m.addConstr( dist[uv] >= 1  )
    for s in vertices:
        for u,v in edges:
            m.addConstr( dist[frozenset([u,s])] <= dist[frozenset([v,s])] + cuts[frozenset([u,v])] )
            m.addConstr( dist[frozenset([v,s])] <= dist[frozenset([u,s])] + cuts[frozenset([u,v])] )
    for e in edges:
        m.addConstr(dist[e] == cuts[e])
    for u in vertices:
        u = frozenset([u])
        m.addConstr(dist[u] == 0)
    
    # optimize it
    m.optimize()
    x = {}
    for e in edges:
        x[e] = cuts[e].x
    return x

