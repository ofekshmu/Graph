from GraphModule import Graph
from Edge import Edge

class DirectedGraph(Graph):
    def __init__(self, 
                    vertices : list = [],
                    edges : list = [], 
                    # Graph Settings
                    duplicates :bool = False, 
                    loops : bool = False,
                    debug : bool = False):

        super().__init__(vertices=vertices,edges=edges,duplicates=duplicates,loops=loops,debug=debug)

    def addEdge(self, e : Edge, force : bool = False):
        """doc"""
        valid = self._ValidInsertion(e, force)
        if valid:
            self.graph[e.start].append(e.end)
            self.edgeList.append(e.setAsDirected())
        return valid