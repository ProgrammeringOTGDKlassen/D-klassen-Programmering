import random

class Game():
    def __init__(self):
        self.grid = [[random.randint(1,5) for y in range(0,10)] for x in range(0,10)]
        self.anim = [[0 for y in range(0,10)] for x in range(0,10)]
        print(self.grid)

    def build_grid(self):
        for x in range(0, len(self.grid)):
            for y in range(0, len(self.grid)):
                if self.grid[x][y] == 0:
                    if y < len(self.grid[x])-1:
                        # Flyt kolonnen ned
                        while(self.grid[x][y] == 0):
                            self.grid[x][y:] = self.shift_column(self.grid[x][y:], 1)
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
                    self.grid[x-1][y] = 0
                    self.anim[x-1][y] = 50
                    self.grid[x][y] = 0
                    self.anim[x][y] = 50
                    self.grid[x+1][y] = 0
                    self.anim[x+1][y] = 50
                    #Hvis vi har fjernet brikker, skal pladen fyldes igen
                    self.build_grid()
