#import pickle
import graph
import LP_relax_v2 as LP
import naive as na
import random; random.seed(1)
from fractions import Fraction
esp = 1e-4

# random graph with fractional LP solution
for n in [200]: 
    print n
    st = []
    for i in range(n/3):
        st.append((2*i, 2*i + 1))
    G = graph.Graph(n = n, p = 4.0/n, st = st)

    LP_sol = LP.multi_cut_LP_relax(G)

    #print type(LP_sol)
    l = list(filter(lambda x: x[1] > esp and x[1] < 1 - esp, LP_sol.items()))
    print [Fraction(k[1]).limit_denominator(1000) for k in l]
