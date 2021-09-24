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
        for vId in vertices:
            if isinstance(vId,V):
                self.vertices[vId.getId()] = vId
            else:
                self.vertices[vId] = V(id=vId)
        
        #TODO: add a force option for edges
        self.edges = []
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
                self.edges.append(e)
                if not self.directed:
                    self.edges.append(e.flippedInstance())
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
        if result: self.edges.append(e)
        return result

    def popEdge(self, e: Edge):
        result = True
        if e in self.edges:
            self.edges.remove(e)
        else:
            result = False
        return result
    
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
            if v.getId() == v_end:
                return True
        return False 

    def NeighboorsOf(self, v): # TODO method impl is not efficient!
        lst = []
        for e in self.edges:
            if e.getStartId() == v:
                lst.append(self.getVertice(e.getEndId()))
        return lst

    def getNeighboors(self, vId, unvisited = False):
        NotImplemented()

    def getVertice(self, vId) -> V:
        if vId in self.vertices:
            return self.vertices[vId]
        else:
            self.debuger("getVertice",f"{vId} is not a vertice in the current graph")
            return None
            

    def exists(self, object: Edge) -> bool:
        if isinstance(object, Edge):
            return object in self.edges
        elif object in self.vertices:
            return True
        else:
            print(f"object is not of Type Edge or Vertice")
            return False

    def vExists(self, vId) -> bool:
        return vId in self.vertices

    def __repr__(self):
        dict = {}
        for vId in self.vertices.keys():
            dict[vId] = []
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
        return [self.edges,self.vertices.values()]
    
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

