from Edge import Edge

class Graph(Edge):
    
    def __init__(self,
                    vertices : list = [],
                    edges : list = [], 
                    # Graph Settings
                    duplicates :bool = False, 
                    loops : bool = False,
                    debug : bool = False):

        self.loops = loops
        self.graph = {}
        self.edgeList = []
        self.debug = debug
        self.duplicates = duplicates

        print(type(vertices),vertices)
        for v in vertices:
            self.addVertice(v)
        for e in edges:
            self.addEdge(e, force = True)

    def _ValidInsertion(self, e: Edge, force):
        [isExist, isStart, isEnd] = [self.exists(e), self.exists(e.start), self.exists(e.end)]
        #print(e,isExist,isStart,isEnd)
        if isExist:
            if self.duplicates:
                if e.isLoop() and not self.loops:
                    self.debuger("_ValidInsertion",f"{e} was Rejected:\nEdge is a loop in a graph with NO loops.")
                    return False
                return True
            self.debuger("_ValidInsertion",f"{e} was Rejected:\nThe graph does not enable duplicates.")
            return False
        else:
            if e.isLoop() and not self.loops:
                self.debuger("_ValidInsertion",f"{e} was Rejected:\nEdge is a loop in a graph with NO loops.")
                return False
            if isStart and isEnd:
                return True
            else:
                if force:
                    if not isStart: 
                        self.addVertice(e.start)
                        self.debuger("_ValidInsertion",f"{e.start} was Forced.")
                    if not isEnd : 
                        self.addVertice(e.end)
                        self.debuger("_ValidInsertion",f"{e.end} was Forced.")
                    return True
                return False

    def addEdge(self, e : Edge, force : bool = False):
        """doc"""
        valid = self._ValidInsertion(e, force)
        if valid:
            self.graph[e.start].append(e.end)
            self.graph[e.end].append(e.start)
            self.edgeList.append(e)
        return valid

    def addVertice(self, v):
        """ Adds a new vertice @v to the graph """
        if v in self.graph.keys():
            self.debuger("addVertice",f"{v} is already a vertice in the graph.")
            return False
        else:
            self.graph[v] = []
            return True
         
    def exists(self, value):
        """
        Receives either a vertices or an Edge and returns True
        if is present in graph, False otherwise.
        """
        if isinstance(value, Edge):
            if value.start in self.graph.keys():
                if value.end in self.graph[value.start]:
                    return True
            """ Notice, The check here is done from start to end. While in Normal
                Graph it doesn't matter because the edge appears both ways, it does matter
                in directional graph. """
        else:
            if value in self.graph.keys():
                return True
        return False 

    def getVertices(self):
        """@returns a list of the vertices in the graph """
        return list(self.graph.keys())

    def getVerticesCount(self):
        """@returns the number of vertices in the graph"""
        return len(self.graph.keys())
    
    def getEdges(self):
        """doc"""
        return self.edgeList

    def getNeighboors(self, v):
        """
        @returns the the neighboors of @v.
        throws an error if @vb does not exist in graph"""
        if self.exists(v):
            return self.graph[v]
        else:
            self.debuger("getNeighboors",f"Vertice {v} does not exist.\nNo list returned.")
            raise RuntimeWarning

    def setDebugMode(self, state : bool = True):
        self.debug = state

    def debuger(self, function :str, message :str):
        if self.debug: 
            print(10*'-',f" Message in Graph Infrustructure -> {function} ",10*'-',"\n",message,"\n")

    def __repr__(self):
        string =20*'-'+"\n"
        if self.graph == {}:
            string += "The Graph is EMPTY!\n"
        else:
            string += "Graph Preview:\n"
            for v in self.graph.keys():
                string += f"\t\t{v} --> "
                for neigh in self.getNeighboors(v):
                    string += f" {neigh},"
                string = string[:-1] +"\n"                #cut the last comma
            loopM = "enabled" if self.loops else "disabled"
            dupM = "enabled" if self.duplicates else "disabled"
            string += f"Loops are {loopM},\nDuplicates are {dupM}.\n"
        string +=20*'-'+"\n"
        return string
