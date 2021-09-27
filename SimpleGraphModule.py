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
                self.debuger("Graph Constructor",f"Graph was not created properly:\ntwo or more identical vertices '{v}'.")
        for e in edges:
            if not self.forceEdge(e):
                self.debuger("Graph Constructor",f"Graph was not created properly:\n Edge {self.__e_str(e)} was not added.")

    def __ValidInsertion(self, e: tuple, force):
        """"""
        [isExist, isStart, isEnd] = [self.exists(e), self.exists(e[0]), self.exists(e[1])]
        #print(e,isExist,isStart,isEnd)
        if isExist:
            if self.__duplicates:
                if e[0] == e[1] and not self.__loops:
                    self.debuger("__ValidInsertion",f"{self.__e_str(e)} was Rejected:\nEdge is a loop in a graph with NO loops.")
                    return False
                return True
            self.debuger("__ValidInsertion",f"{self.__e_str(e)} was Rejected:\nThe graph does not enable duplicates.")
            return False
        else:
            if e[0] == e[1] and not self.__loops:
                self.debuger("__ValidInsertion",f"{self.__e_str(e)} was Rejected:\nEdge is a loop in a graph with NO loops.")
                return False
            if isStart and isEnd:
                return True
            else:
                if force:
                    if not isStart: 
                        self.addVertice(e[0])
                        self.debuger("__ValidInsertion",f"'{e[0]}' was Forced.")
                    if not isEnd : 
                        self.addVertice(e[1])
                        self.debuger("__ValidInsertion",f"'{e[1]}' was Forced.")
                    return True
                return False

    def addEdge(self, e: tuple) -> bool:
        """doc"""
        valid = self.__ValidInsertion(e, force= False)
        if valid:
            self.__graph[e[0]].append(e[1])
            self.__edgeList.append(e)           
            if not self.__directed:
                self.__graph[e[1]].append(e[0])
                self.__edgeList.append((e[1],e[0]))
        return valid

    def forceEdge(self, e: tuple) -> bool:
        """doc"""
        valid = self.__ValidInsertion(e, force = True)
        if valid:
            self.__graph[e[0]].append(e[1])
            self.__edgeList.append(e)           
            if not self.__directed:
                self.__graph[e[1]].append(e[0])
                self.__edgeList.append((e[1],e[0]))
        return valid

    def addVertice(self, v):
        """ Adds a new vertice @v to the graph """
        if v in self.__graph.keys():
            self.debuger("addVertice",f"'{v}'' is already a vertice in the graph.")
            return False
        else:
            self.__graph[v] = []
            return True
         
    def exists(self, value):
        """
        Receives either a vertices or an Edge and returns True
        if is present in graph, False otherwise.
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

    def getVertices(self):
        """@returns a list of the vertices in the graph """
        return list(self.__graph.keys())
    
    def getEdges(self):
        """doc"""
        return self.__edgeList

    def getNeighboors(self, v):
        """
        @returns the the neighboors of @v.
        throws an error if @vb does not exist in graph"""
        if self.exists(v):
            return self.__graph[v]
        else:
            self.debuger("getNeighboors",f"Vertice '{v}'' does not exist.\nNo list returned.")
            raise RuntimeWarning

    def setDebugMode(self, state : bool = True):
        self.__debug = state

    def debuger(self, function :str, message :str):
        if self.__debug: 
            print("\n",10*'-',f" Message in Graph Infrustructure -> {function} ",10*'-',"\n",message,"\n")

    def __e_str(self, e):
        con = "--" if self.__directed else "->"
        return f"{e[0]}{con}{e[1]}"
            

    def __repr__(self):
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
