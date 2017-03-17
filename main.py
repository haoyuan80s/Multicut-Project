import importlib
import dongxi
importlib.reload(dongxi)
from dongxi import *

from scipy.optimize import linprog

# a random Graph with n vetexes
n = 10
p = 0.3

graph = Graph(random_graph(n, p))

c = [-1, 4]
A = [[-3, 1], [1, 2]]
b = [6, 4]
x0_bounds = (None, None)
x1_bounds = (-3, None)
res = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds), options={"disp": True})
print(res)
