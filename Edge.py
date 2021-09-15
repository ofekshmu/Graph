class Edge:
    def __init__(self, s, e,weight: int = 0):
        self.start = s
        self.end = e
        self.weight = weight
        self.direction = False

    def Directed(self):
        self.direction = True
        return self
        
    def _setWeight(self, w : int):
        self.weight = 0

    def flippedInstance(self):
        return Edge(self.end,self.start)

    def isLoop(self):
        return self.start == self.end

    def __eq__(self,other):
        cond1 = self.start == other.start 
        cond2 = self.end == other.end
        cond3 = self.weight == other.weight
        cond4 = self.direction == other.direction
        return cond1 and cond2 and cond3 and cond4

    def __repr__(self):
        connector = "-->" if self.direction else "--"
        return f"({self.start}){connector}({self.end})"