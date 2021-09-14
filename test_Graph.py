from GraphModule import Graph
from Edge import Edge

def testGraph():
    g = Graph()
    g.addVertice(1)
    g.addVertice(2)
    assert g.exists(Edge(1,2)) == False
    g.addEdge(Edge(1,2))
    assert g.exists(1) == True
    assert g.exists(2) ==  True
    assert g.exists(Edge(1,2)) == True
    g.addVertice("ofek")
    assert g.exists("ofek") == True
    assert g.exists(1) and g.exists(2) and g.exists("ofek") and not g.exists(3)
    g.addEdge(Edge(3,2),force=True)
    assert g.exists(Edge(3,2)) == True
    assert g.exists(Edge(2,3)) == True
    assert g.exists(3) == True
    assert g.exists(Edge(1,2)) == True
    assert g.exists(Edge(2,1)) == True
    assert g.addEdge(Edge(1,'afek')) == False
    assert g.exists(Edge(1,'ofek')) == False
    g.addEdge(Edge(1,'afek'),force=True)
    assert g.exists(Edge(1,'afek'))
    assert g.exists(Edge('afek',1))
    assert g.exists("afek")

def testDirected():
    g = Graph(directed=True)