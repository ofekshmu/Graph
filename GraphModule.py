from Edge import Edge
from Vertice import Color, Vertice
import math

class Graph(Vertice, Edge):

    def __init__(self,
                        vertices = [],
                        edges = [],
                        directed = True,
                        debug = False):
        # settings
        self.debug = debug
        self.directed = directed
        #structures
        self.vertices = {}
        self.edges = {}
        self.adj = {}

        for vId in vertices:
            self.addVertive(vId)
        
        for e in edges:
            if isinstance(e, tuple):
                if not self.addEdge(e[0],e[1]):
                    self.debuger("Graph Constructor",f"{e} Was not added!")
            else:
                self.debuger("Graph Constructor", f"{e} is not of type 'Edge'!")

    def addVertice(self, vId) -> bool:
        self.vertices[vId] = Vertice(vId)
        #TODO: check if exist, add to adj

    def _addAdj(self, v1, v2):
        if v1 in self.adj:
            self.adj[v1][v2] = self.vertices[v2]
        else:
            self.adj[v1] = {v2: self.vertices[v2]}
        
    def addEdge(self, v1, v2, weight = 1) -> bool:
        result = False
        c1, c2 = self.exists(v1), self.exists(v2)
        
        if c1 and c2 :
            self.edges[(v1,v2)] = Edge(v1,v2,weight)
            self._addAdj(v1,v2)
            result = True

        if not c1:
            self.debuger("addEdge",f"Vertice {v1} does not exist in graph.")
        if not c2:
            self.debuger("addEdge",f"Vertice {v2} does not exist in graph.")       
        
        return result
 



    def forceEdge(self, v1, v2, weight = 1):
        result = False
        c1, c2 = self.vExists(v1), self.vExists(v2)

        if not c1:
            self.vertices[v1] = Vertice(v1)
            self.debuger("forceEdge",f"Vertice {v1} was forced.")        

        if not c2:
            self.vertices[v2] = Vertice(v2)
            self.debuger("forceEdge",f"Vertice {v2} was forced.")        
 
        if c1 and c2 :
            self.edges[(v1,v2)] = Edge(v1,v2,weight)
            self._addAdj(v1,v2)
            result = True
        else:
            self.debuger("forceEdge",f"Critical Error!")
        
        return result

    def popEdge(self, e: tuple) -> bool: 
        if self.edges.pop(e,None) == None:
            self.debuger("popEdge",f"Edge with an id {e} does not exist.")
            return False
        
        #remove from adj:
        (v1, v2) = e
        if self.adj[v1].pop(v2, None) == None:
            return False
        return True
    
    def popVertice(self, vId) -> bool: #TODO impl func to check if vertice is slo
        # check if edges are attached
        e = self.adj.get(vId, default = None)
        # TODO:what about edges pointing to self?
        if e != None:
            self.debuger("popVertice",f"{vId} was not removed, {e} is attached to it")
            return False

        if self.edges.pop(vId ,None) == None:
            self.debuger("popEdge",f"Vertice with an id {vId} does not exist.")
            return False

        return True
    
    def getUnvisited(self, vId) -> list: #of type Vertice
        
        #white is defined as unvisited
        lst = []
        adj = self.__getAdj(vId)
        for v in adj:
            if v.getColor() == Color.white:
                lst.append(v)
        return lst

        pass

    def isAdj(self, v1, v2) -> bool:
        """ Returns True if @param v1 and @param v2 are Neighboors,
            False otherwise."""
        try:
            self.adj[v1][v2]
            return True
        except KeyError:
            return False

    def __getAdj(self, vId) -> list: #of type Vertice
        """ Returns a list of Neighboors of @param vId"""
        return self.adj[vId].values()

    def __getVertice(self, vId) -> Vertice:
        """ Returns Vertice With """
        try:
            return self.vertices[vId]
        except:
            self.debuger("getVertice",f"{vId} was not found.")
            raise RuntimeWarning

    def exists(self, object) -> bool: #TODO change implemantation
        if isinstance(object,tuple):
            return object in self.edges
        else:
            return object in self.vertices

    def __repr__(self):
        print(self.adj)
        str = ""
        for vId in self.vertices.keys():
            str += f"\t{vId} -->"
            for vId2 in self.adj[vId].keys():
                str += f" {vId2},"
            str += "\n"

        return str


#---------------------------------------
    
    def debuger(self, function :str, message :str):
        if self.debug: 
            print("\n",10*'~',f" Message in Graph Infrustructure -> {function} ",10*'~',"\n",message,"\n")

#---------------------------------------
    def dijkstra_Init(self, init):
        for v in self.vertices:
            v.unvisit()
            v.setDistance(math.inf,acc=False)
        self.getV(init).setDistance(0, acc=False)

