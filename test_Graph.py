from GraphModule import Graph
#from GraphExtensions import Path

def test_session_one():
    g = Graph(vertices=[1,2,3,4,5], edges=[(1,2),(2,3),(5,4),(4,3)],directed=True,debug=True)
    assert g.exists(1) and g.exists(2) and g.exists(3) and g.exists(4) and g.exists(5)
    assert g.exists((1,2)) and g.exists((2,3)) and g.exists((5,4)) and g.exists((4,3))
    assert not g.exists(6) and not g.exists((3,2))
    print(g)

test_session_one()