class Edge:
    def __init__(self, s, e, direction :bool = False):
        self.start = s
        self.end = e
        self.direction = direction
        self.weight = 0
        self.direction = False

    def setWeight(self, w : int):
        self.weight = 0

    def isDir(self):
        return self.direction

    def __repr__(self):
        connector = "-->" if self.direction else "--"
        return f"({self.start}){connector}({self.end})"