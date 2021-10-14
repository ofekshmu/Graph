class Queue:
    def __init__(self):
        self.q = []
    
    def head(self):
        if not self.isEmpty():
            return self.q[-1]
        else:
            print(f"message in QueueModule: head failed!")

    def enqueue(self, obj):
        self.q.insert(0, obj)

    def dequeue(self):
        if not self.isEmpty():
            obj  = self.q.pop(-1)
            return obj
        else:
            print(f"message in QueueModule: Pop failed!")
            raise IndexError("Queue is Empty")       
                 
    def isEmpty(self):
        return len(self.q) == 0