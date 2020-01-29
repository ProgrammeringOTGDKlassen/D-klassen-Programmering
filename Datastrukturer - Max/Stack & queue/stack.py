class Stack():

    def __init__(self):
        self.l = [0 for i in range(0,10)]
        self.top = -1

    def push(self, x):
        self.top += 1
        self.l[self.top] = x

    def pop(self):
        if self.stack_empty():
            raise(Exception("Underflow"))
        else:
            self.top -= 1
        return self.l[self.top + 1]

    def stack_empty(self):
        if self.top == -1:
            r = True
        else:
            r = False
        return r