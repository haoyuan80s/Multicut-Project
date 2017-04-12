import pickle
import graph
import LP
import RG
import IP_v2 as IP
import grid_graph
import time
import math
runs = {}

N = 10

p= 0.45
L = 12

k=2
G = grid_graph.random_grid_graph(N,L,k,p)
for L in range(3,15):
    res =[]
    k = int(math.ceil(N*L*1.0/20))
    for _ in range(5):
        print "=================================="
        del G
        (G,_) = grid_graph.random_grid_graph(N,L,k,p)
        print G.vertices()

        # G = graph.Graph(n=60,p=0.3, st = [(0,1),(2,3),(4,5)])
        start = time.time()
        x_LP =  LP.solve(G)
        end = time.time()
        t_solve_LP = end-start

        OPT_LP =  G.objective(x_LP)
        H = graph.copy_graph(G,x_LP)
        ### }

        # 
        # x_IP = IP.solve(G)
        # OPT_IP = G.objective(x_IP)
        # 



        start = time.time()
        F = RG.solve(G,H)
        end=time.time()
        t_RG = end-start

        ALG = len(F)



        print "LP objective value: ",
        print OPT_LP
        # 
        # print "IP objective value: ",
        # print OPT_IP
        # 
        print "ALG objective value: ",
        print ALG
        res.append({'obj_LP':OPT_LP, 
            'obj_RG':ALG, 
            't_solve_LP': t_solve_LP, 
            't_RG':t_RG, 
            'n': len(G.vertices()), 
            'm': len(G.edges()),
            'k': k, 
            'type': 'grid'})
    runs[N*L] = res

pickle.dump(runs, open("data/grid/grid_graph_experiment1.pickle",'wb'))

### { uncomment this part for visualizing grid graph cuts 
### Output the results into the html files fractional.html and integral.html
# from visualize_grid_graph import vgg, fill 
# cuts = {e: (1 if e in F else 0) for e in G.edges()} 
# vgg(G, N, L, x_LP, M,'fractional.html')
# vgg(G, N, L, cuts, fill(H,M),'integral.html')
### }
