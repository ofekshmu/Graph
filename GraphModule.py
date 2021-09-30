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
            self.vertices[vId] = Vertice(vId)
        
        for e in edges:
            if isinstance(e, Edge):
                if not self.addEdge(e):
                    self.debuger("Graph Constructor",f"{e} Was not added!")
            else:
                self.debuger("Graph Constructor", f"{e} is not of type 'Edge'!")

    def __addAdj(self, v1, v2):
        if v1 in self.adj:
            self.adj[v1][v2] = self.getVertice(v2)
        else:
            self.adj[v1] = {v1: self.getVertice(v2)}
        

    def addEdge(self, v1, v2, weight = 1) -> bool:
        result = False
        c1, c2 = self.vExists(v1), self.vExists(v2)
        
        if c1 and c2 :
            self.edges[(v1,v2)] = Edge(v1,v2,weight)
            self.__addAdj(v1,v2)
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
            self.__addAdj(v1,v2)
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
        adj = self.getAdj(vId)
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

    def _getAdj(self, vId) -> list: #of type Vertice
        """ Returns a list of Neighboors of @param vId"""
        return self.adj[vId].values()

    def _getVertice(self, vId) -> Vertice:
        """ Returns Vertice With """
        try:
            return self.vertices[vId]
        except:
            self.debuger("getVertice",f"{vId} was not found.")
            raise RuntimeWarning

    def exists(self, object) -> bool:
        if isinstance(object,tuple):
            return object in self.edges
        else:
            return object in self.vertices

    def __repr__(self):
        dict = {}
        for v in self.vertices:
            dict[v.id] = []
        for e in self.edges:
            dict[e.getStartId()].append(e.getEndId())

        str = ""
        for k,v in dict.items():
            str += f"{k} --> "
            for vertice in v:
                str += f"{vertice},"
            str = str[:-1] +"\n"
        return str
    
    def debuger(self, function :str, message :str):
        if self.debug: 
            print("\n",10*'~',f" Message in Graph Infrustructure -> {function} ",10*'~',"\n",message,"\n")

    def getRaw(self):
        return [self.edges,self.vertices]
    
    def getWeight(self, e: Edge):
        for e_g in self.edges:
            if e == e_g:
                return e_g.getWeight()
    
    def setWeight(self, e: Edge, w):
        for e_g in self.edges:
            if e == e_g:
                e_g.setWeight(w)
                return True
        return False

    def visit(self, v):
        self.getV(v).visit()
    
    def getDistanceV(self, v):
        return self.getV(v).getDistance()

    def setDistanceV(self, v, d):
        return self.getV(v).setDistance(d)

    def dijkstra_Init(self, init):
        for v in self.vertices:
            v.unvisit()
            v.setDistance(math.inf,acc=False)
        self.getV(init).setDistance(0, acc=False)

