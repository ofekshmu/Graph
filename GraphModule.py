class v:
    def __init__(self, name, distance: int = math.inf, visited = False):
        self.name = name
        self.visited = visited
        self.distance = distance

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

    def getName(self):
        return self.name