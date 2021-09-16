from GraphModule import Graph
from DirectedGraphModule import DirectedGraph
import numpy as np

class GraphEx(DirectedGraph):
    def __init__(self, g: DirectedGraph):
        self.graph = g

    def getShortestPath():
        shortestPath = []
        return shortestPath
    
    def _BFS():
        pass

    def _DFS():
        pass

    def genMatrix(self):
        edge_list = self.graph.getEdges()
        vertices = self.graph.getVertices()
        dim = self.graph.getVerticesCount() + 1
        matrix = np.zeros((dim,dim), dtype =np.int)
        matrix[1:,0] = vertices ; self.matrix[0,1:] = vertices
        res = {vertices[i]: i for i in range(dim - 1)}
        for e in edge_list:
            row = res[e.start]
            col = res[e.end]
            matrix[row][col] = 1
            if not e.isDirected():
                matrix[col][row] = 1
        return matrix
