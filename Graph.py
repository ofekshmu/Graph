
from Edge import Edge


class Graph:
    
    def __Init__(self, graph : dict = {}, vertices : list = [], edges : list = [], Debug : bool = False):
        self.graph = graph
        self.debug = False

    def addEdge(self, e : Edge, force : bool = False):
        """ doc """
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
        pass
    
    def exists(self):
        pass

    def getVertices(self):
        pass

    def getEdges(self):
        pass

    def getNeighboors(self, v):
        pass

    def __repr__(self):
        """ TODO """
        return ""