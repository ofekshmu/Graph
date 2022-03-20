from typing import Union
from GraphModule import Graph
import numpy as np

class AdjMatrix(Graph):
    
    @staticmethod
    def get(g: Graph):
        """@returns an Adjacency matrix and an dictionary representing vertices indexes """
        #variables
        edge_list = g._getEdges()
        vertices = g._getVerticeIds()
        dim = len(vertices)
        matrix = np.zeros((dim,dim),dtype=np.int32)
        #associate a vertice with an index
        index_dict = {vertices[i]: i for i in range(dim)}
        #fill matrix
        for e in edge_list:
            row = index_dict[e.start]
            col = index_dict[e.end]
            matrix[row][col] = 1

        return matrix , index_dict
    
    @staticmethod
    def getString(graph: Graph = None) -> str:
        """ @param get_result is the returned value of the function get of the AdjMatrix class. 
            @returns a string representing the Adjacency matrix
        """
        matrix, res = AdjMatrix.get(graph)

        out_str = "\nThe Adjacency matrix:\n\t" #\t in order to skip slot at [0][0]
        vertices = list(res.keys())
        # first row indicating vertices
        for i in range(len(vertices)):
            out_str += str(vertices[i]) +"\t"
        out_str += "\n"
        #lines 1 to n-1, where n is the number of vertices
        dim = len(matrix)
        for i in range(dim):
            out_str += str(vertices[i]) +"\t" #first element of each row is a vertice name
            for j in range(dim):
                out_str += f"{matrix[i][j]}\t"  
            out_str += "\n"
        return out_str

class Dijkstra(Graph):

    #PRIVATE -  not part of API
    def __dijkstraRec(g: Graph, init, end, debug, itr):
        """ 
            *Inner Function for Private use.
            @param g : object of Type Graph.
            @param init: Id of first Vertice in path.
            @param end: Id of Last VBertice in path.
            @param debug: Turn on/off prints.
            @param itr: indicates the current recursive call, can be seen in debug mode.
            Calculates minimal distances over graph @g.
        """
        unvisited = g.getUnvisited(init)
        for vId in unvisited:
            acc_distance = g.getDistance(init) + g.getWeight(init, vId)
            if acc_distance < g.getDistance(vId):
                g.setDistance(vId, acc_distance)
        #---- for debugging ---------------------------------------------
        if debug:
            print("\n",5*"- ",f"iteration {itr}",5*"- ",f"\ninitId: {init}, distance: {g.getDistance(init)}, neighboors: {g.getAdj(init)}\n",g)
            for v in unvisited:
                print(f"updated distance for {v} is {g.getDistance(v)}")
        #----------------------------------------------------------------
        g.visit(init)
        for v in unvisited:
            if v != end:
                Dijkstra.__dijkstraRec(g, v, end, debug, itr +1)        

    @staticmethod
    def run(g: Graph, init, end, debug = False):
        """
            @param g : object of Type Graph.
            @param init: Id of first Vertice in path.
            @param end: Id of Last VBertice in path.
            @param debug: Turn on/off prints.
            @Returns the minimal distance from @init to @end, if no path was found, returns math.inf.     
        """
        g._dijkstra_Init(init)
        Dijkstra.__dijkstraRec(g, init, end, debug, 0)
        if debug: print("\ndijkstra debugger ended.\n",20*"- ")
        return g.getDistance(end)

from QueueModule import Queue
from Vertice import Color
import math
class BFS(Graph):
    
    __graph = None
    __start = None

    @staticmethod
    def run(g: Graph, sId):
        """
            BFS algorithem for graphs.
            @param g: graph
            @param sId: Id of the start node in the algorithem 
        """
        BFS.__graph = g
        BFS.__start = sId
        # --------- Initialize -----------
        vertices = g._getVerticeIds()
        for vId in vertices:
            if vId != sId:
                g.color(vId, Color.white)
                g.setDistance(vId, math.inf)  
            else:
                g.color(sId, Color.gray)
                g.setDistance(sId, 0)
            g.setPredecessor(vId, None)
        #----------------------------------
        q = Queue()
        q.enqueue(sId)
        while not q.isEmpty():
            uId = q.head()
            adjList = g.getAdj(uId)
            for vId in adjList:
                if g.getColor(vId) == Color.white:
                    g.color(vId, Color.gray)
                    g.setDistance(vId, g.getDistance(uId) + g.getWeight(uId, vId))
                    g.setPredecessor(vId, pId=uId)
                    q.enqueue(vId)
            q.dequeue() #uId
            g.color(uId, Color.black)

    @staticmethod
    def path(vId):
        """
            Upon receiveing an Id of a vertive, returns the path from the start veritce
            stated in BFS.run to the given id.
            if no path exists, inf will be returned.
            if a trivial path exists, None is returned.
            Note: BFS.run should be used before this function.
        """
        if BFS.__graph is not None:
            if BFS.__start == vId:
                print(f"Message in BFS.path: Path to from {BFS.__start} to {vId} is trivival;\nNone will be returned.")

            else:
                pId = BFS.__graph.getPredecessor(vId)
                path = [vId] if pId is not None else math.inf
                while pId is not None:
                    path.insert(0, pId)
                    pId = BFS.__graph.getPredecessor(pId)
                return path
        else:
            print(f"ERROR: Message in GraphExtensions: Please run the BFS first!")

DEBUG = False
class Oiler(Graph):

    def __CountOilerRecursive(g : Graph, k, vId, flag):
        sum = 0
        if g.getColor(vId) == Color.black:
            if k == 0 and flag :
                if DEBUG : print(f"Circle Found Upon reaching {vId}")
                return 1
            else:
                return 0
        elif g.getColor(vId) != Color.black and \
            k > 0:
            for wId in g.getAdj(vId):
                temp = 0
                if g.getColor(wId) != Color.white:
                    if DEBUG : print(f"Recursive Call with {k-1} {wId} {flag}")
                    temp += Oiler.__CountOilerRecursive(g, k-1, wId, flag)
                else:
                    if g.getColor(wId) == Color.white:
                        if DEBUG : print(f"{wId} was colored GRAY, Recursive Call with {k-1} {wId} True")
                        g.color(wId, Color.gray)
                        if DEBUG : print(f"Recursive Call with {k-1} {wId} True")
                        temp += Oiler.__CountOilerRecursive(g, k-1, wId, True)
                        if temp == 0:
                            if DEBUG : print(f"{wId} was turned back to WHITE")
                            g.color(wId, Color.white)
                # if black do NOTHING
                sum += temp
        return sum


    @staticmethod
    def CountOiler(g : Graph, k : int):
        sum = 0
        verticeList = g._getVerticeIds()
        # Initialize vertices
        for vId in verticeList:
            g.color(vId, Color.white)
        for vId in verticeList:
            if DEBUG : print(f"Starting search from {vId}, he is now BLACK")
            g.color(vId, Color.black)
            # initialize Gray Vertice if were created in last iteration 
            for wId in verticeList:
                if g.getColor(wId) == Color.gray:
                    g.color(wId, Color.white)
            # iterate trough neigboors
            for wId in g.getAdj(vId):
                temp = 0
                if g.getColor(wId) == Color.gray:
                    if DEBUG : print(f"Recursive Call with {k-1} {wId} False")
                    temp += Oiler.__CountOilerRecursive(g, k-1, wId, False)
                if g.getColor(wId) == Color.white:
                    g.color(wId, Color.gray)
                    if DEBUG : print(f"{wId} was colored GRAY, Recursive Call with {k-1} {wId} True")
                    temp += Oiler.__CountOilerRecursive(g, k-1, wId, True)
                    if temp == 0:
                        if DEBUG : print(f"{wId} was turned back to WHITE")
                        g.color(wId, Color.white)
                # if black do NOTHING
                sum += temp
                if DEBUG : print(f"Current Values of sum is: {sum}")
        return sum


            

