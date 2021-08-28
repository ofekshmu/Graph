class Edge:
    def __init__(self, s, e):
        self.start = s
        self.end = e
        self.weight = 0
        self.direction = False

    def setWeight(self, w : int):
        self.weight = 0

    def __repr__(self):
        return f"({self.start})--({self.end})"