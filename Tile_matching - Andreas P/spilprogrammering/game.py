import random

class Game():
    def __init__(self):
        self.grid = [[random.randint(1,5) for y in range(0,10)] for x in range(0,10)]
        self.anim = [[0 for y in range(0,10)] for x in range(0,10)]
        self.user_press = False
        self.points = 0
        self.detect_matches()

    def build_grid(self):
        #import pdb; pdb.set_trace()
        for x in range(0, len(self.grid)):
            for y in range(0, len(self.grid)):
                if self.grid[x][y] == 0:
                    if y < len(self.grid[x])-1 and not all(self.grid[x][yy] == 0 for yy in range(y, len(self.grid[x]))):
                        # Flyt kolonnen ned
                        while(self.grid[x][y] == 0):
                            self.grid[x][y:] = self.shift_column(self.grid[x][y:], 1)
                            if self.user_press:
                                self.anim[x][y:] = [50 for i in range(y,len(self.anim[x]))]
                    # Fyld op med nye tiles
                    for fill in range(0,len(self.grid[x])):
                        if self.grid[x][fill] == 0:
                            self.grid[x][fill] = random.randint(1,5)


    def shift_column(self, l, n):
        return l[n:] + l[:n]


    def swap_tiles(self, x1,y1,x2,y2):
        #Sørg for, at vi kun kan bytte naboceller.
        if abs(x1-x2) <= 1 and abs(y1-y2) <= 1:
            self.grid[x1][y1], self.grid[x2][y2] = self.grid[x2][y2], self.grid[x1][y1]


    def detect_matches(self):
        for x in range(1, len(self.grid)-1):
            for y in range(0, len(self.grid)):
                #Detect horizontal match
                if self.grid[x][y] == self.grid[x-1][y] and self.grid[x][y] == self.grid[x+1][y]:
                    c = self.grid[x][y]

                    self.grid[x-1][y] = 0
                    self.grid[x][y] = 0
                    self.grid[x+1][y] = 0
                    x1 = x+2
                    while x1 < len(self.grid) and self.grid[x1][y] == c:
                        self.grid[x1][y] = 0
                        x1 += 1
                    self.points += 10
                    #Hvis vi har fjernet brikker, skal pladen fyldes igen
                    self.build_grid()
        for y in range(1, len(self.grid)-1):
            for x in range(0, len(self.grid)):
                #Detect vertical match
                if self.grid[x][y] == self.grid[x][y-1] and self.grid[x][y] == self.grid[x][y+1]:
                    c = self.grid[x][y]

                    self.grid[x][y-1] = 0
                    self.grid[x][y] = 0
                    self.grid[x][y+1] = 0
                    y1 = y+2
                    while y1 < len(self.grid) and self.grid[x][y1] == c:
                        self.grid[x][y1] = 0
                        y1 += 1
                    self.points += 10
                    #Hvis vi har fjernet brikker, skal pladen fyldes igen
                    self.build_grid()
        if not self.user_press:
            self.points = 0
