from GraphModule import Graph
#from GraphExtensions import Path

def test_session_one():
    g = Graph(vertices=[1,2,3,4,5], edges=[(1,2),(2,3),(5,4),(4,3)],directed=True,debug=True)
    assert g.exists(1) and g.exists(2) and g.exists(3) and g.exists(4) and g.exists(5)
    assert g.exists((1,2)) and g.exists((2,3)) and g.exists((5,4)) and g.exists((4,3))
    assert not g.exists(6) and not g.exists((3,2))
    print(g)
    assert g.addEdge(1,4) # non existing
    assert g.addEdge(3,5)
    assert g.addEdge(1,2) # existing
    assert g.addEdge(4,3)
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
test_session_one()