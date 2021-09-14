from GraphModule import Graph
from Edge import Edge

class DirectedGraph(Graph):
    def __init__(vertices : list = [],
                    edges : list = [], 
                    # Graph Settings
                    duplicates :bool = False, 
                    loops : bool = False,
                    debug : bool = False):

        super().__init__(vertices, edges, duplicates, loops, debug)

    def addEdge(self, e : Edge , force : bool = False):
        #if(super().addEdge(e,force))
        pass

    def exists():
        pass