
from typing import Optional
from Edge import Edge


class Graph:
    
    def __Init__(self, vertices : list = [], edges : list = [], debug : bool = False):
        self.graph = {}
        
        for v in vertices:
            self.addVertice(v)
        for e in edges:
            self.addEdge(e, force = True)
        
        self.debug = debug

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
        if self.debug:
            if force and not cond_e or not cond_s:
                print(f"{e} was forced")  
            if self.debug and not cond_e:
                print(f"End of edge {e} does not exist in graph")
            if self.debug and not cond_s:
                print(f"Start of edge {e} does not exist in graph")

        if force or cond_s and cond_e:
            self.graph.__setitem__(e.start, e.end); 
            return True
        return False

    def addVertice(self, v):
        """ Adds a new vertice @v to the graph """
        if v in self.graph.keys():
            if self.debug: print(f"{v} is already a vertice in the graph.")
        else:
            self.graph[v] = []
        
    
    def exists(self, value : Optional[Edge]):
        """
        Receives either a vertices or an Edge and returns True
        if is present in graph, False otherwise.
        """
        if value.isinstance(Edge):
            end_exists = value.end in self.graph.keys()
            start_exists = value.start in self.graph.keys()
            if end_exists and start_exists:
                if value.end in self.graph[value.start]:
                    return True
        else:
            if value in self.graph.keys():
                return True
        return False 

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
            print(f"Vertice {v} does not exist.\nNo list returned.")
            raise RuntimeWarning


    def setDebugMode(self, state : bool = True):
        self.debug = state

    def __repr__(self):
        string = "Graph Preview:\n"
        for v in self.graph.keys():
            string += f"\t\t{v} --> "
            for neigh in self.getNeighboors(v):
                string += f" {neigh},"
            string = string[:-1]                #cut the last comma
        return string
