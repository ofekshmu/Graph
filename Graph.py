from typing_extensions import runtime
from Edge import Edge

class Graph:
    
    def __init__(self, vertices : list = [],
                     edges : list = [], 
                     duplicates :bool = False, 
                     directed :bool = False,
                     debug : bool = False,
                     loops : bool = False):
        self.loops = loops
        self.graph = {}
        self.debug = debug
        self.duplicates = duplicates
        self.directed = directed

        for v in vertices:
            self.addVertice(v)
        for e in edges:
            self.addEdge(e, force = True)
        
    def addEdge(self, e : Edge, force : bool = False):
        """ 
        Adds a new Edge @e to the graph
        @param e -  a new edge
        @param force - boolean indicating if to force the new edge onto the graph
        even if the corresponding vertices do not exist. vetices will be created and edge
        will be added if @force is True, insertiong will fail otherwise.
        @returns True upon succesful insertion, False otherwise.
        """
        cond_e = e.end in self.graph.keys()
        cond_s = e.start in self.graph.keys()
        if self.__shouldAdd(e):
            if force:
                if not cond_e:
                    self.addVertice(e.end)
                    self.debuger("addEdge",f"End of edge {e} was forced")
                if not cond_s:
                    self.addVertice(e.start)
                    self.debuger("addEdge",f"Start of edge {e} was forced")

            if (cond_e and cond_s) or force:
                self.graph[e.start].append(e.end)
                return True
        return False

    def addVertice(self, v):
        """ Adds a new vertice @v to the graph """
        if v in self.graph.keys():
            self.debuger("addVertice",f"{v} is already a vertice in the graph.")
        else:
            self.graph[v] = []
        
    
    def exists(self, value):
        """
        Receives either a vertices or an Edge and returns True
        if is present in graph, False otherwise.
        """
        if isinstance(value, Edge):
            end_exists = value.end in self.graph.keys()
            start_exists = value.start in self.graph.keys()
            if end_exists and start_exists:
                if value.end in self.graph[value.start]:
                    return True
        else:
            if value in self.graph.keys():
                return True
        return False 

    def __shouldAddEdge(self, e :Edge):        
        if isinstance(e, Edge):
            if e.end == e.start:
                return True if self.loops else False
            elif self.exists(e):
                return True if self.duplicates else False
            return True
        else:
            self.debuger("__shouldAddEdge","ERORR - something is not right!!")
            raise RuntimeError
                



    def getVertices(self):
        """@returns a list of the vertices in the graph """
        return list(self.graph.values())

    def getVerticesCount(self):
        """@returns the number of vertices in the graph"""
        return len(self.graph.keys())

    def getNeighboors(self, v):
        """
        @returns the the neighboors of @v.
        throws an error if @vb does not exist in graph"""
        if self.exists(v):
            return self.graph[v]
        else:
            self.debuger("getNeighboors",f"Vertice {v} does not exist.\nNo list returned.")
            raise RuntimeWarning


    def setDebugMode(self, state : bool = True):
        self.debug = state

    def debuger(self, function :str, message :str):
        if self.debug: 
            print(10*'-',f" Message in Graph Infrustructure -> {function} ",10*'-',"\n",message,"\n")

    def __repr__(self):
        string = "Graph Preview:\n"
        for v in self.graph.keys():
            string += f"\t\t{v} --> "
            for neigh in self.getNeighboors(v):
                string += f" {neigh},"
            string = string[:-1] +"\n"                #cut the last comma
        string +=20*'-'+"\n"
        return string


#some tests for the time being:
g = Graph(debug=True, duplicates=True)
print(g)
g.addVertice(1)
print(g.exists(1))
g.addEdge(Edge(1,2))
g.addEdge(Edge(1,2),force=True)
g.addEdge(Edge(1,3),force=True)
print(g.exists(Edge(1,2)))
g.addEdge(Edge(5,6),force=True)
g.addEdge(Edge(5,6),force=True)

print(g.getNeighboors(5))
#print(g.getNeighboors(1))
print(g)

g2 = Graph(vertices=[1,2,5,7,23],edges=[Edge(1,2),Edge(5,7),Edge(10,1),Edge(20,25)])
print(g2)