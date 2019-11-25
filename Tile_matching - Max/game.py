import random


class Tile:
    def __init__(self):
        self.color = random.randint(1,5)
        self.special = random.randint(1, 1) if random.randint(1, 100) == 1 else None

class Game():
    def __init__(self):
        self.grid = [[Tile() for y in range(0,10)] for x in range(0,10)]
        self.anim = [[0 for y in range(0,10)] for x in range(0,10)]
        self.point = 0
        self.detect_matches()

    def build_grid(self):
        for x in range(0, len(self.grid)):
            for y in range(0, len(self.grid)):
                if self.grid[x][y].color == 0:
                    if y < len(self.grid[x])-1 and not all(self.grid[x][yy].color == 0 for yy in range(y, len(self.grid[x]))):
                        # Flyt kolonnen ned
                        while(self.grid[x][y].color == 0):
                            self.grid[x][y:] = self.shift_column(self.grid[x][y:], 1)
                            self.anim[x][y:] = [50 for i in range(y, len(self.anim[x]))]
                    # Fyld op med nye tiles
                    for fill in range(0,len(self.grid[x])):
                        if self.grid[x][fill].color == 0:
                            self.grid[x][fill].color = random.randint(1,5)

    def shift_column(self, l, n):
        return l[n:] + l[:n]

    def swap_tiles(self, x1,y1,x2,y2):
        #Sørg for, at vi kun kan bytte naboceller.
        if abs(x1 - x2) + abs(y1 - y2) < 2:
            self.grid[x1][y1], self.grid[x2][y2] = self.grid[x2][y2], self.grid[x1][y1]

    def detect_sweeper(self, match_list):
        special = False
        for tile in match_list:
            if tile.special == 1:
                special = True

        return special

    def detect_matches(self):
        for x in range(1, len(self.grid) - 1):
            for y in range(0, len(self.grid)):
                #Detect horizontal match
                if self.grid[x][y].color == self.grid[x-1][y].color and self.grid[x][y].color == self.grid[x+1][y].color:
                    c = self.grid[x][y].color
                    match_list = [
                        self.grid[x-1][y],
                        self.grid[x][y],
                        self.grid[x+1][y],
                    ]
                    x1 = x + 2
                    multiplier = 1
                    while x1 < len(self.grid) and self.grid[x1][y].color == c:
                        match_list.append(self.grid[x1][y])
                        x1 += 1

                    if not self.detect_sweeper(match_list):
                        self.grid[x - 1][y].color = 0
                        self.grid[x][y].color = 0
                        self.grid[x + 1][y].color = 0
                        x1 = x + 2
                        while x1 < len(self.grid) and self.grid[x1][y].color == c:
                            self.grid[x1][y].color = 0
                            x1 += 1
                            multiplier += 1
                    else:
                        for i in range(0, 10):
                            self.grid[i][y].color = 0
                            multiplier += 2
                            
                    self.point = self.point + 10*multiplier
                    self.build_grid()
        for y in range(1, len(self.grid) - 1):
            for x in range(0, len(self.grid)):
                #Detect vertical match
                if self.grid[x][y].color == self.grid[x][y-1].color and self.grid[x][y].color == self.grid[x][y+1].color:
                    c = self.grid[x][y].color
                    match_list = [
                        self.grid[x][y-1],
                        self.grid[x][y],
                        self.grid[x][y+1],
                    ]
                    y1 = y + 2
                    multiplier = 1
                    while y1 < len(self.grid) and self.grid[x][y1].color == c:
                        match_list.append(self.grid[x][y1])
                        y1 += 1
                    if not self.detect_sweeper(match_list):
                        self.grid[x][y - 1].color = 0
                        self.grid[x][y].color = 0
                        self.grid[x][y + 1].color = 0
                        y1 = y + 2
                        while y1 < len(self.grid) and self.grid[x][y1].color == c:
                            self.grid[x][y1].color = 0
                            y1 += 1
                            multiplier += 1
                    else:
                        for i in range(0, 10):
                            self.grid[x][i].color = 0
                            multiplier += 2
                    #Hvis vi har fjernet brikker, skal pladen fyldes igen
                    self.point = self.point + 10*multiplier
                    self.build_grid()

        

