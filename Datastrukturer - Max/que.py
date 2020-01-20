class Queue():

    def __init__(self):
        self.l = [0 for i in range(0,10)]
        self.head = 0
        self.tail = -1
        self.h = 0

    def enqueue(self, x):
        if self.tail >= len(self.l)-1:
            raise(Exception("The queue is full, you can't enqueue! (Overflow)"))
        self.l[self.tail + 1] = x
        self.h += 1
        if self.tail == len(self.l):
            self.tail = 0
        else:
            self.tail = self.tail + 1
    
    def dequeue(self):
        if self.head >= len(self.l)-1:
            raise(Exception("The queue is empty, you can't dequeue! (Underflow)"))
        x = self.l[self.head]
        self.h -= 1
        if self.head == len(self.l):
            self.head = 0
        else:
            self.head = self.head + 1
        return x
    
    