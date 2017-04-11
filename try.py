import graph
import IP
import LP
import naive as IP1
G = graph.Graph(n = 15, p = 0.3, st = [(0,1),(2,3),(4,5),(6,7)])

print IP.solve(G)
print LP.solve(G)
