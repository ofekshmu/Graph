from GraphModule import Graph
import numpy as np
import math

class AdjMatrix(Graph):
    
    @staticmethod
    def get(graph: Graph):
        """@returns an Adjacency matrix and an dictionary representing vertices indexes """
        #variables
        edge_list = graph.getEdges()
        vertices = graph.getVertices()
        dim = graph.getVerticesCount()
        matrix = np.zeros((dim,dim),dtype=np.int32)
        #dictionary to hold indexes for each vertices in matrix
        index_dict = {vertices[i]: i for i in range(dim)}
        #fill matrix
        for e in edge_list:
            row = index_dict[e.start]
            col = index_dict[e.end]
            matrix[row][col] = 1
            if not e.isDirected(): # undirected edges will be added both directions
                matrix[col][row] = 1
        return (matrix, index_dict)
    
    @staticmethod
    def getString(get_result: tuple) -> str:
        """ @param get_result is the returned value of the function get of the AdjMatrix class. 
            @returns a string representing the Adjacency matrix
        """
        (matrix, res) = get_result
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

    @staticmethod
    def Dijkstra(graph: Graph, init, end) -> list:
        vertices = graph.getVertices()
        dict = {vertices[i]:v(name=vertices[i],distance=math.inf,visited=False) for i in range(len(vertices))}
        current = dict[init]
        current.setDistnace(0)
        current.visit()

        #for
        neig = graph.getNeighboors(current)
        unvisited = [neig[i] if dict[neig[i]].isVisited() else None for i in range(len(neig))]
        print(unvisited,"\n", "check that ther is no none value")
        for n in unvisited:
            n.setDistance(current.getDistance(),acc=True)
            if n.getDistance()


class v:
    def __init__(self, name, distance: int = math.inf, visited = False):
        self.name = name
        self.visited = visited
        self.distance = distance

    def visit(self):
        self.visited = True
    
    def isVisited(self):
        return self.visited

    def setDistnace(self, d: int, acc = False):
        if acc:
            self.distance += d
        else:
            self.distance = d
    
    def getDistance(self):
        return self.distance

    def getName(self):
        return self.name