import graph
import json
import pickle

pickle_in = open("facebook.pickle","rb")
G_dic = pickle.load(pickle_in)
G = graph.Graph(graph_dict = G_dic)
d = {}
d["nodes"] = [{'id': i, 'group': 0} for i in G.vertices()]
d["links"] = [{'source': tuple(s)[0], 'target': tuple(s)[1], 'value': v} 
              for s, v in G.weights().items()]
json.dump(d,open("facebook.json", "w"))


for n in [50, 100, 150, 200]:
    G = graph.Graph(n = n, p = 5.0/n)
    d = {}
    d["nodes"] = [{'id': i, 'group': 0} for i in G.vertices()]
    d["links"] = [{'source': tuple(s)[0], 'target': tuple(s)[1], 'value': v} 
              for s, v in G.weights().items()]
    #print d
    json.dump(d,open("g"+str(n)+".json", "w"))
