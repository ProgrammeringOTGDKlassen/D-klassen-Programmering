add_library('minim')

from CopLib import *
from RobberLib import *
import time
from random import randint

def setup():
    size(1000, 1000)
    global cops, cWin, rWin, cCounter, rCounter, counter, copNumber, afstandList, RoboIMG, PopoIMG, popoH, popoW, roboW, roboH, IMGsize, winNumber, soundFile, minim, robberSound, robberWinSound
    fps = 1000
    copNumber = 10
    cops = list()
    initialize()
    textSize(15)
    cWin = False
    rWin = False
    cCounter = 0
    rCounter = 0
    counter = 0
    afstandList = []
    frameRate(fps)
    PopoIMG = loadImage("Popo.png")
    RoboIMG = loadImage("Robber.png")
    IMGsize = 60
    popoH = IMGsize * 0.8
    popoW = IMGsize * 1.2
    roboW = IMGsize
    roboH = IMGsize
    winNumber = 0
    minim=Minim(this)
    sf=minim.loadFile("rollin.mp3")
    sf.play()
    sf.shiftGain(sf.getGain(),-15, 2500)
    robberSound = ["oof.mp3", "mc_oof.mp3"]
    robberWinSound = ["crap_rave.mp3"]

def initialize(rPos = False):
    #I denne funktion skal hele spillet
    #startes forfra.
    global cops, robber, running, copNumber
    #Bagrunden cleares
    background(0)
    
    running = True
    
    #Ny position til røveren
    if rPos:
        robber = Robber(rPos.x, rPos.y)
    else:
        robber = Robber(width/2, height/2)
    
    #Nye positioner til politiet.
    #Tøm listen
    cops[:] = []
    #og tilføj nye politimænd
    for i in range(0,copNumber):
        x = random(10, width - 10)
        y = random(10, height - 10)
        cops.append(Cop(x,y))
    
def draw():
    global cops, robber, running, cWin, rWin, cCounter, rCounter, counter, winNumber, soundFile
    rWin = False
    cWin = False
    
    if running:
        moveRobber()
        moveCops()
    
    if robberWin(robber):
        #Her kan du vælge hvad der skal ske
        #hvis røveren vinder
        if running:
            print("The robber wins")
        # running = False
        rWin = True
        percent = winPercentage(cWin, rWin)
        if percent[0]:
            print(percent[1])
        theFile = robberWinSound[0]
        sf=minim.loadFile(theFile)
        sf.play()
        langde = float(sf.length()/1000)
        time.sleep(langde)
        initialize()
        winNumber = 1
        info(winNumber)
        
        
    if copsWin(cops, robber):
        #Her kan du vælge hvad der skal ske
        #hvis politiet vinder
        if running:
            print("The Cops wins")
        # running = False
        cWin = True
        percent = winPercentage(cWin, rWin)
        if percent[0]:
            print(percent[1])
        theFile = robberSound[randint(0,1)]
        sf=minim.loadFile(theFile)
        sf.play()
        langde = float(sf.length()/1000)
        time.sleep(langde)
        initialize()
        winNumber = 2
        info(winNumber)
    
    total = float(rCounter)+float(cCounter)
    fill(255,255,255)
    text('Total: {}'.format(int(total)), 4, height-4)
    
    drawCopsAndRobbers()

def info(winner):
    global cops, robber, running, cWin, rWin, cCounter, rCounter, counter
    if winner == 1:
        fill(0,255,0)
        text('Robber points {}'.format(rCounter),10,15)
        fill(255,0,0)
        text('Rops points {}'.format(cCounter),width-120,15)
        fill(255,255,255)
        percent = (float(rCounter)/(float(rCounter)+float(cCounter)))*100
        percent = "{:10.2f}".format(percent)
        text('{}%'.format(percent),width/2 - 40,15)
    if winner == 2:
        fill(0,255,0)
        text('Cops points {}'.format(cCounter),width-121,15)
        fill(255,0,0)
        text('Robber points {}'.format(rCounter),10,15)
        fill(255,255,255)
        percent = (float(rCounter)/(float(rCounter)+float(cCounter)))*100
        percent = "{:10.2f}".format(percent)
        text('{}%'.format(percent),width/2 - 40,15)

def winPercentage(cWin, rWin):
    global cCounter, rCounter, counter
    ready = False
    counter += 1
    cPercent = 0
    rPercent = 0
    string = ""
    if cWin:
        cCounter += 1
    if rWin:
        rCounter += 1
    total = cCounter + rCounter
    if total != 0:
        ready = True
        cPercent = (float(cCounter) / float(total)) * 100
        rPercent = (float(rCounter) / float(total)) * 100
    if ready:
        string = "The game has run: {} times \nPolice win: {}% \nRobber wins {}%".format(counter, cPercent, rPercent)
    return ready, string
    

def robberWin(robber):
    global popoH, popoW, roboW, roboH
    #Denne funktion skal returnere True,
    #hvis røveren er nået udenfor skærmen
    checker = False
    if robber.pos.y + roboH >= height or robber.pos.x <= 0 or robber.pos.y <= 0 or robber.pos.x + roboW >= width:
        checker = True
    return checker

def copsWin(cops, robber):
    global popoH, popoW, roboW, roboH, IMGsize
    #Denne funktion skal returnere True,
    #hvis politiet har fanget røveren
    checker = False
    for cop in cops:
        distance = dist(cop.pos.x + (popoW/2), cop.pos.y + (popoH/2), robber.pos.x + (roboW/2), robber.pos.y + (roboH/2))
        if distance < IMGsize/2:
            checker = True
    return checker
          
def moveCops():
    #Politiet bevæger sig imod det sted hvor røveren er.
    #Det er nemlig sådan politet gør.
    for cop in cops:
        afstand = robber.pos.copy()
        afstand.sub(cop.pos)

        afstand += robber.last * (dist(cop.pos.x, cop.pos.y, robber.pos.x, robber.pos.y))
        #Sørg for at politiet kun bevæger sig 1 pixel
        afstand.normalize()
        afstand.mult(cop.speed)
        
        cop.pos.add(afstand)

def moveRobber():
    global COM, robber, distList
    #Udregn massemidtpunkt for politiet.
    #COM = Center of Mass
    COM = PVector()
  
    totalWeight = 0
    for cop in cops:
        distance = dist(cop.pos.x, cop.pos.y, robber.pos.x, robber.pos.y)
        w = (60/distance)**2

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
    robber.last = afstand

    
def drawCopsAndRobbers():
    global COM, cops, robber, RoboIMG, PopoIMG, popoH, popoW, roboW, roboH, winNumber
    background(0)
    info(winNumber)
    
    fill(255)
    ellipse(COM.x, COM.y, 1, 1)
    
    fill(robber.col)
    #ellipse(robber.pos.x, robber.pos.y, 1, 1)
    image(RoboIMG, robber.pos.x, robber.pos.y, roboW, roboH)
    
    for cop in cops:
        noStroke()
        fill(cop.col)
        #ellipse(cop.pos.x, cop.pos.y, 1, 1)
        image(PopoIMG, cop.pos.x, cop.pos.y, popoW, popoH)
        
def keyPressed():
    if key == "r":
        initialize()
        print("New Game")
        
def mousePressed():
    rPos = PVector(mouseX, mouseY)
    initialize(rPos)
