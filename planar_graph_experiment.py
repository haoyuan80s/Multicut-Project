import pickle
import graph
import LP
import RG
import IP_v2 as IP
import time
import math

results = {}

for n in range(10,200,10):
    res = []
    k = int(math.ceil(n/20.0))

    for i in range(1,5):
        print "================================="
        print n

        G = graph.from_csv('data/graphs/n%03d_k%02d/G%d' % (n,k,i))
        tic = time.time()
        x_LP = LP.solve(G)
        t_solve_LP = tic - time.time()

        OPT_LP = G.objective(x_LP)
        H = graph.copy_graph(G,x_LP)

        tic = time.time()
        F = RG.solve(G,H)
        t_RG = tic - time.time()

        x_ALG = {}
        for e in G.edges():
            x_ALG[e] = 0
        for e in F:
            x_ALG[e] = 1
        ALG = G.objective(x_ALG)

        if n < 70:
            tic = time.time()
            x_IP = IP.solve(G)
            OPT_IP = G.objective(x_IP)
            t_solve_IP = tic - time.time()
        else:
            OPT_IP = None
            t_solve_IP = None


        print "LP objective value: ",
        print OPT_LP
        print "ALG objective value: ",
        print ALG
        print "IP objective value: ",
        print (OPT_IP or 'xxx')

        res.append({'obj_LP':OPT_LP,
            'obj_RG':ALG,
            'obj_IP':OPT_IP,
            't_solve_LP': t_solve_LP,
            't_RG':t_RG,
            't_solve_IP': t_solve_IP,
            'n': n,
            'm': len(G.edges()),
            'k': k,
            'type': 'planar'})
        results[n] = res
        pickle.dump(results, open("data/planar_graph_experiment1.pickle", 'wb'))
