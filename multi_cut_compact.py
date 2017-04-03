import tools
from itertools import *
from gurobipy import *

# Collect data
n = 15 # num of vertices
p = 0.4 # prob of (i,j) \in E
k = 2 # number of pairs
graph = tools.Graph(n = n, p = p)
edges_weights = tools.get_weights(graph)
#G = {0: [2,4], 1: [2,3], 2:[0,1,5], 3: [1,4,5], 4: [0,5,3], 5: [2,3,4]}
#graph = tools.Graph(G)
#edges_weights = {(1, 2): 0.5, (1, 3): 0.5, (4,5): 0.25, (0, 4): 0.25, (2, 5): 0.5, (3, 4): 0.25, (0,2): 0.5, (3, 5):0.5 }
vertices = graph.vertices()
edges, weights = multidict(edges_weights)

# Create a new model
m = Model("muticut")

# Create variables
cuts = {} 
for e in edges:
    cuts[e] = m.addVar(vtype=GRB.CONTINUOUS) # cuting edge e; >=0 by default
dist = {}
for e in combinations(vertices,2):
    dist[e] = m.addVar() # add distance variable

# Integrate new variables
m.update()

# Set objective
m.setObjective(sum(cuts[e]*weights[e] for e in edges), GRB.MINIMIZE) # minimize cut-cost

# Add constraints: WLOG source-sink pairs are (0,1),(2,3) ....
for i in xrange(k):
    m.addConstr( dist[(2*i , 2*i + 1)] >= 1  )
for u,v,w in combinations(vertices,3):
    m.addConstr(dist[(u,v)] + dist[(v,w)] >= dist[(u,w)])
    m.addConstr(dist[(u,w)] + dist[(v,w)] >= dist[(u,v)])
    m.addConstr(dist[(u,v)] + dist[(u,w)] >= dist[(v,w)])
for e in edges:
    m.addConstr(dist[e] == cuts[e])

# optimize it
m.optimize()

# display results
def printSolution():
    print 'Problem size: |V| = ', n, ', |E|, = ', len(edges_weights) # size of our problem
    if m.status == GRB.Status.OPTIMAL:
        print('\nCost: %g' % m.objVal)
        #buyx = m.getAttr('x', buy)
        #nutritionx = m.getAttr('x', nutrition)
        print('\nCut:')
        for e in edges:
#            import pdb; pdb.set_trace()
            if cuts[e].x > 0.01 and cuts[e].x < 0.99:
                print(e, cuts[e].x)
    else:
        print('No solution')

printSolution()
