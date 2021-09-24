from GraphModule import Graph
from CompEdge import Edge
from Vertice import V
from GraphExtensions import Path

def testGraphModule():
    g = Graph(vertices=[1,4,2,6,8],edges=[Edge(1,3),
                                        Edge(1,4),
                                        Edge(6,8),
                                        Edge(8,1),
                                        Edge(2,6),
                                        Edge(4,2)],
                                        debug=True)
    print(g)
    assert g.exists(Edge(1,3)) == False
    assert g.exists(Edge(1,4))
    assert g.exists(Edge(4,2))
    assert g.exists(Edge(2,4)) == False
    assert g.popEdge(Edge(1,4))
    assert g.exists(Edge(1,4)) == False
    assert g.popEdge(Edge(1,4)) == False
    e = Edge(8,1)
    assert g.addEdge(e)   
    assert g.exists(e)
    assert g.popEdge(e)
    assert g.exists(e)
    assert g.popEdge(e)
    assert g.exists(e) == False
    print(g)
    assert g.getUnvisited(2) == [V(6)]
    assert g.NeighboorsOf(1) == []
    assert g.NeighboorsOf(2) == [V(6)]

def testShortestPath():
    g = Graph(vertices=[1,2,3,4,5,6,7],
                edges=[Edge(1,4),Edge(1,3),Edge(1,2),
                        Edge(2,3),Edge(2,5),Edge(3,5),
                        Edge(2,6),Edge(5,6),Edge(6,7),Edge(4,7)],
                        directed=False,
                        debug=True)

    assert Path.dijkstra(g,1,7) == 2
    assert g.setWeight(Edge(4,7),10)
    assert Path.dijkstra(g,1,7) == 3
    assert g.popEdge(Edge(4,7))
    assert Path.dijkstra(g,1,7) == 3
    assert g.popEdge(Edge(2,6))
    assert Path.dijkstra(g,1,7) == 4
    assert g.setWeight(Edge(1,2),5)
    assert Path.dijkstra(g,1,7) == 4
    assert g.popEdge(Edge(1,3))
    assert Path.dijkstra(g,1,7) == 8
    assert g.addEdge(Edge(4,7,weight=2))
    assert Path.dijkstra(g,1,7) == 3
    
testShortestPath()