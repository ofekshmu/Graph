import Graph
import Edge
def testGraph():
    g = Graph.Graph()
    g.addVertice(1)
    g.addVertice(2)
    assert g.exists(Edge.Edge(1,2)) == False
    g.addEdge(Edge.Edge(1,2))
    assert g.exists(1) == True
    assert g.exists(2) ==  True
    assert g.exists(Edge.Edge(1,2)) == True
    g.addVertice("ofek")
    assert g.exists("ofek") == True
    assert g.exists(1) and g.exists(2) and g.exists("ofek") and not g.exists(3)
    g.addEdge(Edge.Edge(3,2),force=True)
    assert g.exists(Edge.Edge(3,2)) == True
    assert g.exists(Edge.Edge(2,3)) == True
    assert g.exists(3) == True