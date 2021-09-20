import math

class V:
    def __init__(self, id, distance: int = math.inf, visited = False):
        self.id = id
        self.visited = visited
        self.distance = distance
        self.neighboors = []

    def visit(self):
        self.visited = True
    
    def isVisited(self):
        return self.visited

    def setDistnace(self, d: int, acc = False):
        if acc:
            self.distance += d
        else:
            self.distance = d
    
    def getDistance(self):
        return self.distance

    def getId(self):
        return self.id

    def __eq__(self, other): #TODO: might invoke a problem. checks only per id.
        return self.id == other.id

    def __repr__(self):
        return f"'{self.id}'"