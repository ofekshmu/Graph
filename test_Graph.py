from GraphModule import Graph
from DirectedGraphModule import DirectedGraph
from GraphExtensions import GraphEx
from Edge import Edge

def testGraph():
    g = Graph(debug=True)
    g.addVertice(1)
    g.addVertice(2)
    assert g.exists(Edge(1,2)) == False
    g.addEdge(Edge(1,2))
    assert g.exists(1) == True
    assert g.exists(2) ==  True
    assert g.exists(Edge(1,2)) == True
    g.addVertice("ofek")
    assert g.getNeighboors(1) == [2]
    assert g.getNeighboors(2) == [1]
    assert g.getVertices() == [1,2,"ofek"]
    assert g.exists("ofek") == True
    assert g.exists(1) and g.exists(2) and g.exists("ofek") and not g.exists(3)
    g.addEdge(Edge(3,2),force=True)
    assert g.exists(Edge(3,2)) == True
    assert g.exists(Edge(2,3)) == True
    assert g.exists(3) == True
    assert g.exists(Edge(1,2)) == True
    assert g.exists(Edge(2,1)) == True
    print(g)
    assert g.addEdge(Edge(1,"afek")) == False
    assert g.exists(Edge(1,"ofek")) == False
    g.addEdge(Edge(1,"afek"),force=True)
    assert g.exists(Edge(1,"afek"))
    assert g.exists(Edge("afek",1))
    assert g.exists("afek")
    g.addEdge(Edge(1,1))
    assert g.exists(Edge(1,1)) == False
    print(g.getEdges())

def testDirected():
    g = DirectedGraph(debug=True)
    g.addEdge(Edge(1,1))
    assert g.exists(Edge(1,1)) == False
    g.addEdge(Edge(1,2))
    assert g.exists(Edge(1,2)) == False
    assert g.exists(Edge(2,1)) == False
    g.addEdge(Edge(2,1))
    assert g.addEdge(Edge(1,1),force=True) == False
    assert g.addEdge(Edge(1,2),force=True) == True
    assert g.exists(Edge(1,2)) == True
    assert g.exists(Edge(2,1)) == False
    assert g.addEdge(Edge(2,1)) == True
    assert g.addEdge(Edge(2,1),force=True) == False
    assert g.exists(Edge(2,1)) == True
    assert g.getNeighboors(1) == [2]
    assert g.addVertice(1) == False
    assert g.addVertice(3) == True
    assert g.addVertice("four") == True
    assert g.addEdge(Edge("four","five")) == False
    assert g.addEdge(Edge("four","five"),force=True) == True
    assert g.addEdge(Edge("four","five"),force=True) == False
    assert g.addEdge(Edge(1,3)) == True
    assert g.addEdge(Edge(1,"four")) == True
    assert g.getNeighboors(1) == [2,3,"four"]
    assert g.getNeighboors(2) == [1]

    g2 = DirectedGraph(loops=True,debug=True)
    assert g2.addEdge(Edge(1,2),force=True) == True
    print(g2)
    assert g2.getVertices() == [1,2]
    assert g2.addEdge(Edge(1,3),force=True) == True
    assert g2.getVertices() == [1,2,3]
    assert g2.addEdge(Edge(1,4),force=True) == True
    assert g2.addEdge(Edge(1,"five"),force=True) == True
    assert g2.getNeighboors(1) == [2,3,4,"five"]
    assert g2.getNeighboors(2) == []
    assert g2.addEdge(Edge("five",4),force=True) == True
    assert g2.getNeighboors("five") == [4]
    assert g2.addEdge(Edge("five","five")) == True
    assert g2.exists(Edge("five","five")) == True
    assert g2.getNeighboors("five") == [4,"five"]
    assert g2.getVertices() == [1,2,3,4,"five"]
    assert g2.getVerticesCount() == 5
    assert g2.getEdges() == [Edge(1,2).setAsDirected(),
                            Edge(1,3).setAsDirected(),
                            Edge(1,4).setAsDirected(),
                            Edge(1,"five").setAsDirected(),
                            Edge("five",4).setAsDirected(),
                            Edge("five","five").setAsDirected()]
    print(g2.getEdges())

def test_edges():
    assert Edge(1,2) == Edge(1,2)
    assert type(Edge(2,1).setAsDirected()) == type(Edge(2,1))
    assert Edge(2,1).setAsDirected() != Edge(2,1)
    assert Edge(1,2) == Edge(2,1)

def test_GrapEX():
    g = DirectedGraph(vertices=[1,2,3],edges=[Edge(1,2),Edge(1,3),Edge(3,2),Edge(3,3)],debug=True)
    print(g)
    ge = GraphEx(g)
    print(ge.genMatrix())
    print(ge.genMatrixStr())
    


