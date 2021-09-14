class Edge:
    def __init__(self, s, e,weight: int = 0, direction :bool = False):
        self.start = s
        self.end = e
        self.direction = direction
        self.weight = weight
        self.direction = False

    def Directed(self):
        self.direction = True
        return self
        
    def setWeight(self, w : int):
        self.weight = 0

    def flippedInstance(self):
        return Edge(self.end,self.start)

    def isLoop(self):
        return self.start == self.end

    def __repr__(self):
        connector = "-->" if self.direction else "--"
        return f"({self.start}){connector}({self.end})"