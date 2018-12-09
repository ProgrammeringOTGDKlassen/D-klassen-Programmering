from robotprogrammer import Robot_programmer
robot = Robot_programmer()

#robot.connect("10.130.58.11",False)

while(True):
    try:
        msg = input("Skriv her > ")
        if not msg:
            break
        
        if msg.startswith(msg):
            #m = msg.split(" ")
            #t1 = float(m[0])
            #t2 = m[1]
            #t3 = float(m[2])
            #output_str = "Summen af {} {} {} er {}"
            #print(output_str.format(m[0], m[1], m[2], t1t2t3))
            print(eval(msg))
    except:
        pass
        
print("Tak for nu")