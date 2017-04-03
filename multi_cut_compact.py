import tools

# Collect data
n = 30 # n = 300 works fine
p = 0.7 # prob of (i,j) \in E
k = 8 # number of pairs
graph = tools.Graph(n = n,p = p)
edges_weights = tools.get_weights(graph)
vertices = graph.vertices()



from gurobipy import *

edges, weights = multidict(edges_weights)

# Create a new model
m = Model("mip")

# Create variables
cuts = {} 
for e in edges:
    cuts[e] = m.addVar() # if we cut edge e; >=0 by default
dist = {}
for u in vertices:
    for v in vertices:
        dist[(u,v)] = m.addVar() # add distance variable

# Integrate new variables
m.update()

# Set objective
m.setObjective(sum(cuts[e]*weights[e] for e in edges), GRB.MINIMIZE) # minimize cut-cost

# Add constraints:
# WLOG source-sink pairs are (0,1),(2,3) ....
for i in xrange(k):
    m.addConstr( dist[(2*i , 2*i + 1)] >= 1  )
for u in vertices:
    for v in vertices:
        m.addConstr(dist[(u,v)] == dist[(v,u)])
        for w in vertices:
            m.addConstr(dist[(u,v)] + dist[(v,w)] >= dist[(u,w)])
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
            print(e, cuts[e].x)
    else:
        print('No solution')

printSolution()
