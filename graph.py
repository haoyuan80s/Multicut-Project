"""Contains tookits for solving the Multicut Problems"""
import random; #random.seed(1)

class Graph(object):
    def __init__(self, graph_dict = None, n = 0, p=0, weights = None, st = []):
        """ 
            weights needs to be consistent with edge of graph_dict
        """        
        self.__st = st
        self.__graph_dict = self.__gen_random_graph(n,p) if graph_dict == None else graph_dict
        if weights == None:
            self.__weights = {} 
            for e in self.edges():
                self.__weights[e] = 1
        if weights == "random":
            self.__weights = self.__get_rand_weights() if weights == None else weights
        
    def sts(self):
        """return soure_terminal pairs"""
        return self.__st
    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())
    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()
    def weights(self):
        return self.__weights
    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge, weight):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = frozenset(edge)
        (v1, v2) = tuple(edge)
        if v1 in self.__graph_dict:
            self.__graph_dict[v1].append(v2)
        else:
            self.__graph_dict[v1] = [v2]
        if vertex2 in self.__graph_dict.keys():
            self.__graph_dict[v2].append(v1)
        else:
            self.__graph_dict[v2] = [v1]
            
        self.__weights[edge] = weight
            
    def add_st(self, st):
        """ Adds an s-t pair to the graph, where st is a vertex tuple. If either vertex does not
            exist, it is added to the graph.
        """
        if st[0] not in self.__graph_dict.keys():
            self.add_vertex(st[0])
        if st[1] not in self.__graph_dict.keys():
            self.add_vertex(st[1])
        self.__st.append(st)

    def remove_edges(self, edges):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        for u,v in edges:
            self.__graph_dict[u].remove(v)
            self.__graph_dict[v].remove(u)
            self.__weights.remove(frozenset([u,v]))
    
    def dist_from(self, u):
        """ returns a dictionary mapping vertices v to their distance d(u,v) from vertex u """
        graph_dict = self.__graph_dict
        w = self.__weights
        
        d = {}
        for vtx in self.vertices():
            d[vtx] = float("inf")
        d[u] = 0
        
        unvisited = self.vertices()
        curr = u
        while len(unvisited) > 0:
            for v in self.__graph_dict[curr]:
                d[v] = min(d[v], d[curr] + w[frozenset([curr,v])])
            unvisited.remove(curr)
            curr = None
            for v in unvisited:
                if curr is None or d[v] < d[curr]:
                    curr = v
        return d
        
    def ball_bdry(self, s, r):
        """ returns a ball B and its boundary dB in a tuple """
        d = self.dist_from(s)
        B = [x for x in self.vertices() if d[x] <= r]
        B_set = frozenset(B)
        dB = [e for e in self.edges() if len(e & B_set) == 1]
        return (B,dB)
    
    def __get_rand_weights(self):
        """Associates a random weight to each edges of a graph"""
        weighs = {}
        for e in self.edges():
            weighs[e] = random.random()
        return weighs

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append(frozenset([vertex, neighbour]))
        return edges
    
    def __gen_random_graph(self, n,p):
        graph_dict = {}
        def random_list(k):
            """Create a list containing each number from k to n - 1 with probability p"""
            l = []
            for i in range(k,n):
                if random.random() < p:
                    l.append(i)
            return l

        for i in range(n):
            l = []
            if i <= n - 2:
                l = random_list(i+1)
            for j in range(i):
                if i in graph_dict[j]:
                    l.append(j)
            graph_dict[i] = l
        return graph_dict
    
    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to end_vertex in graph """
        graph = self.__graph_dict 
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, end_vertex, path)
                for p in extended_paths: 
                    paths.append(p)
        return paths
    
    def is_connected(self, start_vertex, end_vertex):
        """ find all paths from start_vertex to 
            end_vertex in graph """
        visited = []
        def help(start_vertex, end_vertex):
            graph = self.__graph_dict
            visited.append(start_vertex)
            if start_vertex == end_vertex:
                return True
            for vertex in graph[start_vertex]:
                if vertex not in visited:
                    if help(vertex, end_vertex):
                        return True
            return False
        return help(start_vertex, end_vertex)
        
    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
    
    def to_csv(self, fname):
        """ Writes vertex names to 'fname.vtx', adjacency list to 'fname.adj', and source/target pairs to 'fname.stp'. """
        graph = self.__graph_dict
        weights = self.__weights
        st = self.__st
        
        idx_of = dict()
        vf = ""
        for (i,v) in enumerate(graph.keys()):
            idx_of[v] = i
            vf = vf + str(v) + "\n"
        vf = vf[:-1]
        print(vf)
        
        ef = ""
        for v in graph.keys():
            for u in graph[v]:
                ef = ef + str(idx_of[v]) + "," + str(idx_of[u]) + "," + str(weights[(v,u)]) + "\n"
        ef = ef[:-1]
        print(ef)
        
        stf = ""
        for s,t in st:
            stf = stf + str(idx_of[s]) + "," + str(idx_of[t]) + "\n"
        stf = stf[:-1]
        print(stf)
        
        with open(fname + ".adj", 'w') as f:
            f.write(ef)
        with open(fname + ".vtx", 'w') as f:
            f.write(vf)
        with open(fname + ".stp", 'w') as f:
            f.write(stf)
    
    
def from_csv(fname):
    """ creates Graph object from 'fname.adj' and 'fname.stp'. Interpreting the vertex names file
        from to_csv is difficult because of Python typing so it's not supported. """
    G = Graph()
    with open(fname + ".adj", 'r') as f:
        for line in f:
            tokens = line.split(',')
            G.add_edge((int(tokens[0]), int(tokens[1])), float(tokens[2]))
            print("adding (" + tokens[0] + "," + tokens[1] + ")")
    with open(fname + ".stp", 'r') as f:
        for line in f:
            tokens = line.split(',')
            G.add_st((int(tokens[0]), int(tokens[1])))
    return G
