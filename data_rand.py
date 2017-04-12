import graph
import LP
import IP_v2 as IP
import RG
import random; random.seed(1)
import time
import pickle
esp = 1e-4

data_rand = {}
for n in range(10,71,10):
    print n
    l = []
    for repeat in range(5):
        k = n/5
        def get_st(k):
            st = []
            for i in range(k):
                st.append((2*i,2*i + 1))
            return st 
        G = graph.Graph(n = n, p = 0.2, st = get_st(n))
        m = len(G.edges())

        t1_LP = time.time()
        x_LP = LP.solve(G)
        t2_LP = time.time()

        t1_IP = time.time()
        x_IP = None #LP.solve(G)
        t2_IP = time.time()

        H = graph.copy_graph(G,x_LP)

        t1_RG = time.time()
        F_RG = RG.solve(G,H)
        t2_RG = time.time()

        def t_LP():
            return t2_LP - t1_LP
        def v_LP():
            return sum([x_LP[e] for e in G.edges()])
        def t_IP():
            return t2_IP - t1_IP
        def v_IP():
            return None#sum([x_IP[e] for e in G.edges()])
        def t_RG():
            return t2_RG - t1_RG
        def v_RG():
            return len(F_RG)
        l.append({"obj_LP":v_LP(),"obj_IP":v_IP(),"obj_RG":v_RG(),
                  "t_solve_LP": t_LP(),"t_solve_IP": t_IP(), "t_solve_RG": t_RG(), 
                  'n': n, 'm': m, "k": k, 'type': 'rand'})
    data_rand[n] = l

output = open('data/rand/rand_data1.pkl', 'wb')
pickle.dump(data_rand, output)
output.close()
