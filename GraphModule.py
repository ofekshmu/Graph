from typing import Optional, Union
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

        self.vertices = []
        for vId in vertices:
            if isinstance(vId,V):
                self.vertices.append(vId)
            else:
                self.vertices.append(V(id=vId))
        
        self.edges = []
        for e in edges:
            if isinstance(e, Edge):
                if not self.addEdge(e):
                    self.debuger("Graph Constructor",f"{e} Was not added!")
            else:
                self.debuger("Graph Constructor", f"{e} is not of type 'Edge'!")

        self.directed = directed
    
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
            print("ERROR")
            result = False
        if not e.start in self.vertices:
            self.vertices.append(V(id=e.start))
        if not e.end in self.vertices:
            self.vertices.append(V(id=e.end))
        if result: self.edges.append(e)
        return result

    def popEdge(self, e: Edge):
        result = True
        if e in self.edges:
            self.edges.remove(e)
        else:
            result = False
        return result
    
    def popVertice(self, v: V): #problematic( what about connecting edges??)
        print(f"method implicates errors, do not use!")
        result = True
        if v in self.vertices:
            self.edges.remove(v)
        else:
            result = False
        return result
    
    def getUnvisited(self):
        lst = []
        for v in self.vertices:
            if not v.isVisited():
                lst.append(v)
        return lst

    def NeighboorsOf(self, v: V): # TODO method impl is not efficient!
        lst = []
        for e in self.edges:
            if e.getStartId() == v:
                lst.append(self.getV(e.getEndId()))
        return lst

    def getV(self, vId) -> V:
        for v in self.vertices:
            if vId == v.getId():
                return v
        self.debuger("getV",f"{v} was not found in graph!")

    def exists(self, object: Union[Edge,V]) -> bool:
        if isinstance(object,V):
            return object in self.vertices
        elif isinstance(object, Edge):
            return object in self.edges
        else:
            print(f"object is not of Type Edge or Vertice")

    def vExists(self, id) -> bool:
        for v in self.vertices:
            if id == v.getId():
                return True
        return False

    def __repr__(self):
        dict = {}
        for v in self.vertices:
            dict[v.id] = []
        for e in self.edges:
            dict[e.getStartId()].append(e.getEndId())

        str = ""
        for k,v in dict.items():
            str += f"{k} -->"
            for vertice in v:
                str += f" {vertice},"
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
                return e.getWeight()

    def visit(self, v: V):
        v.visit()
    
    def getDistanceV(self, v: V):
        return self.getV(v).getDistance()

    def setDistanceV(self, v: V, d):
        return self.getV(v).setDistance(d)

    def __dijkstra_Init(self, init):
        for v in self.vertices:
            v.unvisit()
            v.setDistance(math.inf,acc=False)
        self.getV(init).setDistnace(0, acc=False)

