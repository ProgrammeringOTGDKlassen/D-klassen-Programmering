class Queue():

    def __init__(self):
        self.l = [0 for i in range(0,10)]
        self.head = 0
        self.tail = -1

    def enqueue(self, x):
        if self.tail >= len(self.l)-1:
            raise(Exception("The queue is full, you can't enqueue! (Overflow)"))
        self.l[self.tail + 1] = x
        if self.tail == len(self.l):
            self.tail = 0
        else:
            self.tail = self.tail + 1
    
    def dequeue(self):
        if self.head >= len(self.l)-1:
            raise(Exception("The queue is empty, you can't dequeue! (Underflow)"))
        x = self.l[self.head]
        if self.head == len(self.l):
            self.head = 0
        else:
            self.head = self.head + 1
        return x
    
    def queue_full(self):
        if self.tail > self.head:
            return self.tail - self.head + 1 == self.len(self.l)
        else:
            return self.tail - self.head + 1 == 0
        
    def queue_empty(self):
        pass