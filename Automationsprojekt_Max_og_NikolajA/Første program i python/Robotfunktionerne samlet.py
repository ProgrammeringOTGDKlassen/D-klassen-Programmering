from robotprogrammer import Robot_programmer #Importere robotfunktionerne som move_home() osv fra et andet dokument
from robotCam import RobotCam #Importere robot kamera så man kan finde koordinater med et kamera
from rTData import RTData #Importere RTData så man kan finde informationer om robotten
import math #Importere math, har har vi brugt det til pi
import cv2 #Importere cv2 som bruges til kameraet
import time #Importere time som vi har brugt da vi skulle automatisere vores program
robot = Robot_programmer() #Definere robot som Robot_programmer()
cam = RobotCam() #Definere cam som RobotCam()
robot.connect("10.130.58.11",True)#Change to false to connect. Tilslutter til robotten. Tjek ip for rigtig forbindelse

#Forskellige variabler
prompt = '\nSkriv her > ' #Ændre prompt som vi bruger til input
x = 0 #Sætter x til 0
y = 0 #Sætter y til 0
z = 0 #Sætter z til 0
a = 0 #Sætter a til 0
Calibrated = 0 #Sætter Calibrated til 0
antal1 = 0 #Sætter antal1 til 0
rtd = RTData() #sætter rts som præfix for RTData()
rtd.connect('10.130.58.11',True)#Change to false to connect. Tilslutter til robottens data. Tjek ip for rigtig forbindelse

#Forskellige beskeder/kommandoer
quit = "quit"
help = "help"
reset = "reset"
move = "move"
moveA = "moveA"
moveX = "moveX"
moveY = "moveY"
moveZ = "moveZ"
moveXYZ = "moveXYZ"
home = "home"
open = "open"
close = "close"
camfind = "cam find"
calib = "calib"
transform = "transform"
getPos = "getPos"
getStat = "getStat"
getConf = "getConf"
complete = "complete"
antal = "antal"
AutoMove = "AutoMove"

#CMD med alle de forskellige kommandoer som er beskrevet
CMD = {}
CMD["Lukker programmet"] = quit
CMD["Liste af kommandoer"] = help
CMD["Resetter promt og andre ting"] = reset
CMD["Rykker robotten til angivene koordinater"] = move
CMD["Rykker robotten til angivene koordinater og drejer gripperen"] = moveA
CMD["Rykker robotten relativt til x aksen så den ikke rykker fra side til side"] = moveX
CMD["Rykker robotten relativt til y aksen så den ikke rykker fra side til side"] = moveY
CMD["Rykker robotten relativt til z aksen så den ikke rykker fra side til side"] = moveZ
CMD["Rykker robotten relativt til x,y,z aksen"] = moveXYZ
CMD["Åbner gripperen"] = open
CMD["Lukker gripperen"] = close 
CMD["Finder koordinaterne til klodsen med kamera"] = camfind
CMD["Kalibrerer kameraet"] = calib
CMD["Tager kamerakoordinater og laver om til robot koordinater"] = transform
CMD["Finder robottens aktuelle position"] = getPos
CMD["Finder robottens aktuelle status"] = getStat
CMD["Finder robottens aktuelle konfiguration"] = getConf
CMD["Plusser antal med 1"] = complete
CMD["Viser hvor mange enheder der er rykket | Sætter antal rykkede enheder"] = antal
CMD["Finder klodsen og rykker robotten hen til den"] = AutoMove

while(True): #Kører programmet hele tiden når det er true
    try: 
        msg = input(prompt) #Definere msg som den besked vi skriver
        if not msg: #Hvis der ikke er nogen besked stopper programmet
            rtd.disconnect() #Disconnecter fra RTData så programmet stopper
            break #Stopper programmet
        
        if msg == (quit): #Hvis msg == quit så stopper programmet
            rtd.disconnect() #Disconnecter fra RTData så programmet stopper
            break #Stopper programmet
        elif msg == (reset): #resetter programmet
            prompt = '\nSkriv her > ' #Indstiller prompt
            x = 0 #Sætter x til 0
            y = 0 #Sætter y til 0
            z = 0 #Sætter z til 0
            a = 0 #Sætter a til 0
            Calibrated = 0 #Sætter Calibrated til 0
            antal1 = 0 #Sætter antal1 til 0
            print('Programmet er blevet resat')
        elif msg == (help): #Printer alle kommandoer og beskrivelse af dem
            for name in CMD: #Looper igennem CMD
                print("Kommando: "+ CMD[name], "- "+ name)
        
        elif msg == (getPos): #Printer robottens position
            pos = rtd.tool_frame #Robottens aktuelle position
            print(pos)
        elif msg == (getStat): #Printer robottens status
            status = rtd.program_state #Robottens aktuelle status. 1.0 = stille og 2.0 = bevægelse
            print(status)
        elif msg == (getConf): #Printer configurationen
            conf = rtd.qactual #Robottens aktuelle konfiguration
            print(conf)
        
        elif msg == (move): #Kan rykke robottn
            status = rtd.program_state #Robottens aktuelle status. 1.0 = stille og 2.0 = bevægelse
            
            command = input('Hvor skal robotten hen? Format: [x y z]: ') #Skriv tal i millimeter! 
            list1 = command.split() #Deler de tal man har skrevet op efter hvert mellemrum og laver en liste
            
            x = float(list1[0]) #Definere x som det første tal i listen
            x = x/1000 #Laver x om til millimeter
            
            y = float(list1[1]) #Definere y som det andet tal i listen
            y = y/1000 #Laver y om til millimeter
            
            z = float(list1[2]) #Definere z som det tredje tal i listen
            z = z/1000 #Laver z om til millimeter
            if(status == 1.0): 
                robot.move_xyz(x, y, z) #Rykker robotten til koordinaterne x, y, z
                print('Rykker robotten til {}, {}, {}'.format(x, y, z))
            else:
                print("[WARNING] The robot is moving. Wait until it's done!")
        elif msg == (moveA):  #Kan rykke robotten og dreje gripperen
            status = rtd.program_state #Robottens aktuelle status. 1.0 = stille og 2.0 = bevægelse
            
            command = input('Hvor skal robotten hen? Format: [x y z a]: ') #Skriv tal i millimeter! 
            list1 = command.split() #Deler de tal man har skrevet op efter hvert mellemrum og laver en liste
            x = float(list1[0]) #Definere x som det første tal i listen
            x = x/1000 #Laver x om til millimeter
            
            y = float(list1[1]) #Definere y som det andet tal i listen
            y = y/1000 #Laver y om til millimeter
            
            z = float(list1[2]) #Definere z som det tredje tal i listen
            z = z/1000 #Laver z om til millimeter
            
            a = float(list1[3]) #Definere a som det fjerde tal i listen
            a = a*2*math.pi/360 #Regner tallet om til 
            if(status == 1.0):
                robot.move_xyza(x, y, z, a) #Rykker robotten til koordinaterne x, y, z og drejer gripperen med a radianer
                print('Rykker robotten til {}, {}, {}, {}'.format(x, y, z, a))
            else:
                print("[WARNING] The robot is moving. Wait until it's done!")
        elif msg == (moveX): #Kan rykke robotten i x-aksen
            status = rtd.program_state #Får status
            
            command = input("Indtast x-koordinat: ") #Skriv til i millimeter
            list1 = command.split()
            
            x = float(list1[0]) #Definere x som det første tal i listen
            x = x/1000 #Laver x om til millimeter
            if(status == 1.0): #Tjekker om status er 1
                robot.move_relative_x(x) #Rykker robotten ved x-aksen
                print('Rykker robotten til x-koordinat: {}'.format(x))
            else:
                print("[WARNING] The robot is moving. Wait until it's done!")
        elif msg == (moveY): #Kan rykke robotten i y-aksen
            status = rtd.program_state #Får status
            
            command = input("Indtast y-koordinat: ") #Skriv til i millimeter
            list1 = command.split()
            
            y = float(list1[0]) #Definere y som det første tal i listen
            y = y/1000 #Laver y om til millimeter
            if(status == 1.0): #Tjekker om status er 1
                robot.move_relative_y(y) #Rykker robotten ved y-aksen
                print('Rykker robotten til y-koordinat: {}'.format(y))
            else:
                print("[WARNING] The robot is moving. Wait until it's done!")
        elif msg == (moveZ):  #Kan rykke robotten i z-aksen
            status = rtd.program_state #Får status
            
            command = input("Indtast z-koordinat: ") #Skriv til i millimeter
            list1 = command.split()
            
            z = float(list1[0]) #Definere z som det første tal i listen
            z = z/1000 #Laver z om til millimeter
            if(status == 1.0): #Tjekker om status er 1
                robot.move_relative_z(z) #Rykker robotten ved z-aksen
                print('Rykker robotten til z-koordinat: {}'.format(z))
            else:
                print("[WARNING] The robot is moving. Wait until it's done!")
        elif msg == (moveXYZ): #Kan rykke robotten i xyz-aksen
            status = rtd.program_state #Får status
            
            command = input("Indtast koordinater: Format:[x y z]: ") #Skriv til i millimeter
            list1 = command.split()
            
            x = float(list1[0]) #Definere x som det første tal i listen
            x = x/1000 #Laver x om til millimeter
            
            y = float(list1[1]) #Definere y som det første tal i listen
            y = y/1000 #Laver y om til millimeter
            
            z = float(list1[2]) #Definere z som det første tal i listen
            z = z/1000 #Laver z om til millimeter
            if(status == 1.0): #Tjekker om status er 1
                robot.move_relative_xyz(x,y,z) #Rykker robotten ved xyz-aksen
                print('Rykker robotten til koordinater: {}, {}, {}'.format(x,y,z))
            else:
                print("[WARNING] The robot is moving. Wait until it's done!")
        elif msg == (home): #Rykker robotten tilbage til dens normale position kaldet "home"
            robot.move_home()
        elif msg == (open): #Åbner gripperen
            status = rtd.program_state #Robottens aktuelle status. 1.0 = stille og 2.0 = bevægelse 
            if(status == 1.0): #Tjekker om status er 1
                robot.open_gripper() #Åbner griberen
            else:
                print("[WARNING] The robot is moving. Wait until it's done!")
        elif msg == (close): #Lukker gripperen
            status = rtd.program_state #Robottens aktuelle status. 1.0 = stille og 2.0 = bevægelse
            if(status == 1.0): #Tjekker om status er 1
                robot.close_gripper() #Lukker griberen
            else:
                print("[WARNING] The robot is moving. Wait until it's done!")
                
        elif msg == (camfind): #Kameraet tager et billede og gemmer det i mappen, udskriver koordinaterne som klodsen er i og hvilken vinkel som klodsen er i.
            cam.analyze()
        
        elif msg == (calib): 
            command = input('Skriv de 8 tal: ') #Skriv 8 tal
            list1 = command.split() #Deler de tal man har skrevet op efter hvert mellemrum og laver en liste
            
            while len(list1) != 8: #Hvis der ikke er 8 tal så skriver den en fejl besked og man skal prøve igen indtil der er 8 tal.
                print('[ERROR][To many or to few numbers!] Make sure you wrote 8 numbers!')
                command = input('Skriv de 8 tal: ') #Skriv 8 tal
                list1 = command.split() #Deler de tal man har skrevet op efter hvert mellemrum og laver en liste
            
            #Kx og Ky = klodsens koordinater. Bx og By er billedets koordinater.
            Kx1 = float(list1[0]) #Definere Kx1 som det første element i listen
            Ky1 = float(list1[1]) #Definere Ky1 som det andet element i listen
            Bx1 = float(list1[2]) #Definere Bx1 som det tredje element i listen 
            By1 = float(list1[3]) #Definere By1 som det fjerde element i listen
            Kx2 = float(list1[4]) #Definere Kx2 som det femte element i listen
            Ky2 = float(list1[5]) #Definere Ky2 som det sjette element i listen
            Bx2 = float(list1[6]) #Definere Bx2 som det syvende element i listen
            By2 = float(list1[7]) #Definere By2 som det ottende element i listen
            
            output_str = "Tal til kalibrering = {}, {}, {}, {}, {}, {}, {}, {} " #Definere hvordan en besked skal skrives, i {} kan man indsætte ord eller tal
            print(output_str.format(list1[0], list1[1], list1[2], list1[3], list1[4], list1[5], list1[6], list1[7])) #Printer beskeden skrevet henover men med tal i {}
            
            ax = ((Kx1-Kx2)/(Bx1-Bx2)) #Udregner ax
            bx = ((-Bx2*Kx1+Kx2*Bx1)/(Bx1-Bx2)) #Udregner bx
            ay = ((Ky1-Ky2)/(By1-By2)) #Udregner ay
            by = ((-By2*Ky1+Ky2*By1)/(By1-By2)) #Udregner by
            
            output_str = "ax = {}, bx = {}, ay = {} og by = {}" #Definere hvordan en besked skal skrives, i {} kan man indsætte ord eller tal
            print(output_str.format(ax, bx, ay, by)) #Printer beskeden henover men med ax, bx, ay, by i {}
            
            Calibrated = 1 #Sætter Calibrated til 1 så man kan bruge transform
            
            print("Kalibrering ok")
        elif msg == (transform):
            if Calibrated != 0:    #Kører kun programmet videre hvis kameraret er blevet kalibreret
                CamXPos = float(input("Kamera x-position: "))
                CamYPos = float(input("Kamera y-position: "))
                
                XKoordinat = ax*CamXPos+bx #Finder x-koordinaten til robotten
                YKoordinat = ay*CamYPos+by #Finder y-koordinaten til robotten
                
                print("Klodsens koordinater til robotten er: (", XKoordinat, ";", YKoordinat, ")")
            else:
                print("[ERROR] The camera is not calibrated. Calibrate the camera by typing 'calib'!")
        
        elif msg.startswith(antal):
            m = msg.split(" ")
            if len(m) > 1: #Finder ud af om der står noget efter antal
                antal1 = int(m[1]) #Sætter antal til det tal som der står efter antal
            else:
                print(antal1) #Hviser hvad antal er
        
        elif msg == (complete):
            antal1 = antal1 + 1 #Lægger 1 til antal
            print("Robotten har rykket",antal1,"klods(er).")
        
        elif msg == (AutoMove):
            if Calibrated != 0:
                if(rtd.program_state == 1.0):
                    print("[ROBOT] Leder efter klods")
                    cx,cy,v = cam.analyze() 
                    XKoordinat = ax*cx+bx
                    YKoordinat = ay*cy+by
                    XKoordinat = XKoordinat/1000
                    YKoordinat = YKoordinat/1000
                    a = float(v)
                    a = a*2*math.pi/360
                    z = 280/1000
                    robot.open_gripper() #Åbner griberen
                    while(rtd.program_state == 1.0):
                        time.sleep(0.1) #Får programmet til at vente
                    while(rtd.program_state == 2.0):
                        time.sleep(0.1) #Får programmet til at vente
                    robot.move_xyza(XKoordinat,YKoordinat,z,a) #Flytter robotten til en bestemt position og griberen drejet til en bestemt vinkel
                    print("[ROBOT] Flytter til: ",XKoordinat,YKoordinat,z," med drejer griberen til: ",a)
                    while(rtd.program_state == 1.0):
                        time.sleep(1) #Får programmet til at vente
                    while(rtd.program_state == 2.0):
                        time.sleep(1) #Får programmet til at vente
                    z = -196.55/1000
                    robot.move_relative_z(z) #Flytter robotten med en given længde op eller ned
                    print("[ROBOT] Sænker ned til klodsen" )
                    while(rtd.program_state == 1.0):
                        time.sleep(1) #Får programmet til at vente
                    while(rtd.program_state == 2.0):
                        time.sleep(1) #Får programmet til at vente
                    robot.close_gripper() #Lukker griberen
                    print("[ROBOT] Lukker griberen")
                    while(rtd.program_state == 1.0):
                        time.sleep(0.1) #Får programmet til at vente
                    while(rtd.program_state == 2.0):
                        time.sleep(0.1) #Får programmet til at vente
                    z = 196.55/1000
                    robot.move_relative_z(z) #Flytter robotten med en given længde op eller ned
                    print("[ROBOT] Løfter klodsen op")
                    while(rtd.program_state == 1.0):
                        time.sleep(1) #Får programmet til at vente
                    while(rtd.program_state == 2.0):
                        time.sleep(1) #Får programmet til at vente
                    x = 200/1000
                    y = -150/1000
                    z = 0/1000
                    robot.move_relative_xyz(x,y,z) #Flytter robotten
                    print("[ROBOT] Flytter klodsen med: ",x,y,z)
                    while(rtd.program_state == 1.0):
                        time.sleep(1)
                    while(rtd.program_state == 2.0):
                        time.sleep(1)
                    z = -196.55/1000
                    robot.move_relative_z(z)
                    print("[ROBOT] Sænker klodsen")
                    while(rtd.program_state == 1.0):
                        time.sleep(1)
                    while(rtd.program_state == 2.0):
                        time.sleep(1)
                    robot.open_gripper()
                    print("[ROBOT] Åbner griberen")
                    while(rtd.program_state == 1.0):
                        time.sleep(0.1)
                    while(rtd.program_state == 2.0):
                        time.sleep(0.1)
                    robot.move_home()
                    print("[ROBOT] Tager hjem")
                    antal1 = antal1 + 1 #Lægger 1 til antal
                    print("[ROBOT] Jeg har rykket",antal1,"klods(er)")
            
            else:
                print("[WARNING] Du skal kalibrerer kameraet før du kan bruge denne kommando!")
                    
        else:
            print("[ERROR] "+msg, "is an unknown command. Type 'help' to get a list og commands.")
        
    except Exception as e:
        print(e)
        print("[ERROR] Except was runned! Check your code!!!")
        
print("Tak for nu")