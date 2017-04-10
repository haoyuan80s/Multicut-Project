import tools
from itertools import *

# lattice graph in image models
# internal nodes (IN) are of the form (a,b) where a, b = 0,1,...,N-1
# boundary condition nodes (BCN) are of the form s_i = (-1,i), t_i = (-2,i), for i = 1,2,...,k
# there are 2(N-1)(2N-1) edges between internal nodes, and 2(N-1)(2N+1) edges in total
# edge weights from a BCN to an IN should have weight 2(N-1)(2N-1) + 1,
#   this is because it is always a valid cut to select all the internal nodes

neighbors = [(-1,1),(0,1),(1,1),(1,0)];
def grid_graph(N):
    G = Graph(graph_dict = {(a,b):[] for a in range(N) for b in range(N)}, n=N**2)
    for a in range(N):
        for b in range(N):
            for (c,d) in neighbors:
                if 0 <= a+c < N and 0<=b+d < N and abs(c)+abs(d) >0:
                    G.add_edge(((a,b),(a+c,b+d)))
    return G

k = 3 # we want k pairs of (s_i,t_i) terminals
N = 10

# the terminals are nodes of the (-1,1), (-1,2), (-1,3) ...., (-1,k)
terminals = [(-1,i) for i in range(1,k+1)]
st_pairs = combinations(terminals,2)

M = [[1,1,1,2,2,2,2,1,1,1],
     [1,0,0,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,0,0,2],
     [1,0,0,0,0,0,0,0,0,2],
     [1,0,0,0,0,0,0,0,0,2],
     [3,0,0,0,0,0,0,0,0,2],
     [3,0,0,0,0,0,0,0,0,1],
     [3,0,0,0,0,0,0,0,0,1],
     [3,3,3,2,2,2,2,1,1,1]]


# M = [[1,1,2,2,1,1,1],
#      [1,0,0,0,0,0,1],
#      [1,0,0,0,0,0,2],
#      [3,0,0,0,0,0,2],
#      [3,0,0,0,0,0,1],
#      [3,0,0,0,0,0,1],
#      [3,3,2,2,1,1,1]]
# 




graph_tuple = grid_graph(N)

edges_weights = {}

for e in graph.edges():
    edges_weights[e] = 1

for a in range(N):
    for b in range(N):
        i = M[a][b]
        if i>0:
            graph_tuple.add_edge(((-1,i),(a,b)))
            edges_weights[((-1,i),(a,b))] = 2*(N-1)*(2*N-1)+1

n = N**2
p = 2*(N-1)*(2*N+1)

keys = graph_tuple.vertices()
values = range(len(graph_tuple.vertices()))

tupleToInt = dict(zip(keys,values))
intToTuple = dict(zip(values,keys))

graph = Graph()
for v in keys:
    graph.add_vertex(v)
for e in graph_tuple.edges():
    (u,v) = e
    graph.add_edge((tupleToInt(u),tupleToInt(v)), edges_weights[e])
