from typing import List, Optional, Union
from CompEdge import Edge
from Vertice import V
import math

class Graph(V, Edge):

    def __init__(self,
                        vertices: V = [],
                        edges: Edge = [],
                        directed = True,
                        debug = False):
        # NEED TO CHECK FOR DUPLICATES
        self.debug = debug
        self.directed = directed

        self.vertices = {}
        self.edges = {}
        for vId in vertices:
            if isinstance(vId,V):
                self.vertices[vId.getId()] = vId
                self.edges[vId.getId()] = []
            else:
                self.vertices[vId] = V(id=vId)
                self.edges[vId] = []
        
        #TODO: add a force option for edges
        for e in edges:
            if isinstance(e, Edge):
                if not self.addEdge(e):
                    self.debuger("Graph Constructor",f"{e} Was not added!")
            else:
                self.debuger("Graph Constructor", f"{e} is not of type 'Edge'!")

    
    def addEdge(self, e: Edge):
        result = False
        #sanity check
        if not isinstance(e,Edge):
            self.debuger("addEdge",f"{e} is not of type 'Edge'!")
        else:
            if self.directed: e.setAsDirected()
            if self.vExists(e.getStartId()) and self.vExists(e.getEndId()) :
                #self.edges.append(e)
                self.edges[e.getStartId()].append(e)
                if not self.directed:
                    self.edges[e.getEndId()].append(e.flippedInstance())
                result = True
        return result

    def forceEdge(self, e: Edge):
        result = True
        if self.directed: e.setAsDirected()
        if not isinstance(e,Edge):
            print(f"tried forcing {e} which is not an edge!")
            result = False
    
        if not e.getStartId() in self.vertices:
            self.vertices[e.getStartId()].append(V(id=e.getStartId()))
        if not e.getEndId() in self.vertices:
            self.vertices[e.getEndId()].append(V(id=e.getEndId()))
        if result:
            self.edges[e.getStartId()].append(e)
            if not self.directed:
                self.edges[e.getEndId()].append(e.flippedInstance())
        return result

    def popEdge(self, e_in: Edge):
        res = self.getEdge(e_in)
        self.edges[e_in.getStartId()].remove(e_in) #TODO might be possible that value being deleted is deleting "res" too, might need deep copy
        return res

    def getEdge(self, e_in: Edge):
        """"""
        lst =  self.edges[e_in.getStartId()]
        for e in lst:
            if e.getStartId() == e_in.getStartId():
                return e
        self.debuger("getEdge","Edge {e} was not found")
        return False

    def popVertice(self, vId) -> V: #TODO:problematic( what about connecting edges??)
        print(f"method implicates errors, do not use!")

        result = self.vertices.pop(vId, None)
        if result == None:
            print(f"{vId} was not found\nNone returned!")

        return result
    
    def getUnvisited(self, vId) -> List: # TODO: implement with edge dictionary to save using isNei...
        lst = []
        for v in self.vertices.values():
            if not v.isVisited() and self.isNeighboors(vId, v.getId()):
                lst.append(v)
        return lst

    def isNeighboors(self, v_start, v_end):
        lst = self.NeighboorsOf(v_start)
        for v in lst:
            if v == v_end:
                return True
        return False 

    def NeighboorsOf(self, vId): # TODO can have duplicates in dup graph
        lst = []
        for e in self.edges[vId]:
            lst.append(e.getEndId())
        return lst

    def getNeighboors(self, vId, unvisited = False):
        NotImplemented()

    def getVertice(self, vId) -> V:
        if vId in self.vertices:
            return self.vertices[vId]
        else:
            self.debuger("getVertice",f"{vId} is not a vertice in the current graph")
            return None
            

    def Eexists(self, object: Edge) -> bool:
        if self.getEdge(object) == False:
            return False
        return True

    def vExists(self, vId) -> bool:
        return vId in self.vertices

    def __repr__(self):
        dict = {}

        str = ""
        for vId in self.vertices.keys():
            str += f"{vId} --> "
            for e in self.edges[vId]:
                str += f"{e.getEndId()},"
            str = str[:-1] +"\n"
        return str
    
    def debuger(self, function :str, message :str):
        if self.debug: 
            print("\n",10*'~',f" Message in Graph Infrustructure -> {function} ",10*'~',"\n",message,"\n")

    def getRaw(self):
        return [self.edges,self.vertices.values()]
    
    def getWeight(self, e: Edge):
        edge = self.getEdge(e)
        return edge.getWeight()
    
    def setWeight(self, e: Edge, w):
        edge = self.getEdge(e)
        edge.setWeight(w)
        return True

    def visit(self, vId):
        self.getVertice(vId).visit()
    
    def getDistanceV(self, vId):
        return self.getVertice(vId).getDistance()

    def setDistanceV(self, vId, distance):
        return self.getVertice(vId).setDistance(distance)

    def dijkstra_Init(self, init):
        for v in self.vertices.values():
            v.unvisit()
            v.setDistance(math.inf)
        self.getVertice(init).setDistance(0, acc=False)

