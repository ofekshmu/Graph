from Vertice import V

class Edge:
    def __init__(self, startId, endId, weight: int = 1, direction: bool = True):
        self.startId = startId
        self.endId = endId
        self.weight = weight
        self.direction = direction

    def setAsDirected(self):
        self.direction = True
        return self
    
    def isDirected(self):
        return self.direction

    def setWeight(self, w : int):
        self.weight = w

    def getWeight(self):
        return self.weight

    def flippedInstance(self):
        return Edge(startId=self.endId, endId=self.startId)

    def isLoop(self):
        return self.startId == self.endId

    def __eq__(self,other):
        cond2 = self.direction == other.direction
        values_Cond = self.startId == other.startId and self.endId == other.endId
        if not self.direction:
            values_Cond = values_Cond or self.startId == other.endId and self.endId == other.startId 
        return cond2 and values_Cond

    def getStartId(self) -> str:
        return self.startId

    def getEndId(self) -> str:
        return self.endId

    def __repr__(self) -> str:
        connector = "-->" if self.direction else "--"
        return f"({self.startId}){connector}({self.endId})"