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
        if e.start in self.vertices and e.end in self.vertices:
            self.edges.append(e)

    def forceEdge(self, e: Edge):
        if not e.start in self.vertices:
            self.vertices.append(V(id=e.start))
        if not e.end in self.vertices:
            self.vertices.append(V(id=e.end))
        self.edges.append(e)

    def popEdge(self, e: Edge):
        NotImplemented()
    
    def popVertice(self, v: V):
        NotImplemented()
    
    def getUnvisited():
        NotImplemented()

    def NeighboorsOf(v: V):
        NotImplemented()

