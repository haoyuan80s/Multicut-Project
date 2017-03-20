
import tools

# Collect data
n = 20 # n = 300 works fine
p = 0.3
graph = tools.Graph(n = n,p = p)
edges_weights = tools.get_weights(graph)
vertices = graph.vertices()

#print(len(edges_weights)) # size of our problem



from gurobipy import *

edges, weights = multidict(edges_weights)


# Create a new model
m = Model("mip")

# Create variables
cuts = {} 
for e in edges:
    cuts[e] = m.addVar(vtype = GRB.BINARY) # if we cut edge e
members = {}
for v in vertices:
    members[v] = m.addVar(vtype = GRB.BINARY) # if we choose vertex v in our set S
    
# Integrate new variables
m.update()

# Set objective
m.setObjective(sum(cuts[e]*weights[e] for e in edges), GRB.MINIMIZE) # minimize cut-cost

# Add constraints:
m.addConstr(members[1] == 1)
m.addConstr(members[0] == 0)
for e in edges:
    u,v = e
    m.addConstr(members[v] <= members[u] + cuts[e])

# optimize it
m.optimize()

# display results
def printSolution():
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

