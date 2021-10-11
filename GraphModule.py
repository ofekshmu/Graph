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
        self.__vertices = {}
        self.__edges = {}
        self.__adj = {}

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
            self.__vertices[vId] = Vertice(vId)
            self.__adj[vId] = {} 
            return True
        
    def addEdge(self, v1, v2, weight = 1) -> bool:
        """
            @param v1: pointing vertice Id.
            @param v2: pointed vertice Id.
            @weight: numerical weight value.
            Adds edge (@v1,@v2) to the graph. 
            Returns True when successful, otherwise, False
            if edge exists in graph.
        """
        result = False
        c1, c2 = self.exists(v1), self.exists(v2)
        
        if c1 and c2 :
            if self.exists((v1,v2)):
                self.debuger("addEdge",f"Edge ({v1},{v2}), already exists!.")   
            else:
                self.__edges[(v1,v2)] = Edge(v1,v2,weight)
                self.__addAdj(v1,v2)
                result = True

        if not c1:
            self.debuger("addEdge",f"Failed inserting ({v1},{v2}), Vertice {v1} does not exist in graph.")
        if not c2:
            self.debuger("addEdge",f"Failed inserting ({v1},{v2}), Vertice {v2} does not exist in graph.")       
        
        return result

    def forceEdge(self, v1, v2, weight = 1) -> bool:
        """
            @param v1: pointing vertice Id.
            @param v2: pointed vertice Id.
            @weight: numerical weight value.
            Adds edge (@v1,@v2) to the graph. Upon missing vertices, adds
            one or both of them. Returns True when successful, otherwise, False
            if edge exists in graph.
        """
        if not self.exists((v1,v2)):    
            c1, c2 = self.exists(v1), self.exists(v2)

            if not c1:
                self.addVertice(v1)
                self.debuger("forceEdge",f"Vertice {v1} was forced.")        

            if not c2:
                self.addVertice(v2)
                self.debuger("forceEdge",f"Vertice {v2} was forced.")        
    
            self.__edges[(v1,v2)] = Edge(v1,v2,weight)
            self.__addAdj(v1,v2)
            return True
        self.debuger("forceEdge",f"Edge ({v1},{v2}) already exists.")        
        return False

    def popEdge(self, e: tuple) -> bool: 
        """
            @param e: an Edge in a tuple form: (v1,v2).
            Removes edge @e from graph and returns True if succesfell
        """
        if self.__edges.pop(e,None) == None:
            self.debuger("popEdge",f"Edge with an id {e} does not exist.")
            return False
        
        #remove from adj:
        (v1, v2) = e
        if self.__adj[v1].pop(v2, None) == None:
            return False
        return True
    
    def getUnvisited(self, vId = None) -> list: #list contains vertice Ids
        """
            @param vId: Id of Vertice.
            @Returns Ids list of unvisited Neighboors of @vId. If @vId is None,
            than returns all Unvisited Vertices Ids in the graph.
        """
        if vId is None:
            return [v.id for v in self.__vertices.values() if v.isUnvisited()]
        adj = self.__getAdj(vId)
        return [v.id for v in adj if v.isUnvisited()]

    def isAdj(self, v1, v2) -> bool:
        """ 
            @param v1: Id of Vertice.
            @param v2: Id of Vertice.
            Returns True if @v1 and @v2 are Neighboors,
            False otherwise.
        """
        try:
            self.__adj[v1][v2]
            return True
        except KeyError:
            return False

    def getAdj(self, vId) -> list: #list contains vertice Ids
        """ 
            @param vId: Id of Vertice.
            @Returns List of Neighboor Ids.
        """
        return [v.id for v in self.__getAdj(vId)]

    def exists(self, object) -> bool:
        """ 
            Check if an object exists in Graph, Edge or Vertice.
            Edges will be determined by a tuple structure.
        """
        if isinstance(object,tuple):
            return object in self.__edges
        else:
            return object in self.__vertices

    #TODO: test
    def setWeights(self, dict: dict) -> bool:
        """
            @param dict: a dictionary containing pairs of edges as keys,
            where edges are represented as tuples, and weights as values,
            where values are represented numerical types.
            Sets the given weights to the edges.
        """
        for e, w in dict.items():
            if not self.setWeight(e[0], e[1], w):
                self.debuger("setWeights",f"{e} was not found in graph.")
                return False
        return True
# --------------------------------- 
#       Private Functions
# --------------------------------- 
    def __getAdj(self, vId) -> List[Vertice]: #of type Vertice
        """ 
            @param vId: Id of Vertice.
            @Returns List of Neighboor Vertices.
        """
        return self.__adj[vId].values()
    
    def __addAdj(self, v1, v2):
        """ 
            @param v1: Id of Vertice.
            @param v2: Id of Vertice.
            Updates the Neighboor Dictionary according to the edge (@v1,@v2)
        """        
        if v1 in self.__adj:
            self.__adj[v1][v2] = self.__vertices[v2]
        else:
            self.__adj[v1] = {v2: self.__vertices[v2]}    

# --------------------------------- 
#       Vertice related Functions
# ---------------------------------     
    def getDistance(self, vId):
        if self.exists(vId):
            return self.__vertices[vId].distance
        else:
            raise KeyError(f"In GraphModule -> getDistnace: {vId} not found.")
    
    def setDistance(self, vId, d) -> bool:
        if self.exists(vId):
            self.__vertices[vId].distance = d
            return True
        else:
            self.debuger(f"In GraphModule -> setDistnace:", f"{vId} not found.")
            return False            

    def visit(self, vId):
        self.__vertices[vId].color = Color.gray
# --------------------------------- 
#       Edge related Functions
# ---------------------------------      
    def getWeight(self, v1, v2):
        if self.exists((v1,v2)):
            return self.__edges[(v1,v2)].weight
        else:
            raise KeyError(f"In GraphModule -> getWeight: {(v1,v2)} not found.")
          
    def setWeight(self, v1, v2, weight):
        if self.exists((v1, v2)):
            self.__edges[(v1, v2)].weight = weight
            return True
        else:
            self.debuger(f"In GraphModule -> setWeight:", f"{(v1, v2)} not found.")
            return False            

# --------------------------------- 
#       Extensions related Functions
# ---------------------------------   
    def _getEdges(self):
        return list(self.__edges.values())
    
    def _getVerticeIds(self):
        return list(self.__vertices.keys())

    def _dijkstra_Init(self, init):
        """
            Initializes Graph for Dijkstra Algorithem.
            @param init: Id of inital Vertice
            1. Mark all vertices as unvisited (Color.white)
            2. Set distances of all vertices to  infinity
            3. Set distance of initial Vertice to 0
        """
        for v in self.__vertices.values():
            v.unvisit()
            v.distance = math.inf
        self.__vertices[init].distance = 0
#---------------------------------------
    
    def debuger(self, function :str, message :str):
        if self.debug: 
            print("\n",10*'~ ',f" Message in Graph Infrustructure -> {function} ",10*'~ ',"\n",message,"\n")

    def __repr__(self):
        str = "\nGraph:\n"
        for vId in self.__vertices.keys():
            str += f"\t{vId} -->  "
            for vId2 in self.__adj[vId].keys():
                str += f"{vId2}, "
            str = str[:-2]
            str += "\n"

        return str
