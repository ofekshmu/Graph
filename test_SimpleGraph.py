from SimpleGraphModule import Graph
from GraphExtensions import AdjMatrix

"""
Run tests in module:
    $ pytest *module_Name*.py
Run tests in a directory:
    $ pytest *directory*/
To run a spesific test:
    $ pytest *test_mod*.py::*test_func*
Run tests by keyword expressions:
    $ pytest -k "*Key words*"
"""

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
    g.forceEdge((3,2))
    assert g.exists((3,2)) == True
    assert g.exists((2,3)) == True
    assert g.exists(3) == True
    assert g.exists((1,2)) == True
    assert g.exists((2,1)) == True
    print(g)
    assert g.addEdge((1,"afek")) == False
    assert g.exists((1,"ofek")) == False
    g.forceEdge((1,"afek"))
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
    assert g.forceEdge((1,1)) == False
    assert g.forceEdge((1,2))
    assert g.exists((1,2)) == True
    assert g.exists((2,1)) == False
    assert g.addEdge((2,1)) == True
    assert g.forceEdge((2,1)) == False
    assert g.exists((2,1)) == True
    assert g.getNeighboors(1) == [2]
    assert g.addVertice(1) == False
    assert g.addVertice(3) == True
    assert g.addVertice("four") == True
    assert g.addEdge(("four","five")) == False
    assert g.forceEdge(("four","five")) == True
    assert g.forceEdge(("four","five")) == False
    assert g.addEdge((1,3)) == True
    assert g.addEdge((1,"four")) == True
    assert g.getNeighboors(1) == [2,3,"four"]
    assert g.getNeighboors(2) == [1]

    g2 = Graph(loops=True, directed=True, debug=True)
    assert g2.forceEdge((1,2)) == True
    print(g2)
    assert g2.getVertices() == [1,2]
    assert g2.forceEdge((1,3)) == True
    assert g2.getVertices() == [1,2,3]
    assert g2.forceEdge((1,4)) == True
    assert g2.forceEdge((1,"five")) == True
    assert g2.getNeighboors(1) == [2,3,4,"five"]
    assert g2.getNeighboors(2) == []
    assert g2.forceEdge(("five",4)) == True
    assert g2.getNeighboors("five") == [4]
    assert g2.addEdge(("five","five")) == True
    assert g2.exists(("five","five")) == True
    assert g2.getNeighboors("five") == [4,"five"]
    assert g2.getVertices() == [1,2,3,4,"five"]
    assert g2.getEdges() == [(1,2),(1,3),(1,4),(1,"five"),("five",4),("five","five")]
    print(g2.getEdges())

def test_GrapEX():
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

def test_raiseError():
    g = Graph(vertices=[1,2,3])
    try:   
        assert g.getNeighboors(4) == []
        print("\nError was not raised")
    except RuntimeWarning:
        print("\nError seccssecfuly catched")

def testSimpleGraph():
    g = Graph(vertices=[1,2,3,4,5,6,7,8], edges=[(1,2),(2,3),(3,4),(6,7),(8,9),(8,1),(7,6),(5,4)],
    directed=True,duplicates=False,loops=False,debug=True)
    assert g.exists((1,2))
    assert g.exists((8,9)) == False
    assert g.isNeighboors(1,2)
    assert g.isNeighboors(2,1) == False
    assert g.isNeighboors(5,6) == False
    assert g.isNeighboors(6,5) == False
    assert g.exists(5) and g.exists(8)
    assert g.exists(9) == False
    assert g.exists(10) == False
    assert g.forceEdge((1,9))
    #except message
    assert g.exists((1,9)) and g.exists(9)
    assert g.exists((9,1)) == False
    assert g.addEdge((9,10)) == False
    assert g.addEdge((9,9)) == False
    assert g.addEdge((1,2)) == False
    assert g.addEdge((2,4)) == True



