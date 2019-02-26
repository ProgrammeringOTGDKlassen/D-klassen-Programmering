from CopLib import *
from RobberLib import *

def setup():
    size(500,500)
    global cops, copsCanWin, robberCanWin
    
    cops = list()
    initialize()
    
    copsCanWin = True
    robberCanWin = True
    
def initialize():
    #I denne funktion skal hele spillet
    #startes forfra.
    global cops, robber, running
    
    #Bagrunden cleares
    background(0)
    
    running = True
    
    #Ny position til røveren
    robber = Robber(width/2, height/2)
    
    #Nye positioner til politiet.
    #Tøm listen
    cops[:] = []
    #og tilføj nye politimænd
    for i in range(0,150):
        x = random(10, width - 10)
        y = random(10, height - 10)
        cops.append(Cop(x,y))
    
def draw():
    global cops, robber, copsCanWin, robberCanWin, running
    if running:
        moveRobber()
        moveCops()
    
    if robberWin(robber) and robberCanWin:
        #Her kan du vælge hvad der skal ske
        #hvis røveren vinder
        if running:
            print("The robber wins")
        running = False
        # initialize()
        copsCanWin = False
        
        
    if copsWin(cops, robber) and copsCanWin:
        #Her kan du vælge hvad der skal ske
        #hvis politiet vinder
        if running:
            print("The Cops wins")
        running = False
        # initialize()
        robberCanWin = False
    
    drawCopsAndRobbers()
    
def robberWin(robber):
    #Denne funktion skal returnere True,
    #hvis røveren er nået udenfor skærmen
    checker = False
    if robber.pos.y >= height or robber.pos.x <= 0 or robber.pos.y <= 0 or robber.pos.x >= width:
        checker = True
    return checker

def copsWin(cops, robber):
    #Denne funktion skal returnere True,
    #hvis politiet har fanget røveren
    checker = False
    for cop in cops:
        distance = dist(cop.pos.x, cop.pos.y, robber.pos.x, robber.pos.y)
        if distance < 1 and distance > -1:
            checker = True
    return checker
            
def moveCops():
    #Politiet bevæger sig imod det sted hvor røveren er.
    #Det er nemlig sådan politet gør.
    for cop in cops:
        afstand = robber.pos.copy()
        afstand.sub(cop.pos)
        #Sørg for at politiet kun bevæger sig 1 pixel
        afstand.normalize()
        afstand.mult(cop.speed)
        
        cop.pos.add(afstand)

def moveRobber():
    global COM
    #Udregn massemidtpunkt for politiet.
    #COM = Center of Mass
    COM = PVector()
  
    totalWeight = 0
    for cop in cops:
        w = 1
        totalWeight += w
        COM.x += cop.pos.x * w
        COM.y += cop.pos.y * w
      
    COM.x /= totalWeight
    COM.y /= totalWeight

    #Find retningen væk fra COM.
    #Beregn afstanden til massemidtpunktet
    afstand = robber.pos.copy()
    afstand.sub(COM)
    
    #Vælg hvor langt røveren skal bevæge sig
    afstand.normalize()
    afstand.mult(robber.speed)
    
    #Flyt røveren
    robber.pos.add(afstand)

    
def drawCopsAndRobbers():
    global COM, cops, robber
    
    fill(255)
    ellipse(COM.x, COM.y, 1, 1)
    
    fill(robber.col)
    ellipse(robber.pos.x, robber.pos.y, 1, 1)
    
    for cop in cops:
        noStroke()
        fill(cop.col)
        ellipse(cop.pos.x, cop.pos.y, 1, 1)
        
def keyPressed():
    if key == "r":
        initialize()
        print("New Game")
