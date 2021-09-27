from SimpleGraphModule import Graph
from GraphExtensions import AdjMatrix

def testGraph():
    g = Graph(debug=True)
    g.addVertice(1)
    g.addVertice(2)
    assert g.exists((1,2)) == False
    g.addEdge((1,2))
    assert g.exists(1) == True
    assert g.exists(2) ==  True
    assert g.exists((1,2)) == True
    g.addVertice("ofek")
    assert g.getNeighboors(1) == [2]
    assert g.getNeighboors(2) == [1]
    assert g.getVertices() == [1,2,"ofek"]
    assert g.exists("ofek") == True
    assert g.exists(1) and g.exists(2) and g.exists("ofek") and not g.exists(3)
    g.addEdge((3,2),force=True)
    assert g.exists((3,2)) == True
    assert g.exists((2,3)) == True
    assert g.exists(3) == True
    assert g.exists((1,2)) == True
    assert g.exists((2,1)) == True
    print(g)
    assert g.addEdge((1,"afek")) == False
    assert g.exists((1,"ofek")) == False
    g.addEdge((1,"afek"),force=True)
    assert g.exists((1,"afek"))
    assert g.exists(("afek",1))
    assert g.exists("afek")
    g.addEdge((1,1))
    assert g.exists((1,1)) == False
    print(g.getEdges())

def testDirected():
    g = Graph(debug=True,directed=True)
    g.addEdge((1,1))
    assert g.exists((1,1)) == False
    g.addEdge((1,2))
    assert g.exists((1,2)) == False
    assert g.exists((2,1)) == False
    g.addEdge((2,1))
    assert g.addEdge((1,1),force=True) == False
    assert g.addEdge((1,2),force=True) == True
    assert g.exists((1,2)) == True
    assert g.exists((2,1)) == False
    assert g.addEdge((2,1)) == True
    assert g.addEdge((2,1),force=True) == False
    assert g.exists((2,1)) == True
    assert g.getNeighboors(1) == [2]
    assert g.addVertice(1) == False
    assert g.addVertice(3) == True
    assert g.addVertice("four") == True
    assert g.addEdge(("four","five")) == False
    assert g.addEdge(("four","five"),force=True) == True
    assert g.addEdge(("four","five"),force=True) == False
    assert g.addEdge((1,3)) == True
    assert g.addEdge((1,"four")) == True
    assert g.getNeighboors(1) == [2,3,"four"]
    assert g.getNeighboors(2) == [1]

    g2 = Graph(loops=True, directed=True, debug=True)
    assert g2.addEdge((1,2),force=True) == True
    print(g2)
    assert g2.getVertices() == [1,2]
    assert g2.addEdge((1,3),force=True) == True
    assert g2.getVertices() == [1,2,3]
    assert g2.addEdge((1,4),force=True) == True
    assert g2.addEdge((1,"five"),force=True) == True
    assert g2.getNeighboors(1) == [2,3,4,"five"]
    assert g2.getNeighboors(2) == []
    assert g2.addEdge(("five",4),force=True) == True
    assert g2.getNeighboors("five") == [4]
    assert g2.addEdge(("five","five")) == True
    assert g2.exists(("five","five")) == True
    assert g2.getNeighboors("five") == [4,"five"]
    assert g2.getVertices() == [1,2,3,4,"five"]
    assert g2.getVerticesCount() == 5
    assert g2.getEdges() == [(1,2),(1,3),(1,4),(1,"five"),("five",4),("five","five")]
    print(g2.getEdges())

def DONOTRUN_GrapEX():
    g = Graph(vertices=[1,2,3],edges=[(1,2),(1,3),(3,2),(3,3)],directed=True, debug=True)
    print(g)
    mat = AdjMatrix.get(g)
    str = AdjMatrix.getString(mat)
    print(mat[0],"\n",str)

    g2 = Graph(vertices=['a','b','c',3,2,5],edges=[('a',2),(3,2),(3,5),('c','a')])
    print(g2)
    mat = AdjMatrix.get(g2)
    str = AdjMatrix.getString(mat)
    print(mat[0],"\n",str)
    


