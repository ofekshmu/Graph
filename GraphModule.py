from Edge import Edge
from Vertice import Color, Vertice
from typing import List
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
            self.addVertice(vId)
        
        for e in edges:
            if isinstance(e, tuple):
                if not self.addEdge(e[0],e[1]):
                    self.debuger("Graph Constructor",f"{e} Was not added!")
            else:
                self.debuger("Graph Constructor", f"{e} is not of type 'Edge'!")

    def addVertice(self, vId) -> bool:
        if self.exists(vId):
            self.debuger("addVertice",f"Failed inserting '{vId}', a vertice with id {vId} already exists.")
            return False
        else:
            self.vertices[vId] = Vertice(vId)
            self.adj[vId] = {}
            return True

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
            self.debuger("addEdge",f"Failed inserting ({v1},{v2}), Vertice {v1} does not exist in graph.")
        if not c2:
            self.debuger("addEdge",f"Failed inserting ({v1},{v2}), Vertice {v2} does not exist in graph.")       
        
        return result

    def forceEdge(self, v1, v2, weight = 1):
        if not self.exists((v1,v2)):    
            c1, c2 = self.exists(v1), self.exists(v2)

            if not c1:
                self.addVertice(v1)
                self.debuger("forceEdge",f"Vertice {v1} was forced.")        

            if not c2:
                self.addVertice(v2)
                self.debuger("forceEdge",f"Vertice {v2} was forced.")        
    
            self.edges[(v1,v2)] = Edge(v1,v2,weight)
            self._addAdj(v1,v2)
            return True
        self.debuger("forceEdge",f"Edge ({v1},{v2}) already exists.")        
        return False

    def popEdge(self, e: tuple) -> bool: 
        if self.edges.pop(e,None) == None:
            self.debuger("popEdge",f"Edge with an id {e} does not exist.")
            return False
        
        #remove from adj:
        (v1, v2) = e
        if self.adj[v1].pop(v2, None) == None:
            return False
        return True
    
    # def popVertice(self, vId) -> bool: #TODO impl func to check if vertice is slo
    #     # check if edges are attached
    #     e = self.adj.get(vId, default = None)
    #     # TODO:what about edges pointing to self?
    #     if e != None:
    #         self.debuger("popVertice",f"{vId} was not removed, {e} is attached to it")
    #         return False

    #     if self.edges.pop(vId ,None) == None:
    #         self.debuger("popEdge",f"Vertice with an id {vId} does not exist.")
    #         return False

    #     return True
    
    def getUnvisited(self, vId = None) -> List[Vertice]: #of type Vertice
        if vId is None:
            return [v.id for v in self.vertices.values() if v.isUnvisited()]
        #white is defined as unvisited
        adj = self.__getAdj(vId)
        return [v.id for v in adj if v.isUnvisited()]

    def isAdj(self, v1, v2) -> bool:
        """ Returns True if @param v1 and @param v2 are Neighboors,
            False otherwise."""
        try:
            self.adj[v1][v2]
            return True
        except KeyError:
            return False

    def __getAdj(self, vId) -> List[Vertice]: #of type Vertice
        """ Returns a list of Neighboors of @param vId"""
        return self.adj[vId].values()

    def getAdj(self, vId):
        return [v.id for v in self.__getAdj(vId)]
    #TODO: not used
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
        str = "Graph:\n"
        for vId in self.vertices.keys():
            str += f"\t{vId} -->  "
            for vId2 in self.adj[vId].keys():
                str += f"{vId2}, "
            str = str[:-2]
            str += "\n"

        return str

#--------------------------------------- Vertice related
    def getDistance(self, vId):
        return self.vertices[vId].distance
    
    def setDistance(self, vId, d):
        self.vertices[vId].distance = d

    def visit(self, vId):
        self.vertices[vId].color = Color.gray
#--------------------------------------- Edge related
    def getWeight(self, v1, v2):
        return self.edges[(v1,v2)].weight

#--------------------------------------- Graph Extensions related
    def _getEdges(self):
        return list(self.edges.values())
    
    def _getVerticeIds(self):
        return list(self.vertices.keys())
#---------------------------------------
    
    def debuger(self, function :str, message :str):
        if self.debug: 
            print("\n",10*'~',f" Message in Graph Infrustructure -> {function} ",10*'~',"\n",message,"\n")

#---------------------------------------
    def dijkstra_Init(self, init):
        for v in self.vertices.values():
            v.unvisit()
            v.distance = math.inf
        self.vertices[init].distance = 0

