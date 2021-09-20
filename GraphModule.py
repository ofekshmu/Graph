from typing import Optional, Union
from CompEdge import Edge
from Vertice import V
import math

class Graph:

    def __init__(self,
                        vertices: V = [],
                        edges: Edge = [],
                        directed = True):
        # NEED TO CHECK FOR DUPLICATES
        self.directed = directed

        self.vertices = []
        for v in vertices:
            if isinstance(v,V):
                self.vertices.append(v)
            else:
                self.vertices.append(V(id=v))
        
        self.edges = []
        for e in edges:
            if isinstance(e, Edge):
                self.addEdge(e)
            else:
                print(f"{e} is not of type 'Edge'!")

        self.directed = directed
    
    def addEdge(self, e: Edge):
        result = True
        if not isinstance(e,Edge):
            print("ERROR")
            result = False
        if self.directed: e.setAsDirected()
        if self.vExists(e.getStart()) in self.vertices and self.vExists(e.getEnd()) in self.vertices:
            self.edges.append(e)
            if self.directed:
                self.edges.append(e.flippedInstance())
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
            if e.start == v:
                lst.append(e.end)
        return lst

    def exists(self, object: Union[Edge,V]):
        if isinstance(object,V):
            return object in self.vertices
        elif isinstance(object, Edge):
            return object in self.edges
        else:
            print(f"object is not of Type Edge or Vertice")

    def vExists(self, id):
        for v in self.vertices:
            if id == v.getId():
                return True
        return False

    def __repr__(self):
        dict = {}
        for v in self.vertices:
            dict[v.id] = []
        for e in self.edges:
            dict[e.getStart()].append(e.getEnd())

        str = ""
        for k,v in dict.items():
            str += f"{k} -->"
            for vertice in v:
                str += f" {vertice},"
            str = str[:-1] +"\n"
        return str
    
    def getRaw(self):
        return [self.edges,self.vertices]

