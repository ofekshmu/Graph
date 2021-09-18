from SimpleGraphModule import Graph
import numpy as np

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

