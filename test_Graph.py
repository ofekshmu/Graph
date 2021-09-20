from GraphModule import Graph
from Edge import Edge
from Vertice import V

def testGraphModule():
    g = Graph(vertices=[1,4,2,6,8],edges=[Edge(1,3),
                                        Edge(1,4),
                                        Edge(6,8),
                                        Edge(8,1),
                                        Edge(2,6),
                                        Edge(4,2)])
    assert g.exists(Edge(1,3))
    assert g.exists(Edge(1,4))
    assert g.exists(Edge(4,2))
    print(g.getRaw())
    print(g)
    assert g.exists(Edge(2,4)) == False
    assert g.pop(Edge(1,4))
    assert g.exists(Edge(1,4)) == False
    assert g.pop(Edge(1,4)) == False
    e = Edge(8,1)
    assert g.addEdge(e)   
    assert g.exists(e)
    assert g.popEdge(e) and g.popEdge(e)
    assert g.exists(e)
    assert g.getUnvisited() == [V(1),V(4),V(2),V(6),V(8)]
    assert g.NeighboorsOf(V(1)) == [V(3)]

#def testShortestPath():
#    NotImplemented()