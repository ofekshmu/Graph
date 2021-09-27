
from SimpleGraphModule import Graph
from Edge import Edge

class InformalSimpleGraphInterface:
    def __init__(self,
                    vertices: list = [],
                    edges: list = [], 
                    # Graph Settings
                    duplicates: bool = False, 
                    loops: bool = False,
                    directed: bool = False,
                    debug: bool = False) -> Graph:        
        """doc"""
        pass

    def _ValidInsertion(self, e: Edge, force) -> bool:
        """doc"""
        pass

    def addEdge(self, e : Edge, force : bool = False) -> bool:
        """doc"""
        pass

    def addVertice(self, v):

    def exists(self, value):

    def getVertices(self):

    def getVerticesCount(self):

    def getEdges(self):

    def getNeighboors(self, v):

    def setDebugMode(self, state : bool = True):

    def debuger(self, function :str, message :str):

    def __repr__(self):
