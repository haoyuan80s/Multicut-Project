import graph
import IP
import LP
import IP_v2
esp = 1e-4
import random; random.seed(1)

n = 50
st = []
for i in range(n/3):
    st.append((2*i,2*i + 1))
 
G = graph.Graph(n = n, p = 0.3, st = st)

#print IP.solve(G)
#LP.solve(G)
IP_v2.solve(G)

LP_sol = LP.solve(G)


print list(filter(lambda x: x[1] > esp and x[1] < 1 - esp, LP_sol.items()))

