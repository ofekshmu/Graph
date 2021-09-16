from GraphModule import Graph
from DirectedGraphModule import DirectedGraph
import numpy as np

class GraphEx(DirectedGraph):
    def __init__(self, g: DirectedGraph):
        self.graph = g
        self.matrix = []

    def getShortestPath():
        shortestPath = []
        return shortestPath
    
    def _BFS():
        pass

    def _DFS():
        pass

    def getAdjMat(self):
        edge_list = self.graph.getEdges()
        vertices = self.graph.getVertices()
        dim = self.graph.getVerticesCount()
        self.matrix = np.zeros((dim,dim),dtype=np.int32)
        self.indexs = {vertices[i]: i for i in range(dim)}
        for e in edge_list:
            row = self.indexs[e.start]
            col = self.indexs[e.end]
            self.matrix[row][col] = 1
            if not e.isDirected():
                self.matrix[col][row] = 1
        return self.matrix

    def getAdjMatStr(self) -> str:
        self.getAdjMat()
        string = "\nThe Adjacency matrix:\n\t"
        vertices = self.graph.getVertices()
        for i in range(len(vertices)):
            string += str(vertices[i]) +"\t"
        string += "\n"
        dim = len(self.matrix)
        for i in range(dim):
            string += str(vertices[i]) +"\t"
            for j in range(dim):
                string += f"{self.matrix[i][j]}\t"  
            string += "\n"
        return string

