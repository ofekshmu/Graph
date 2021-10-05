from GraphModule import Graph
import numpy as np
import math

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

        
    def __init__(self):
        pass

    def _dijkstraRec(self, g: Graph, init, end):
        #---- for debugging --------
        print(f"init: {init}, distance: {g.getDistanceV(init)}, neighboors: {g.NeighboorsOf(init)}")
        print(g)
        # --------------------------
        unvisited = g.getUnvisited(init)
        for v in unvisited:
            acc_distance = g.getDistanceV(init) + g.getWeight(Edge(init,v.getId()))
            if acc_distance < g.getDistanceV(v.getId()):
                g.setDistanceV(v.getId(), acc_distance)
        #---- for debugging --------
        for v in unvisited:
            print(f"current distance for {v} is {v.getDistance()}")
        g.visit(init)
        for v in unvisited:
            if v.getId() != end:
                self._dijkstraRec(g, v.getId(), end)        


    def dijkstra(self, g: Graph, init, end) -> list:
        g.dijkstra_Init(init)
        self._dijkstraRec(g, init, end)
        return g.getDistanceV(end)

            

