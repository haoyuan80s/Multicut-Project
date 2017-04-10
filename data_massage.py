import pickle
f = open('348.edges', 'r')                                                                                                                                                      
def change_format(x): 
    return [int(n) for n in x.split()]                                                                                    
g = {}
                           
for line in f:
    u,v = change_format(line)
    if u > 500 and v > 500:
        if u not in g:
            g[u] = [v]
        else:
            g[u] += [v]
        if v not in g:
            g[v] = [u]
        else:
            g[v] += [u]
print len(g)
pickle_out = open("facebook.pickle", "wb",)
pickle.dump(g, pickle_out)
pickle_out.close()                       
