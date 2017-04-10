import pickle

f = open('348.edges', 'r')

def change_format(x):
    return [int(n) for n in x.split()]

# M = 0
# for line in f:
#     u,v = change_format(line)
#     M = max(M,u,v)
# 571
graph_dict = {}
for i in range(572):
    graph_dict[i] = []

for line in f:
    u,v = change_format(line)
    print(u,v)
    graph_dict[u-1] += [v-1]
    graph_dict[v-1] += [u-1]

pickle_out = open("facebook.pickle", "wb",)
pickle.dump(graph_dict, pickle_out,protocol=2)
pickle_out.close()

