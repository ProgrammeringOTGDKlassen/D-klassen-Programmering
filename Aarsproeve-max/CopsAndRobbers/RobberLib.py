class Robber:
    pos = None
    speed = 0
    col = None
    
    def __init__(self, x, y):
        self.pos = PVector(x,y)
        self.speed = 1
        self.col = color(255,33,33)