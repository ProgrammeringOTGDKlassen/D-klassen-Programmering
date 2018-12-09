from math import sqrt
from robotprogrammer import Robot_programmer
quit = "quit"
help = "help"
sqrt2 = "sqrt 2"
toplusto = "2+2"
seksgangeseks = "6*6"
spurgt = "spurgt"
list1 = [quit, help, sqrt2, toplusto, seksgangeseks, spurgt]
robot = Robot_programmer()
robot.connect("10.130.58.11",False)

while True:
    try:
        msg = input("Skriv her > ")
        if not msg:
            break
        if msg.startswith("home"):
            robot.move_home()
        if msg.startswith("move"):
            robot.move_xyz(-0.489, -0.69, 0.724)

        if msg.startswith(quit):
            break
        if msg.startswith("s"):
            break
        #elif msg.startswith(help):
        #    print("Kommandoer til rådighed:")
        #    print(list1)
        #elif msg.startswith(sqrt2):
        #    print(sqrt(2))
        #elif msg.startswith(toplusto):
        #    print(2+2)
        #elif msg.startswith(seksgangeseks):
        #    print(6*6)
        #elif msg.startswith(spurgt):
        #    print("Du bliver nu smidt ud af programmet!")
        #    break
        else:
            print("Du skrev: "+str(msg)+". Skriv "+help+" for at se hvilke kommandoer du har til rådighed")
    except:
        break
        
print("Tak for nu")