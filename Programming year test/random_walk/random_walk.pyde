pos = [0, 0]

def setup():
    global frame_counter
    global sec_counter
    global pos
    global prik_color
    global n
    global v
    
    size(500,500)
    background(0)
    
    frame_counter = 0
    sec_counter = 0
    pos = [width/2, height/2]
    prik_color = color(random(0,255), random(0,255), random(0,255))
    
    n = 0
    v = 0
    
    frameRate(60)
    

def draw():
    global frame_counter
    global sec_counter
    global pos
    global prik_color
    
    frame_counter += 1
    if frame_counter % 300 == 0:
        prik_color = color(random(0,255), random(0,255), random(0,255))

    #Vælg bevægelse i x
    if random(0,1) > 0.5:
        x_step = -2
    else:
        x_step = 2
    #Vælg bevægelse i y
    if random(0,1) > 0.5:
        y_step = -2
    else:
        y_step = 2

    #Flyt prikken
    pos[0] += x_step
    pos[1] += y_step
    
    #Fade
    fill(0,0,0,1)
    rect(0,0,width, height)
    
    #Tegn prikken    
    noStroke()
    fill(prik_color)
    ellipse(pos[0], pos[1], 4, 4)
    
def keyPressed():
    global prik_color
    if key == 'c':
        prik_color = color(random(0,255), random(0,255), random(0,255))

def mousePressed():
    if mouseX <= pos[0]:
        v = -10
    if mouseX >= pos[0]:
        v = 10
    if mouseY <= pos[1]:
        n = -10
    if mouseY >= pos[1]:
        n = 10
    pos[0] += v
    pos[1] += n
    
    #Fade
    fill(0,0,0,1)
    rect(0,0,width, height)
    
    #Tegn prikken    
    noStroke()
    fill(prik_color)
    ellipse(pos[0], pos[1], 4, 4)
    
