import pickle
import graph
import LP
import RG
import IP_v2 as IP
import grid_graph
import time
runs = {}

N = 5
k = 4
p = 0.45


for L in range(5,20,3):
    res =[]
    for _ in range(5):
        print "================================================"
        print L
        (G,M) = grid_graph.random_grid_graph(N,L,k,p)
        t1 = time.time()
        x_LP =  LP.solve(G)
        OPT_LP =  G.objective(x_LP)
        
        H = graph.copy_graph(G,x_LP)
        t2 = time.time()
        x_IP = IP.solve(G)
        
        OPT_IP = G.objective(x_IP)
        t3 = time.time()

        F = RG.solve(G,H)
        ALG = len(F)
        t4 = time.time()



        #print "LP objective value: ",
        #print OPT_LP
        # 
        # print "IP objective value: ",
        # print OPT_IP
        # 
        #print "ALG objective value: ",
        #print ALG
        res.append({
            'time_LP': t2 - t1,
            'time_IP': t3 - t2,
            'time_RG': t4 - t3,
            'obj_LP':OPT_LP, 
            'obj_IP':OPT_IP,
            'obj_RG': ALG, 
            'n': len(G.vertices()), 
            'm': len(G.edges()),
            'k': k, 
            'type': 'grid'})
    runs[N*L] = res
print runs
pickle.dump(runs, open("data/small_n.pickle",'wb'))

### { uncomment this part for visualizing grid graph cuts 
### Output the results into the html files fractional.html and integral.html
# from visualize_grid_graph import vgg, fill 
# cuts = {e: (1 if e in F else 0) for e in G.edges()} 
# vgg(G, N, L, x_LP, M,'fractional.html')
# vgg(G, N, L, cuts, fill(H,M),'integral.html')
### }

