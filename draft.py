import graph

reload(graph)
import random; random.seed(1)
G = graph.Graph(n = 20, p = 0.3)
#G.remove_edges([(0,14),(5,12)])
print G.is_connected(1,2)


