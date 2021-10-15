from GraphExtensions import AdjMatrix, Dijkstra
from GraphModule import Graph
import math

def test_session_one():
    g = Graph(vertices=[1,2,3,4,5], edges=[(1,2),(2,3),(5,4),(4,3)],directed=True,debug=True)
    assert g.exists(1) and g.exists(2) and g.exists(3) and g.exists(4) and g.exists(5)
    assert g.exists((1,2)) and g.exists((2,3)) and g.exists((5,4)) and g.exists((4,3))
    assert not g.exists(6) and not g.exists((3,2))
    print(g)
    assert g.addEdge(1,4) # non existing
    assert g.addEdge(3,5)
    assert not g.addEdge(1,2) # existing
    assert not g.addEdge(4,3)
    assert not g.addEdge(5,7)  # not valid
    assert not g.addEdge(9,6)
    assert g.addVertice(6) # valid
    assert g.addVertice(7)
    assert not g.addVertice(5) #invalid
    assert not g.addVertice(6)
    assert g.exists((1,4)) and g.exists(6)
    assert g.forceEdge(8,9) #force both
    assert g.forceEdge(10,11)
    assert g.forceEdge(10,12) # force one
    assert not g.forceEdge(1,2) #exists
    print(g)
    assert g.popEdge((1,2))
    assert g.popEdge((8,9))
    assert not g.popEdge((11,10)) # invalid
    assert not g.popEdge((20,21))
    assert not g.popEdge((6,7))
    print(g)

def test_session_two():
    g = Graph(vertices=[1,2,3],edges=[(1,2),(2,3)],directed=True,debug=True)
    print(g)
    print(g.getUnvisited()) # 1,2,3
    print(g.getUnvisited(1)) # 2
    print(g.getUnvisited(3)) # empty
    assert g.isAdj(1,2) and g.isAdj(2,3)
    assert not g.isAdj(1,4) # non existing vertice
    assert not g.isAdj(2,1) # opposite direction 
    assert not g.isAdj(5,6) # both non existing

def test_adjMatrix():
    g = Graph(vertices=[1,2,3,4,5],edges=[(1,2),(1,3),(4,5),(2,3)],directed=True,debug=True)
    print(AdjMatrix.get(g)[0])
    print(AdjMatrix.getString(g))

def test_dijkstra():
    g = Graph(vertices=[1,2,3,4,5],edges=[(1,2),(1,3),(4,5),(2,3),(3,4)],directed=True,debug=True)
    print(g)
    assert Dijkstra.run(g,1,4,debug=False) == 2
    assert Dijkstra.run(g,4,1) == math.inf
    assert g.popEdge((1,3))
    assert Dijkstra.run(g,1,4) == 3
    assert g.popEdge((2,3))
    assert Dijkstra.run(g,1,4) == math.inf
    assert Dijkstra.run(g,2,5) == math.inf
    assert Dijkstra.run(g,3,5) == 2
    print(g)

from GraphExtensions import BFS

def test_bfs():
    g = Graph(vertices=[1,2,3,4,5],edges=[(1,2),(1,3),(4,5),(2,3),(3,4)],directed=True,debug=True)
    print(g)
    BFS.path(1)
    BFS.run(g, 1)
    for vId in g._getVerticeIds():
        print(f"Path to {vId} is: ",BFS.path(vId))
    BFS.run(g, 2)
    for vId in g._getVerticeIds():
        print(f"Path to {vId} is: ",BFS.path(vId))
    try:
        print(BFS.path(10))
    except KeyError:
        print("Cought Error.")
    #bug at path to 1 when starting from 2, lok into it