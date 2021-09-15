class Edge:
    def __init__(self, s, e,weight: int = 0):
        self.start = s
        self.end = e
        self.weight = weight
        self.direction = False

    def setAsDirected(self):
        self.direction = True
        return self
    
    def isDirected(self):
        return self.direction

    def _setWeight(self, w : int):
        self.weight = 0

    def flippedInstance(self):
        return Edge(self.end,self.start)

    def isLoop(self):
        return self.start == self.end

    def __eq__(self,other):
        cond1 = self.weight == other.weight
        cond2 = self.direction == other.direction
        cond3 = self.direction == other.direction
        values_Cond = self.start == other.start and self.end == other.end
        if not self.direction:
            values_Cond = values_Cond or self.start == other.end and self.end == other.start 
        print(cond1,cond2,cond3,self.direction,values_Cond) 
        return cond1 and cond2 and cond3 and values_Cond

    def __repr__(self):
        connector = "-->" if self.direction else "--"
        return f"({self.start}){connector}({self.end})"