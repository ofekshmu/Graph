from typing import List
from numpy import void
from SimpleGraphInterface import InformalSimpleGraphInterface

class Graph(InformalSimpleGraphInterface):
    
    def __init__(self,
                    vertices: list = [],
                    edges: list = [], 
                    # Graph Settings
                    duplicates: bool = False, 
                    loops: bool = False,
                    directed: bool = False,
                    debug: bool = False):

        self.__duplicates = duplicates
        self.__loops = loops
        self.__directed = directed
        self.__debug = debug

        self.__edgeList = []
        self.__graph = {}

        for v in vertices:
            if not self.addVertice(v):
                self.__debuger("Graph Constructor",f"Graph was not created properly:\ntwo or more identical vertices '{v}'.")
        for e in edges:
            if not self.addEdge(e):
                self.__debuger("Graph Constructor",f"Graph was not created properly:\nEdge {self.__e_str(e)} was not added.")

    def __ValidInsertion(self, e: tuple, force) -> bool:
        """ Private Function
            Given a tuple @e representing an edge. validates if the presence of the edge in
            the graph is valid and @returns True and False otherwise.
            Upon receiving a @force = True, might add new edges to graph to enable edge insertion.
        """
        [isExist, isStart, isEnd] = [self.exists(e), self.exists(e[0]), self.exists(e[1])]
        if isExist:
            if self.__duplicates:
                if e[0] == e[1] and not self.__loops:
                    self.__debuger("__ValidInsertion",f"{self.__e_str(e)} was Rejected:\nEdge is a loop in a graph with NO loops.")
                    return False
                return True
            self.__debuger("__ValidInsertion",f"{self.__e_str(e)} was Rejected:\nThe graph does not enable duplicates.")
            return False
        else:
            if e[0] == e[1] and not self.__loops:
                self.__debuger("__ValidInsertion",f"{self.__e_str(e)} was Rejected:\nEdge is a loop in a graph with NO loops.")
                return False
            if isStart and isEnd:
                return True
            else:
                if force:
                    if not isStart: 
                        self.addVertice(e[0])
                        self.__debuger("__ValidInsertion",f"'{e[0]}' was Forced.")
                    if not isEnd : 
                        self.addVertice(e[1])
                        self.__debuger("__ValidInsertion",f"'{e[1]}' was Forced.")
                    return True
                return False

    def addEdge(self, e: tuple) -> bool:
        """ adds an edge to the graph.
            on successful insertion returns True, False otherwise 
        """
        valid = self.__ValidInsertion(e, force= False)
        if valid:
            self.__graph[e[0]].append(e[1])
            self.__edgeList.append(e)           
            if not self.__directed:
                self.__graph[e[1]].append(e[0])
                self.__edgeList.append((e[1],e[0]))
        return valid

    def forceEdge(self, e: tuple) -> bool:
        """ forces an edge onto the graph.
            on successful force, returns True, False otherwise.
            forcing an edge defines as adding its vertices when they are missing in the graph.
            vertices will be added only if graph rules are met upon insertion.
        """
        valid = self.__ValidInsertion(e, force = True)
        if valid:
            self.__graph[e[0]].append(e[1])
            self.__edgeList.append(e)           
            if not self.__directed:
                self.__graph[e[1]].append(e[0])
                self.__edgeList.append((e[1],e[0]))
        return valid

    def addVertice(self, v):
        """ Adds a new vertice @v to the graph 
            Returns True upon successful insertion, False otherwise.
        """
        if v in self.__graph.keys():
            self.__debuger("addVertice",f"'{v}'' is already a vertice in the graph.")
            return False
        else:
            self.__graph[v] = []
            return True
         
    def exists(self, value) -> bool:
        """
        Receives either a vertices or an Edge and returns True
        if is present in graph, False otherwise.
        Edge is represented by a tuple while vertice could be represented by any type.
        """
        if isinstance(value, tuple):
            if value[0] in self.__graph.keys():
                if value[1] in self.__graph[value[0]]:
                    return True
            """ Notice, The check here is done from start to end. While in Normal
                Graph it doesn't matter because the edge appears both ways, it does matter
                in directional graph. """
        else:
            if value in self.__graph.keys():
                return True
        return False 

    def getVertices(self) -> list:
        """Returns a list of the vertices in the graph """
        return list(self.__graph.keys())
    
    def getEdges(self) -> list:
        """Returns a list of egdes in the graph"""
        return self.__edgeList

    def getNeighboors(self, v) -> list:
        """ Returns the the neighboors of @v.
            throws a RunTimeError if @v does not exist in graph
        """
        if self.exists(v):
            return self.__graph[v]
        else:
            self.__debuger("getNeighboors",f"Vertice '{v}'' does not exist.\nNo list returned.")
            raise RuntimeWarning

    def isNeighboors(self, v1, v2) -> bool:
        """ Returns True if edge v1-->v2 exists, False otherwise"""
        # valid for both direct and undirected graph
        return (v1,v2) in self.__edgeList


    def setDebugMode(self, state: bool = True):
        """ Change the graphs debug mode """
        self.__debug = state

    def __debuger(self, function: str, message: str):
        """ Private function
            for printing Messages in infrustructure
        """
        if self.__debug: 
            print("\n",10*'-',f" Message in Graph Infrustructure -> {function} ",10*'-',"\n",message,"\n")

    def __e_str(self, e):
        """ Pricvate function
            for printing edges
        """
        con = "--" if self.__directed else "->"
        return f"{e[0]}{con}{e[1]}"
            

    def __repr__(self):
        """ Returns a string describing the Graph"""
        string =20*'-'+"\n"
        if self.__graph == {}:
            string += "The Graph is EMPTY!\n"
        else:
            string += "Graph Preview:\n"
            for v in self.__graph.keys():
                string += f"\t\t{v} --> "
                for neigh in self.getNeighboors(v):
                    string += f" {neigh},"
                string = string[:-1] +"\n"                #cut the last comma
            loopM = "enabled" if self.__loops else "disabled"
            dupM = "enabled" if self.__duplicates else "disabled"
            string += f"Graph Settings:\n\tLoops are {loopM},\n\tDuplicates are {dupM}.\n"
        string +=20*'-'+"\n"
        return string

# remove edge
# remove vertice