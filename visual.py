import graph
import json

G = graph.Graph(n = 100, p = 0.4)
d = {}
d["nodes"] = [{'id': i, 'group': 0} for i in G.vertices()]
d["links"] = [{'source': tuple(s)[0], 'target': tuple(s)[1], 'value': v} 
              for s, v in G.weights().items()]
#print d
json.dump(d,open("g.json", "w"))
