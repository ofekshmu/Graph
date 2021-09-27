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
    
    # ---------------- Private -----------------
    def __ValidInsertion(self, e, force) -> bool:
        """ Private Function
            Given a tuple @e representing an edge. validates if the presence of the edge in
            the graph is valid and @returns True and False otherwise.
            Upon receiving a @force = True, might add new edges to graph to enable edge insertion.
        """
        pass

    def __debuger(self, function :str, message :str):
        """ Private function
            for printing Messages in infrustructure
        """
        pass

    def __e_str(self, e):
        """ Pricvate function
            for printing edges
        """ 
        pass
       
    def __repr__(self):
        """ Returns a string describing the Graph"""
        pass

    def addEdge(self, e, force : bool = False) -> bool:
        """ adds an edge to the graph.
            on successful insertion returns True, False otherwise 
        """        
        pass

    def forceEdge(self, e: tuple) -> bool:
        """ forces an edge onto the graph.
            on successful force, returns True, False otherwise.
            forcing an edge defines as adding its vertices when they are missing in the graph.
            vertices will be added only if graph rules are met upon insertion.
        """
        pass

    def addVertice(self, v) -> bool:
        """ Adds a new vertice @v to the graph 
            Returns True upon successful insertion, False otherwise.
        """
        pass

    def exists(self, value) -> bool:
        """
        Receives either a vertices or an Edge and returns True
        if is present in graph, False otherwise.
        Edge is represented by a tuple while vertice could be represented by any type.
        """
        pass
    
    def isNeighboors(self, v1, v2) -> bool:
        """ Returns True if edge v1-->v2 exists, False otherwise"""
        pass 
    # --------- GETTERS ---------
    def getVertices(self) -> list:
        """Returns a list of the vertices in the graph """
        pass

    def getEdges(self) -> list:
        """Returns a list of egdes in the graph"""
        pass

    def getNeighboors(self, v) -> list:
        """ Returns the the neighboors of @v.
            throws a RunTimeError if @v does not exist in graph
        """
        pass
    # --------- SETTERS ---------
    def setDebugMode(self, state : bool = True):
        """ Change the graphs debug mode """
        pass 
     