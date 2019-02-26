from CopLib import *
from RobberLib import *

def setup():
    size(500,500)
    global cops
    
    cops = list()
    initialize()
    
def initialize():
    #I denne funktion skal hele spillet
    #startes forfra.
    global cops,robber
    
    #Bagrunden cleares
    background(0)
    
    #Ny position til røveren
    robber = Robber(width/2, height/2)
    
    #Nye positioner til politiet.
    #Tøm listen
    cops[:] = []
    #og tilføj nye politimænd
    for i in range(0,15):
        x = random(10, width - 10)
        y = random(10, height - 10)
        cops.append(Cop(x,y))
    
def draw():
    global cops, robber
    
    moveRobber()
    moveCops()
    
    if robberWin():
        #Her kan du vælge hvad der skal ske
        #hvis røveren vinder
        pass
        
    if copsWin():
        #Her kan du vælge hvad der skal ske
        #hvis politiet vinder
        pass
    
    drawCopsAndRobbers()
    
    
def robberWin():
    #Denne funktion skal returnere True,
    #hvis røveren er nået udenfor skærmen
    return False

def copsWin():
    #Denne funktion skal returnere True,
    #hvis politiet har fanget røveren
    return False    
            
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