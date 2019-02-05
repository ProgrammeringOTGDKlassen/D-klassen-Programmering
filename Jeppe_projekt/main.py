from robotprogrammer import Robot_programmer
from rTData import RTData
import time
spip = '10.130.58.13'
simulate = False
doc = open("Positioner.txt","a+")
robot = Robot_programmer()
robot.connect('10.130.58.13' , False)

rtd = RTData()
rtd.connect('10.130.58.13' , False)

# Alt skal noteres i meter ikke andre enheder ellers skal der regnes om til meter enheden
#ventetid
tid = 5
#Startspunkter
xs = -525.8/1000
ys = -483.5/1000
zs = 99.4/1000
# kvadrater
x = 0.001/1000
y = 5/1000
z = 5/1000
# Nettet
x1 = 0.001/1000
y1 = 50/1000
z1 = 50/1000


pt = [x,y,z]
net = [x1,y1,z1]

xm = int(net[0]/pt[0])
ym = int(net[1]/pt[1])
zm = int(net[2]/pt[2])
print(rtd.program_state)
for a in range(0,xm):
	for b in range(0,ym):
		for c in range(0,zm):
			if rtd.program_state == 1:
				robot.move_xyz(xs+pt[0]*a,ys+pt[1]*b,zs+pt[2]*c)
				xpos = xs+pt[0]*a
				ypos = ys+pt[1]*b
				zpos = zs+pt[2]*c
				doc.write("[{},{},{}]\n".format(xpos,ypos,zpos))
			while rtd.program_state == 1:
				time.sleep(1)
			while rtd.program_state == 2:
				time.sleep(1)
			if rtd.program_state == 1:
				time.sleep(tid)
				
time.sleep(5)
rtd.disconnect()
time.sleep(5)