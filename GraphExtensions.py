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

class Path(Graph):

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
                Path.__dijkstraRec(g, v, end, debug, itr +1)        

    @staticmethod
    def dijkstra(g: Graph, init, end, debug = False):
        """
            @param g : object of Type Graph.
            @param init: Id of first Vertice in path.
            @param end: Id of Last VBertice in path.
            @param debug: Turn on/off prints.
            @Returns the minimal distance from @init to @end, if no path was found, returns math.inf.     
        """
        g._dijkstra_Init(init)
        Path.__dijkstraRec(g, init, end, debug, 0)
        if debug: print("\ndijkstra debugger ended.\n",20*"- ")
        return g.getDistance(end)

from QueueModule import Queue
from Vertice import Color
import math
class BFS(Graph):
    
    __graph = None

    @staticmethod
    def run(g: Graph, sId):
        BFS.__graph = g
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
        if BFS.__graph is not None:
            path = [vId]
            pId = BFS.__graph.getPredecessor(vId)
            while pId is not None:
                path.insert(0, pId)
                pId = BFS.__graph.getPredecessor(pId)
            return path
        else:
            print(f"ERROR: Message in GraphExtensions: Please run the BFS first!")

        


            

