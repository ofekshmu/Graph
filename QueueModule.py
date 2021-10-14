class Queue:
    def __init__(self):
        self.q = []
    
    def push(self, obj):
        self.q.insert(0, obj)

    def pop(self):
        if not self.isEmpty():
            obj  = self.q.pop(-1)
            return obj
        else:
            print(f"message in QueueModule: Pop failed!")
            raise IndexError("Queue is Empty")       
                 
    def isEmpty(self):
        return len(self.q) == 0