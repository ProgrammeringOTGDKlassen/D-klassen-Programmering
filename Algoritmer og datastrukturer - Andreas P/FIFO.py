class Que:
    def __init__(self):
        self.max = 10
        self.l = [0 for i in range(0, self.max)]
        self.tail = 0
        self.head = 0

    def enqueue(self, x):
        if self.tail == self.head -1:
            self.expand()
        self.l[self.tail] = x
        if self.tail == len(self.l) -1:
            self.tail = 0
        else:
            self.tail = self.tail + 1

    def dequeue(self):
        if self.head >= len(self.l) -1:
            raise(Exception("The que is empty, you can't deque!"))
        x = self.l[self.head]
        self.l[self.head] = None
        if self.head == len(self.l) -1:
            self.head = 0
        else:
            self.head = self.head + 1
        return x

    def expand(self):
        self.max *= 2
        n = [0 for i in range(0, self.max)]
        for index, item in enumerate(self.l):
            n[index] = item
        self.l = n

