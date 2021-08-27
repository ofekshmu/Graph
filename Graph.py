
from Edge import Edge


class Graph:
    
    def __Init__(self, graph : dict = {}, vertices : list = [], edges : list = [], Debug : bool = False):
        self.graph = graph
        self.debug = False

    def addEdge(self, e : Edge, force : bool = False):
        """ 
        Adds a new Edge @e to the graph
        @param e -  a new edge
        @param force - boolean indicating if to force the new edge onto the graph
        even if the corresponding vertices do not exist. vetices will be created and edge
        will be added if @force is True, insertiong will fail otherwise.
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
        
    
    def exists(self):
        pass

    def getVertices(self):
        pass

    def getEdges(self):
        pass

    def getNeighboors(self, v):
        pass

    def setDebugMode(self, state : boolean = True):
        self.debug = state

    def __repr__(self):
        """ TODO """
        return ""