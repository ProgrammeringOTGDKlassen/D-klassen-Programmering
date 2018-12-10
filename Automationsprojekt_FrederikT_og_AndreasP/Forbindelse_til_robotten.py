IP = "10.130.58.13"

import math #importerer matematikbibliotek
import cv2 #importerer cv2 bibliotek, som skal bruges for at tjekke at det er installeret korrekt
from robotprogrammer import Robot_programmer #importerer særens "bibliotek" fra andet dokument
from Robotcam import RobotCam #importerer særens "bibliotek" fra andet dokument
from sympy.solvers import solve #importerer sympy bibliotek (dog skal man lige have installeret den nyeste version af sympy)
from sympy import Symbol #heter Symbol fra sympy, som bruges til at definere ubekendte
from rTData import RTData

#kommandoer:
kommando_quit = "q"
kommando_help = "help"
kommando_move = "move"
kommando_home = "home"
kommando_moveA = "angle"
kommando_open = "open"
kommando_close = "close"
kommando_calibrate = "calib"
kommando_camFind = "cam"
kommando_transform = "transform"
kommando_camConnect = "connect"
kommando_find = "find"
kommando_stat = "status"
kommando_pos = "position"
kommando_conf = "conf"
kommando_fmove = "relative"
kommando_fmoveA = "rangle"
kommando_antal = "antal"
kommando_automation = "automation"

#Dictionary:
cmd = {}
cmd["Quits the program"] = kommando_quit
cmd["List of commands"] = kommando_help
cmd["Moves the robot to a home position"] = kommando_home
cmd["Moves the robot to given position"] = kommando_move
cmd["Move robot and give an angle rotating the grapper"] = kommando_moveA
cmd["Moves the robot relative to it's realtime position"] = kommando_fmove
cmd["Moves the angle of the robot relative to it's realtime position"] = kommando_fmoveA
cmd["Finds the block and moves the robot to that position"] = kommando_find
cmd["Automates the robot process"] = kommando_automation
cmd["Shows the amount of blocks the robot has moved"] = kommando_antal
cmd["Opens gripper of robot"] = kommando_open
cmd["Closes gripper of robot"] = kommando_close
cmd["Connects to the camera"] = kommando_camConnect
cmd["Finds coordinates for block (cam coordinates)"] = kommando_camFind
cmd["Calibrates Camera"] = kommando_calibrate
cmd["Transforms information from camera to imput position for the robot (x,y)"] = kommando_transform
cmd["1.0: the robot is still - 2.0: the robot is moving"] = kommando_stat
cmd["Gets the position of the robot"] = kommando_pos
cmd["Gets the configuration of the robot"] = kommando_conf

#Her oprettes et robot−objekt 4 
robot = Robot_programmer() 
#Her forbindes til robotten. 
robot.connect(IP , False)

rtd = RTData()
rtd.connect(IP, False)

#variabler
cal = False
camOnline = False
amount = 0
failsafe = 0
ax = None
bx = None
ay = None
by = None


#funktioner:

def wait(s = 2):
    while rtd.program_state == s:
        pass

#Funktionen tager en liste og tjekker om længden er ens med det 3. parameter, hvis ikke; spørg igen...
def lenChecker(first, list1, l):
    list1.remove(first)
    while len(list1) != l:
        print("Der er ikke {} informationer!".format(l))
        command = input("Skriv informationerne: ")
        list1 = command.split()
    return list1

#Tjekker status for robotten og retunerer værdien
def status(x = False):
    stat = rtd.program_state
    if x:
        print(stat)
    return stat

#Tjekker positionen for robotten og returnerer den
def position(x = False):
    pos = rtd.tool_frame 
    if x:
        print(pos)
    return pos

#Tjekker configurationen af robotten og retunerer det
def configuration(x = False):
    conf = rtd.qactual
    if x:
        print(conf)
    return conf

#Sender informationer (parameter 1,2,3) til robotten om at flytte til
def move(x, y, z):
    x = float(x)/1000 
    y = float(y)/1000 
    z = float(z)/1000
    stat = status()
    if stat == 1:
        robot.move_xyz(x , y, z)
    elif stat == 0:
        print("Robotten er ikke forbundet!")
    else:
        print("Robotten er i bevægelse")

#Gør det samme som move(), men tilføjer en vinkel
def moveA(x, y, z, rz):
    x = float(x)/1000 #0.3
    y = float(y)/1000 #0.5
    z = float(z)/1000 #0.02
    rz = float(rz) #3
    rz = rz*2*math.pi/360

    stat = status()
    if stat == 1:
        robot.move_xyza(x , y, z, rz) #sender informationerne til robotten, så det bliver udført
    elif stat == 0:
        print("Robotten er ikke forbundet!")
    else:
        print("Robotten er i bevægelse")

#Roterer robotten et givent antal grader i forhold til vinklen robtten har
def relativ_vinkel(rz):
    rz = float(rz)
    rz = rz*2*math.pi/360
    stat = status()
    if stat == 1:
        pos = rtd.tool_frame
        robot.move_xyza(pos[0], pos[1], pos[2], pos[5] + rz)
    elif stat == 0:
        print("Robotten er ikke forbundet!")
    else:
        print("Robotten er i bevægelse")

#Åbner gribearmen på robotten
def open_gripper():
    stat = status()
    if stat == 1:
        robot.open_gripper()
    elif stat == 0:
        print("Robotten er ikke forbundet!")
    else:
        print("Robotten er i bevægelse")

#Lukker gribearmen på robotten
def close_gripper():
    stat = status()
    if stat == 1:
        robot.close_gripper()
    elif stat == 0:
        print("Robotten er ikke forbundet!")
    else:
        print("Robotten er i bevægelse")

#Kalibrerer robottens koordinater med kameraets koordinater, så den robotten efterfølgende selv kan finde ud hvordan den skal positionenere sig for at den står rigtigt
def calibrate(x1, y1, x1Camera, y1Camera, x2, y2, x2Camera, y2Camera, ar1, ac1, ar2, ac2):
    global axS, bxS, ayS, byS, aa, ab
    ar1 = float(ar1)
    ac1 = float(ac1)
    ar2 = float(ar2)
    ac2 = float(ac2)
    '''
    300 80 50 30 70 150 110 90
    #list1[0] = 300 x1
    list1[1] = 80 y1
    #list1[2] = 50 x1 camera
    list1[3] = 30 y1 camera
    #list1[4] = 70 x2
    list1[5] = 150 y2
    #list1[6] = 110 x2 camera
    list1[7] = 90 y2 camera
    '''
    #tager informationerne fra listen og sepererer dem, så de kan regnes med
    x1 = float(x1)
    y1 = float(y1)
    x1Camera = float(x1Camera)
    y1Camera = float(y1Camera)
    x2 = float(x2)
    y2 = float(y2)
    x2Camera = float(x2Camera)
    y2Camera = float(y2Camera)
    
    #ligning1
    #definerer ax og bx i sympy systemet
    ax = Symbol('ax')
    bx = Symbol('bx')
    
    #solver ved hjælp af sympy biblioteket (ligningen er lig 0, så man skal tage højresiden og trække fra på begge sider for at løse den)
    axL = solve(ax*x1Camera + bx - x1, ax)
    axS = axL[0]
    bxL = solve(axS*x2Camera + bx - x2, bx)
    bxS = float(bxL[0])
    axL = solve(ax*x1Camera + bxS - x1, ax)
    axS = float(axL[0])

    #ligning2
    ay = Symbol('ay')
    by = Symbol('by')
    
    ayL = solve(ay*y1Camera + by - y1, ay)
    ayS = ayL[0]
    byL = solve(ayS*y2Camera + by - y2, by)
    byS = float(byL[0])
    ayL = solve(ay*y1Camera + byS - y1, ay)
    ayS = float(ayL[0])
    

    aa = (ar1 - ar2) / (ac1 - ac2)
    ab = ar1 - (aa * ac1)

    #for begge ligninger er der gæmt værdier ax, ay, bx, by som skal bruges i transform
    print("\nax er:", axS, "\nbx er:", bxS, "\nay er:", ayS, "\nby er:", byS)

    print("Kalibrering ok")

    return axS, bxS, ayS, byS, aa, ab

#Transformerer, dvs. tjekker om kalibreringen er lavet rigtigt
def transform(cal, xCamera, yCamera, aCam):
    if cal:
        aCam = float(aCam)  
        xCamera = float(xCamera)
        yCamera = float(yCamera)
        
        #sætter dem ind i ligningen for at transformere og få værdien, som skal ind i robotten
        ligning1 = float(ax*xCamera + bx)
        ligning2 = float(ay*yCamera + by)

        test = aCam * aa + ab
        

        print("Dette er en test, hvor angle er {}".format(test))
        #printer værdierne som robotten skal have, for at placere sig ved klodsen i x- og y-koordinatsystemet
        print("(", ligning1, ",", ligning2, ")")
    else:
        print("Calibrate first pls")

#Forbinder til cameraret
def cam_connect():
    global cam
    #Her oprettes et cam−objekt
    try:
        cam = RobotCam()
    except:
        print("Kunne ikke forbinde til kameraret!")

#Bruger cameraret til at finde en klods
def cam_find(camOnline):
    if camOnline:
        cam.analyze()
    else:
        print("Kameraret er ikke forbundet!")

#Finder en klods med kameraret og flytter robotten derhen
def find(cal, camOnline, ax, bx, ay, by):
    if cal and camOnline:
        array = cam.analyze()
        print(array)
        xc = float(array[0])
        yc = float(array[1])

        xr = xc * ax + bx
        yr = yc * ay+ by
        print(xr)
        print(yr)
        stat = status()
        if stat == 1:
            robot.move_xyz(xr/1000, yr/1000, float(245)/1000)
        elif stat == 0:
            print("Robotten er ikke forbundet!")
        else:
            print("Robotten er i bevægelse")
    else:
        print("Calibrate and/or connect camera first pls")

#Flytter robotten relativt til dens nuværende position
def relative(x, y, z):
    x = float(x)/1000
    y = float(y)/1000
    z = float(z)/1000
    stat = status()
    if stat == 1:
            pos = rtd.tool_frame
            robot.move_xyz(float(pos[0])+x, float(pos[1])+y, float(pos[2])+z)
    elif stat == 0:
        print("Robotten er ikke forbundet!")
    else:
        print("Robotten er i bevægelse")

#Viser antallet af klodser flyttet, eller sætter en ny værdi for det
def antal(x, amount):
    if len(x) == 1:
        print(amount)
    else:
        m = lenChecker(x[0], x, 1)
        amount = m[0]
        print(amount)
    return amount

#komandosystem:
#Kalder nødvendige funktioner i forhold til kommandoen der skal udføres
while True:
    try:
        msg = input("\nSkriv her: ")
        
        if not msg:
            break
       
        elif msg.startswith(kommando_quit):
            break
        
        elif msg.startswith(kommando_help):
            print("")
            counter = 1
            for navn in cmd:
                print(counter, "-", "kommando: " + cmd[navn], " - ", navn)
                counter += 1
       
        elif msg.startswith(kommando_move):
            m = msg.split()
            m = lenChecker(m[0], m, 3)
            move(m[0], m[1], m[2])
       
        elif msg.startswith(kommando_home):
            robot.move_home() #flytter sig til hjem-positionen defineret i det andet dokument
       
        elif msg.startswith(kommando_moveA):
            m = msg.split()
            m = lenChecker(m[0], m, 4)
            moveA(m[0], m[1], m[2], m[3])
       
        elif msg.startswith(kommando_fmoveA):
            m = msg.split()
            m = lenChecker(m[0], m, 1)
            relativ_vinkel(m[0])
       
        elif msg.startswith(kommando_open):
            open_gripper()
            
        elif msg.startswith(kommando_close):
            close_gripper()
      
        elif msg.startswith(kommando_calibrate):
            m = msg.split()
            m = lenChecker(m[0], m, 12)
            elementer = calibrate(m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11])
            ax = elementer[0]
            bx = elementer[1]
            ay = elementer[2]
            by = elementer[3]
            aa = elementer[4]
            ab = elementer[5]
            cal = True
            
        elif msg.startswith(kommando_transform):
            m = msg.split()
            m = lenChecker(m[0], m, 3)
            transform(cal, m[0], m[1], m[2])
       
        elif msg.startswith(kommando_camConnect):
            cam_connect()
            camOnline = True
       
        elif msg == (kommando_camFind):
            cam_find(camOnline)
       
        elif msg == (kommando_find):
            find(cal, camOnline, ax, bx, ay, by)
       
        elif msg == (kommando_stat):
            status(True)
                  
        elif msg == (kommando_pos):
            position(True)
      
        elif msg == (kommando_conf):
            configuration(True)
     
        elif msg.startswith(kommando_fmove):
            m = msg.split()
            m = lenChecker(m[0], m, 3)
            relative(m[0], m[1], m[2])

        elif msg.startswith(kommando_antal):
            m = msg.split()
            amount = antal(m, amount)
            
        
        elif msg == (kommando_automation):
            if cal and camOnline:
                robot.move_home()
                for i in range(2):
                    array = cam.analyze()
                    #while len(array) > 2:
                     #   array = cam.analyze()
                    xc = float(array[0])
                    yc = float(array[1])
                    a = float(array[2])
                    
        
                    xr = xc * axS + bxS
                    yr = yc * ayS + byS
                    ar = (aa * a + ab)
                    ar = ar*2*math.pi/360
                    #*360/(2*math.pi)
                    print(xr)
                    print(yr)
                    if yr < -400:
                        print("Den rykker sig for meget på y-aksen!")
                        failsafe = 1
                    stat = status()
                    if stat == 0:
                        print("Robotten er ikke forbundet!")
                    elif failsafe == 0:
                        robot.move_xyza(xr/1000, yr/1000, float(245)/1000, ar)
                        wait(1)
                        wait()
                        #open_gripper()
                        robot.open_gripper()
                        wait(1)
                        wait()
                        pos = rtd.tool_frame
                        #move(pos[0], pos[1], pos[2]-float(167)/1000)
                        robot.move_xyz(pos[0], pos[1], pos[2]-float(167)/1000)
                        wait(1)
                        wait()
                        #close_gripper()
                        robot.close_gripper()
                        amount += 1
                        wait(1)
                        wait()
                        robot.move_home()
                        wait(1)
                        wait()
                        pos = rtd.tool_frame
                        #move(pos[0], pos[1], pos[2]-float(175)/1000)
                        robot.move_xyz(pos[0], pos[1], pos[2]-180/1000)
                        wait(1)
                        wait()
                        pos = rtd.tool_frame
                        #move(pos[0], pos[1]-float(25)/1000*amount, pos[2])
                        robot.move_xyz(pos[0], pos[1]+float(25)/1000*amount, pos[2])
                        wait(1)
                        wait()
                        #open_gripper()
                        robot.open_gripper()
                        wait(1)
                        wait()
                        robot.move_home()
           
            else:
                print("Calibrate and/or connect camera first pls")
        else:
            print("\nDu skrev " + str(msg))
    except Exception as e:
        print(e)
        break
rtd.disconnect()
print("Tak for nu")