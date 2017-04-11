import graph
from itertools import *
from gurobipy import *

def multi_cut_LP_relax(g):
    """ 
    solve the multi_cut_LP relaxation problem, return the LP solution
    Input: graph g, and number of (s,t) pairs by convension s1 = 0, t1 = 1; s2 = 3, t2 = 4, etc...
    Output: a list of [edge, fraction_cut]. i.e. [[(0,1) 0.3], [[2,3],1.00]]
    """
    vertices = g.vertices()
    edges = g.edges()
    weights = g.weights()
    # Create a new model
    m = Model("muticut")
    # Create variables
    cuts = {}
    for e in edges:
        cuts[e] = m.addVar(vtype=GRB.CONTINUOUS) # cuting edge e; >=0 by default
    dist = {}
    for e in combinations(vertices,2):
        e = frozenset(e)
        dist[e] = m.addVar(vtype=GRB.CONTINUOUS) # add distance variable
    # Integrate new variables
    m.update()
    # Set objective
    m.setObjective(sum([cuts[e]*weights[e] for e in edges]), GRB.MINIMIZE) # minimize cut-cost
    # Add constraints: WLOG source-sink pairs are (0,1),(2,3) ....
    for u,v in g.sts():
        m.addConstr( dist[frozenset([u , v])] >= 1  )
    #count = 0
    for e in combinations(vertices,3):
        l = list(e); l.sort(); u,v,w = l
        #count += 1
        #if count % 10000 == 0: print count
        m.addConstr(dist[frozenset([u,v])] + dist[frozenset([v,w])] >= dist[frozenset([u,w])])
        m.addConstr(dist[frozenset([u,w])] + dist[frozenset([v,w])] >= dist[frozenset([u,v])])
        m.addConstr(dist[frozenset([v,u])] + dist[frozenset([u,w])] >= dist[frozenset([v,w])])
    for e in edges:
        m.addConstr(dist[e] == cuts[e])
    
    m.optimize()
    
    x = {}
    for e in edges:
        x[e] = cuts[e].x
    return x
