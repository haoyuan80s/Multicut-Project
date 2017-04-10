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
        l = list(e); l.sort(); se = tuple(l)
        dist[se] = m.addVar(vtype=GRB.CONTINUOUS) # add distance variable
    # Integrate new variables
    m.update()
    # Set objective
    m.setObjective(sum([cuts[e]*weights[e] for e in edges]), GRB.MINIMIZE) # minimize cut-cost
    # Add constraints: WLOG source-sink pairs are (0,1),(2,3) ....
    for u,v in g.sts():
        m.addConstr( dist[(u , v)] >= 1  )
    count = 0
    for e in combinations(vertices,3):
        l = list(e); l.sort(); u,v,w = l
        count += 1
        if count % 10000 == 0: print count
        m.addConstr(dist[(u,v)] + dist[(v,w)] >= dist[(u,w)])
        m.addConstr(dist[(u,w)] + dist[(v,w)] >= dist[(u,v)])
        m.addConstr(dist[(u,v)] + dist[(u,w)] >= dist[(v,w)])
    for e in edges:
        m.addConstr(dist[e] == cuts[e])
    # optimize it
    m.optimize()
    d = {}
    
#    for e in edges:
#        print e, cuts[e].x

#    print "asdfdsf"
    for e in combinations(vertices,2):
        l = list(e); l.sort(); se = tuple(l)
        d[se] = dist[se].x # add distance variable
        #if dist[e].x > 0.01:
#        print e,d[e]
    return d
    # display results
    
#     def printSolution():
# #        print 'Problem size: |V| = ', n, ', |E|, = ', len(edges_weights) # size of our problem
#         if m.status == GRB.Status.OPTIMAL:
#             print('\nCost: %g' % m.objVal)
#             #buyx = m.getAttr('x', buy)
#             #nutritionx = m.getAttr('x', nutrition)
#             print('\nCut:')
#             for e in edges:
#     #            import pdb; pdb.set_trace()
#                 #if cuts[e].x > 0.01 and cuts[e].x < 0.99:
#                 print(e, cuts[e].x)
#         else:
#             print('No solution')

#     printSolution()
