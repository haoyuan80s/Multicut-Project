import pickle
# d = {1:2}
# output = open('haha', 'wb')
# pickle.dump(d, output)
# output.close()

input = open('rand_data.pkl', 'rb')
data_rand = pickle.load(input)
print data_rand[20]

data_rand = {}
n = 100
for k = range(20,50,5):
    print k
    for repeat in range(5):
        k = n/5
        def get_st(n):
            st = []
            for i in range(k):
                st.append((2*i,2*i + 1))
            return st 
        G = graph.Graph(n = n, p = 0.3, st = get_st(n))
        m = len(G.edges())

        t1_LP = time.time()
        x_LP = LP.solve(G)
        t2_LP = time.time()

#        t1_IP = time.time()
#        x_IP = LP.solve(G)
#        t2_IP = time.time()

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
            return sum([x_IP[e] for e in G.edges()])
        def t_RG():
            return t2_RG - t1_RG
        def v_RG():
            return len(F_RG)
        l.append({"obj_LP":v_LP(),"obj_IP":v_IP(),"obj_RG":v_RG(),
                  "t_solve_LP": t_LP(),"t_solve_IP": t_IP(), "t_solve:RG": t_RG(), 
                  'n': n, 'm': m, "k": k, 'type': 'rand'})
    data_rand[n] = l

output = open('rand_data.pkl', 'wb')
pickle.dump(data_rand, output)
output.close()
