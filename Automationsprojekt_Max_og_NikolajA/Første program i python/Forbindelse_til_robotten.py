import math #importerer matematikbibliotek
import cv2 #importerer cv2 bibliotek, som skal bruges for at tjekke at det er installeret korrekt
from robotprogrammer import Robot_programmer #importerer særens "bibliotek" fra andet dokument
from Robotcam import Robotcam #importerer særens "bibliotek" fra andet dokument
from sympy.solvers import solve #importerer sympy bibliotek (dog skal man lige have installeret den nyeste version af sympy)
from sympy import Symbol #heter Symbol fra sympy, som bruges til at definere ubekendte

#kommandoer:
quit = "q"
help = "help"
move = "move"
home = "home"
moveA = "move_angle"
open = "open"
close = "close"
calibrate = "calib"
camFind = "cam find"
transform = "transform"


#Dictionary:
cmd = {}
cmd["Quits the program"] = quit
cmd["List of commands"] = help
cmd["Moves the robot to given position"] = move
cmd["Moves the robot to a home position"] = home
cmd["Move robot and give an angle rotating the grapper"] = moveA
cmd["Opens gripper of robot"] = open
cmd["Closes gripper of robot"] = close
cmd["Calibrates Camera"] = calibrate
cmd["Finds coordinates for block (cam coordinates)"] = camFind
cmd["Transforms information from camera to imput position for the robot (x,y)"] = transform


#Her oprettes et robot−objekt 4 
robot = Robot_programmer() 
#Her forbindes til robotten. 
robot.connect("10.130.58.14" , False)

 



while True:
    try:
        msg = input("\nSkriv her: ")
        
        if not msg:
            break
        elif msg == (quit):
            break
        elif msg == (help):
            print("\n")
            for navn in cmd:
                print("kommando: " + cmd[navn], " -  " + navn)
        elif msg == (move):
            command = input("Hvor skal robotten flytte sig hen?: ") #300 500 20 
            list1 = command.split() # ["300", "500", "20"]
            x = float(list1[0]) #300
            x = x/1000 #0.3
            
            y = float(list1[1]) #500
            y = y/1000 #0.5
            
            z = float(list1[2]) #20
            z = z/1000 #0.02

            robot.move_xyz(x , y, z) #taler til robotten i forhold til clasen i det andet dokument
        elif msg == (home):
            robot.move_home() #flytter sig til hjem-positionen defineret i det andet dokument
        elif msg == (moveA):
            command = input("Hvor skal robotten flytte sig hen?: ") #300 500 20 & en vinkel 3
            list1 = command.split()
            x = float(list1[0]) #300
            x = x/1000 #0.3
            
            y = float(list1[1]) #500
            y = y/1000 #0.5
            
            z = float(list1[2]) #20
            z = z/1000 #0.02
            
            a = float(list1[3]) #3
            a = a*2*math.pi/360 #konverterer graderne til radianer, da robotten arbejder i radianer
            
            robot.move_xyza(x , y, z, a) #sender informationerne til robotten, så det bliver udført
        elif msg == (open):
            robot.open_gripper() #åbner gripperen på en predefineret måde
        elif msg == (close):
            robot.close_gripper() #lukker gripperen på en predefineret måde
        elif msg == (calibrate):
            command = input("Skriv informationerne: ") # her skal man skrive informationerne man får fra find cam analysen
            list1 = command.split() #laver en liste ud fra informationerne
            while len(list1) != 8: #hvis der ikke er 8 elementer af informationer, kør det igen, indtil der er
                print("Der er ikke 8 informationer!")
                command = input("Skriv informationerne: ")
                list1 = command.split()
            '''
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
            x1 = int(list1[0])
            y1 = int(list1[1])
            x1Camera = int(list1[2])
            y1Camera = int(list1[3])
            x2 = int(list1[4])
            y2 = int(list1[5])
            x2Camera = int(list1[6])
            y2Camera = int(list1[7])
            
            
            #ligning1
            #definerer ax og bx i sympy systemet
            ax = Symbol('ax')
            bx = Symbol('bx')
            
            #solver ved hjælp af sympy biblioteket (ligningen er lig 0, så man skal tage højresiden og trække fra på begge sider for at løse den)
            axL = solve(ax*x2-ax*x1Camera + x1 - x2Camera, ax)
            axS = axL[0]
            bxL = solve(axS*x1Camera + bx - x1, bx)
            bxS = bxL[0]
            
            #ligning2
            ay = Symbol('ay')
            by = Symbol('by')
            
            ayL = solve(ay*y2-ay*y1Camera + y1 - y2Camera, ay)
            ayS = ayL[0]
            byL = solve(ayS*y1Camera + by - y1, by)
            byS = byL[0]
            
            #for begge ligninger er der gæmt værdier ax, ay, bx, by som skal bruges i transform
            
            print("Kalibrering ok")
            
        elif msg == (transform):
            #man skriver informationerne fra cameraret
            xCamera = int(input("x Camera: "))
            yCamera = int(input("y Camera: " ))
            
            #sætter dem ind i ligningen for at transformere og få værdien, som skal ind i robotten
            ligning1 = axS*xCamera + bxS
            ligning2 = ayS*yCamera + byS
            
            #printer værdierne som robotten skal have, for at placere sig ved klodsen i x- og y-koordinatsystemet
            print("(", ligning1, ",", ligning2, ")")
        elif msg == (camFind): 
            #Her oprettes et cam−objekt
            cam = Robotcam()
            cam.analyze() 
        else:
            print("\nDu skrev " + str(msg))
    except:
        break
print("Tak for nu")