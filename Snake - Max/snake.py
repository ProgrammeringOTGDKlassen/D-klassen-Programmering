import math
import random
import pygame
import tkinter as tk
import time
from tkinter import messagebox
rows = 10
width = 500
dis = width // rows
snakeHead = pygame.image.load('images\snakeHead.png')
snakeHead = pygame.transform.scale(snakeHead,(dis,dis))
snackPic = pygame.image.load('images\points.png')
snackPic = pygame.transform.scale(snackPic, (dis,dis))
boostPic = pygame.image.load('images\Boost.png')
boostPic = pygame.transform.scale(boostPic, (dis,dis))

music = ['sounds\y2mate.com - nytrstale_til_dansk_i_2g_g8pnBZHa8Bg.ogg']

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load(music[0])
pygame.mixer.music.set_volume(100)
pygame.mixer.music.play(-1)
class cube(object):
    rows = 10
    w = 500
    def __init__(self,start,img = 'images\snakeHead.png',dirnx=1,dirny=0,color=(255,0,0), isMax = True, isBoost = False, isSnack = False):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color
        dis = self.w // self.rows
        self.giffler = snackPic
        self.max = snakeHead
        self.isMax = isMax
        self.isBoost = isBoost
        self.booster = boostPic
        self.isSnack = isSnack
       
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
 
    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        if self.isMax:
            surface.blit(self.max, (i*dis+1,j*dis+1, dis-2, dis-2))
        elif self.isBoost:
            surface.blit(self.booster, (i*dis+1,j*dis+1, dis-2, dis-2))
        else:
            surface.blit(self.giffler, (i*dis+1,j*dis+1, dis-2, dis-2))
       
 
class snake(object):
    body = []
    turns = {}
    
    def __init__(self, color, pos, speed):
        self.color = color
        self.head = cube(pos, 'images\snakeHead.png')
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
        self.time_to_move = speed
        self.move_speed = speed
 
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
 
            keys = pygame.key.get_pressed()
 
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
 
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
 
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
 
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        self.time_to_move -= 1
        if self.time_to_move <= 0:
            self.time_to_move = self.move_speed
            for i, c in enumerate(self.body):
                p = c.pos[:]
                if p in self.turns:
                    turn = self.turns[p]
                    c.move(turn[0],turn[1])
                    if i == len(self.body)-1:
                        self.turns.pop(p)
                else:
                    if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                    elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0, c.pos[1])
                    elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                    elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows-1)
                    else: c.move(c.dirnx,c.dirny)
       
    def speedup(self):
        self.move_speed = 10
    
    def slowdown(self):
        self.move_speed = self.move_speed+1
        
    def reset(self, pos, speed):
        self.head = cube(pos, 'images\snakeHead.png')
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1
        self.time_to_move = speed
        self.move_speed = speed
 
    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny
 
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1]), 'images\snakeHead.png'))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1]), 'images\snakeHead.png'))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1), 'images\snakeHead.png'))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1), 'images\snakeHead.png'))
 
        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy
       
 
    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i ==0:
                c.draw(surface, True)
            else:
                c.draw(surface)
 
 
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
 
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
 
        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))
       
 
def redrawWindow(surface):
    global rows, width, s, snack, boost
    surface.fill((0,0,0))
    s.draw(surface)
    snack.draw(surface)
    boost.draw(surface)
    drawGrid(width,rows, surface)
    pygame.display.update()
 
 
def randomSnack(rows, item, boost):
    boost = boost
    positions = item.body
    if boost == None:
        while True:
            x = random.randrange(rows)
            y = random.randrange(rows)
            if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
                randomSnack(rows, item, boost)
            else:
                break        
    else:
        while True:
            x = random.randrange(rows)
            y = random.randrange(rows)
            if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0 or boost.pos == (x,y):
                randomSnack(rows, item, boost)
            else:
                break
       
    return (x,y)
 

def randomBoost(rows, item, snack):
    snack = snack
    positions = item.body
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0 or snack.pos == (x,y):
            randomBoost(rows, item, snack)
        else:
            break
       
    return (x,y)
 
def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass
 
 
def main():
    global width, rows, s, snack, boost
    width = 500
    rows = 10
    win = pygame.display.set_mode((width, width))
    speed = 10
    s = snake((255,0,0), (random.randint(0,9),random.randint(0,9)), speed)
    snack = cube(randomSnack(rows, s, None), 'images\snakeHead.png',color=(0,255,0), isMax = False, isSnack = True)
    boost = cube(randomBoost(rows, s, snack), 'images\snakeHead.png',color=(0,255,255),isMax = False, isBoost = True)
    flag = True
 
    clock = pygame.time.Clock()
    while flag:
        clock.tick(100)
        s.move()
        # print(s.body[0].pos)
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s, boost), 'images\snakeHead.png', color=(0,255,0), isMax = False, isSnack = True)
            s.slowdown()
        elif s.body[0].pos == boost.pos:
            boost = cube(randomBoost(rows, s, snack), 'images\snakeHead.png',color=(0,255,255),isMax = False, isBoost = True)
            s.speedup()
 
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                print('Score: ', len(s.body))
                message_box('You Lost!', f'Score: {len(s.body)} \nPlay again...')
                s.reset((random.randint(0,9),random.randint(0,9)), speed)
                break
 
           
        redrawWindow(win)
 
       
    pass
 
 
 
main()
