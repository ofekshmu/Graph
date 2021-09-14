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

        for v in vertices:
            self.addVertice(v)
        for e in edges:
            self.addEdge(e, force = True)

    def _ValidInsertion(self, e: Edge, force):
        [isExist, isStart, isEnd] = [self.exists(e), self.exists(e.start), self.exists(e.start)]
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
            elif force:
                if not isStart: 
                    self.addVertice(e.start)
                    self.debuger("_ValidInsertion",f"{e.start} was Forced.")
                if not isEnd : 
                    self.addVertice(e.end)
                    self.debuger("_ValidInsertion",f"{e.e} was Forced.")
                return True

    def addEdge(self, e : Edge, force : bool = False):
        """doc"""
        valid = self._ValidInsertion(e, force)
        if valid:
            self.graph[e.start] = e.end
            self.graph[e.end] = e.start
            self.edgeList.append(e)
            self.edgeList.append(e.flippedInstance())
        return valid


    def addVertice(self, v):
        """ Adds a new vertice @v to the graph """
        if v in self.graph.keys():
            self.debuger("addVertice",f"{v} is already a vertice in the graph.")
        else:
            self.graph[v] = []
        
    
    def exists(self, value):
        """
        Receives either a vertices or an Edge and returns True
        if is present in graph, False otherwise.
        """
        if isinstance(value, Edge):
            end_exists = value.end in self.graph.keys()
            start_exists = value.start in self.graph.keys()
            if end_exists and start_exists:
                if value.end in self.graph[value.start]:
                    return True
            #if not value._isDir():
                #value._flip()
                #check again for normal edges
        else:
            if value in self.graph.keys():
                return True
        return False 

    def getVertices(self):
        """@returns a list of the vertices in the graph """
        return list(self.graph.values())

    def getVerticesCount(self):
        """@returns the number of vertices in the graph"""
        return len(self.graph.keys())

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
            dirM = "enabled" if self.directed else "disabled"
            dupM = "enabled" if self.duplicates else "disabled"
            string += f"Loops are {loopM},\nEdge Direction is {dirM},\nDuplicates are {dupM}.\n"
        string +=20*'-'+"\n"
        return string


#some tests for the time being:
g = Graph(debug=False, duplicates=False,loops=False)
print(g)
g.addVertice(1)
print(g.exists(1))
g.addEdge(Edge(1,2),force=True)
g.addEdge(Edge(1,2))

g.addEdge(Edge(5,5),force=True)
g.addEdge(Edge(5,5),force=True)
g.addEdge(Edge(7,7),force=True)

#print(g)
e = Edge(1,2)
g.addEdge(e,force=True)
g.addEdge(Edge(1,3),force=True)
print(g.exists(Edge(1,2)))
g.addEdge(Edge(5,6),force=True)
g.addEdge(Edge(5,6),force=True)

print(g.getNeighboors(5))
#print(g.getNeighboors(1))
print(g)

#g2 = Graph(vertices=[1,2,5,7,23],edges=[Edge(1,2),Edge(5,7),Edge(10,1),Edge(20,25)])
#print(g2)

#implement of non directional double edges
# implement check of both sided edges where flipped 