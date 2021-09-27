class InformalSimpleGraphInterface:
    def __init__(self,
                    vertices: list = [],
                    edges: list = [], 
                    # Graph Settings
                    duplicates: bool = False, 
                    loops: bool = False,
                    directed: bool = False,
                    debug: bool = False):        
        """doc"""
        pass

    def __ValidInsertion(self, e, force) -> bool:
        """doc"""
        pass

    def addEdge(self, e, force : bool = False) -> bool:
        """doc"""
        pass

    def addVertice(self, v) -> bool:
        """doc"""
        pass

    def exists(self, value) -> bool:
        """doc"""
        pass
    
    def getVertices(self) -> list:
        """doc"""
        pass

    def getEdges(self):
        """doc"""
        pass

    def getNeighboors(self, v):
        """doc"""
        pass
    
    def setDebugMode(self, state : bool = True):
        """doc"""
        pass
    
    def debuger(self, function :str, message :str):
        """doc"""
        pass
    
    def __repr__(self):
        """doc"""
        pass
    