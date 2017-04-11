import graph
from itertools import *

# lattice graph in image models
# internal nodes (IN) are of the form (a,b) where a, b = 0,1,...,N-1
# boundary condition nodes (BCN) are of the form s_i = (-1,i), t_i = (-2,i), for i = 1,2,...,k
# there are 2(N-1)(2N-1) edges between internal nodes, and 2(N-1)(2N+1) edges in total
# edge weights from a BCN to an IN should have weight 2(N-1)(2N-1) + 1,
#   this is because it is always a valid cut to select all the internal nodes

neighbors = [(-1,1),(0,1),(1,1),(1,0)];
def grid_graph(N):
    G = graph.Graph(graph_dict = {(a,b):[] for a in range(N) for b in range(N)}, n=N**2)
    for a in range(N):
        for b in range(N):
            for (c,d) in neighbors:
                if 0 <= a+c < N and 0<=b+d < N and abs(c)+abs(d) >0:
                    G.add_edge(((a,b),(a+c,b+d)),1)
    return G

k = 3 # we want k pairs of (s_i,t_i) terminals
N = 10

# the terminals are nodes of the (-1,1), (-1,2), (-1,3) ...., (-1,k)

M = [[1,1,1,2,2,1,1,1,1,1],
     [1,0,0,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,0,0,2],
     [1,0,0,0,0,0,0,0,0,2],
     [3,0,0,0,0,0,0,0,0,2],
     [3,0,0,0,0,0,0,0,0,1],
     [3,0,0,0,0,0,0,0,0,1],
     [3,3,3,2,2,2,2,2,1,1]]


# M = [[1,1,2,2,1,1,1],
#      [1,0,0,0,0,0,1],
#      [1,0,0,0,0,0,2],
#      [3,0,0,0,0,0,2],
#      [3,0,0,0,0,0,1],
#      [3,0,0,0,0,0,1],
#      [3,3,2,2,1,1,1]]
# 




G = grid_graph(N)

terminals = [(-1,i) for i in range(1,k+1)]

for t in terminals:
    G.add_vertex(t)

for st in combinations(terminals,2):
    G.add_st(st)

for a in range(N):
    for b in range(N):
        i = M[a][b]
        if i>0:
            G.add_edge(((-1,i),(a,b)),2*(N-1)*(2*N-1)+1)


n = N**2
p = 2*(N-1)*(2*N+1)

