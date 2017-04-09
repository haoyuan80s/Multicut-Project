import graph
from gurobipy import *

def multi_cut_native(g):
    """return optimal multi_cut by solve an IP"""
    vertices = g.vertices()
    edges = g.edges()
    weights = g.weights()

    m = Model("muticut")

    # Create variables
    cuts = {} 
    for e in edges:
        cuts[e] = m.addVar(vtype = GRB.BINARY) # if we cut edge e

    # Integrate new variables
    m.update()

    # Set objective
    m.setObjective(sum(cuts[e]*weights[e] for e in edges), GRB.MINIMIZE) # minimize cut-cost

    # Add constraints:
    for s,t in g.sts():
        for P in g.find_all_paths(s,t):
            m.addConstr( sum( [ cuts[(min(P[j],P[j+1]), max(P[j],P[j+1]) )] for j in range(len(P) - 1)] ) >= 1 )

    # optimize it
    m.optimize()

    # # display results
    # def printSolution():
    #     print 'Problem size: |V| = ', n, ', |E|, = ', len(edges_weights) # size of our problem
    #     if m.status == GRB.Status.OPTIMAL:
    #         print('\nCost: %g' % m.objVal)
    #         #buyx = m.getAttr('x', buy)
    #         #nutritionx = m.getAttr('x', nutrition)
    #         print('\nCut:')
    #         for e in edges:
    #             print(e, cuts[e].x)
    #     else:
    #         print('No solution')

    # printSolution()

    return [e for e in g.edges() if cuts[e].x == 1]
    
