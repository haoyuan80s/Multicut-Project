import tools

# Collect data
n = 15 # n = 300 works fine
p = 0.4 # prob of (i,j) \in E
k = 2 # number of pairs
graph = tools.Graph(n = n,p = p)
edges_weights = tools.get_weights(graph)
vertices = graph.vertices()

from gurobipy import *

edges, weights = multidict(edges_weights)

# Create a new model
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
# WLOG source-sink pairs are (0,1),(2,3) ....
for i in range(k):
    for P in graph.find_all_paths(2*i,2*i + 1):
        m.addConstr( sum( [ cuts[(min(P[j],P[j+1]), max(P[j],P[j+1]) )] for j in range(len(P) - 1)] ) >= 1 )

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
            print(e, cuts[e].x)
    else:
        print('No solution')

printSolution()
