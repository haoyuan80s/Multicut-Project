
import tools
import importlib; importlib.reload(tools)

# Collect data
n = 10
p = 0.3
graph = tools.Graph(n = 10,p = 0.3)
edges_weights = tools.get_weights(graph)
vertices = graph.vertices()

from gurobipy import *

edges, weights = multidict(edges_wieghts)

try:

    # Create a new model
    m = Model("mip")

    # Create variables
    is_cut = m.addVars(deges, vtype=GRB.BINARY)
    is_member = m.addVars(vertices, vtype=GRB.BINARY)
    
    # Integrate new variables
    m.update()

    # Set objective
    m.setObjective(is_cut.prod(weights), GRB.MAXIMIZE)

    # Add constraints:
    m.addConstr(is_member[0] == 1)
    m.addConstr(is_member[9] == 0)
    for e in edges:
        u,v = e
        m.addConstr(is_member[v] <= is_member[u] + is_cut[e])

    m.optimize()

except GurobiError:
    print('Error reported')
