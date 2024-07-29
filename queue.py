class Queue:

    def __init__(self):
        self.queue = []
        self.indexavailabe = 0
 
    def inqueue(self,item):
        self.queue[self.indexavailabe] = item
        self.indexavailabe +=1
    def dequeue (self):
        m = self.queue[0]
        del self.queue[0]
        self.indexavailabe -= 1
        return m
