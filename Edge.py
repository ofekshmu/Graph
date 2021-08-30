class Edge:
    def __init__(self, s, e,weight: int = 0, direction :bool = False):
        self.start = s
        self.end = e
        self.direction = direction
        self.weight = weight
        self.direction = False

    def setWeight(self, w : int):
        self.weight = 0

    def _isDir(self):
        return self.direction
    
    def _flip(self):
        if self.direction:
            print("\tWarning!!!\nFlipping an Edge with direction!")
        temp = self.start
        self.start = self.end
        self.end = temp

    def __repr__(self):
        connector = "-->" if self.direction else "--"
        return f"({self.start}){connector}({self.end})"