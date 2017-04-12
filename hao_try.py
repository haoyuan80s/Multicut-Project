import graph
import LP
import IP_v2 as IP
import RG
import random;# random.seed(1)
import time
import pickle
esp = 1e-4

# data_growing_k = {}
# n = 70
#for k in range(10,30,3):
#    print k
#    for repeat in range(5):

data_p = {}
n = 50
k = n / 2
for p in [x*0.1+0.1 for x in range(10)]:
    print '=========================================================================================================================================================='
    print p
    l = []
    for _ in range(8):
        def get_st(k):
            st = []
            for i in range(k):
                st.append((2*i,2*i + 1))
            return st 
        G = graph.Graph(n = n, p = p, st = get_st(k))
        m = len(G.edges())

        t1_LP = time.time()
        x_LP = LP.solve(G)
        t2_LP = time.time()
        H = graph.copy_graph(G,x_LP)

        t1_RG = time.time()
        F_RG = RG.solve(G,H)
        t2_RG = time.time()
        def v_LP():
            return sum([x_LP[e] for e in G.edges()])
        def t_LP():
            return t2_LP - t1_LP
        def t_IP():
            return t2_IP - t1_IP
        def v_IP():
            return sum([x_IP[e] for e in G.edges()])
        def t_RG():
            return t2_RG - t1_RG
        def v_RG():
            return len(F_RG)
        #print [x_LP[key] for key in x_LP if x_LP[key] > esp and x_LP[key] < 1 - esp]
        
        l.append({"obj_LP":v_LP(),"obj_RG":v_RG(),
          "t_solve_LP": t_LP(), "t_solve_RG": t_RG(), 
          'n': n, 'm': m, "k": k, 'type': 'rand'})
    data_p[p] = l

output = open('data/rand/data_p.pkl', 'wb')
pickle.dump(data_p, output)
output.close()





