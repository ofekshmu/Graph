from Edge import Edge
from Vertice import V
import math

class Graph:

    def __init__(self,
                        vertices: V = [],
                        edges: Edge = []):
        
        self.vertices = []
        for v in vertices:
            if isinstance(v,V):
                self.vertices.append(v)
            else:
                self.vertices.append(V(id=v))
        
        self.edges = []
        for e in edges:
            if isinstance(e, Edge):
                self.edges.appenf(e)
            else:
                print(f"{e} is not of type 'Edge'!")
    
    def addEdge(self, e: Edge):
        result = True
        if not isinstance(e,Edge):
            print("ERROR")
            result = False
        if e.start in self.vertices and e.end in self.vertices:
            self.edges.append(e)
        return result

    def forceEdge(self, e: Edge):
        result = True
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
    
    def popVertice(self, v: V):
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

