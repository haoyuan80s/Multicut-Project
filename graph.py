"""Contains tookits for solving the Multicut Problems"""
import random; #random.seed(1)

class Graph(object):
    def __init__(self, graph_dict = None, n = 0, p=0, weights = None):
        """ 
            weights needs to be consistent with edge of graph_dict
        """
        self.__graph_dict = self.__gen_random_graph(n,p) if graph_dict == None else graph_dict
        self.__weights = self.__get_rand_weights() if weights == None else weights
            
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

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]
    
    def __get_rand_weights(self):
        """Associates a random weight to each edges of a graph"""
        weighs = {}
        for u,v in self.edges():
            if u < v:
                weighs[(u,v)] = random.random()
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
                    edges.append((vertex, neighbour))
        return edges
    
    def __gen_random_graph(self, n,p):
        graph_dict = {}
        def random_list(k):
            """Creat a list containing each number from k to n - 1 with probability p"""
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

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
