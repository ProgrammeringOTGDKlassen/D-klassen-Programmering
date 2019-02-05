import math
import matplotlib.pyplot as plt
from robotprogrammer import Robot_programmer
from rTData import RTData

IP = "10.130.58.13"


robot = Robot_programmer()
robot.connect(IP, False)
rtd = RTData()
rtd.connect(IP, False)


def wait(s=2):
    while rtd.program_state == s:
        pass


def lenChecker(first, list1, l):
    list1.remove(first)
    while len(list1) != l:
        print("Der er ikke {} informationer!".format(l))
        command = input("Skriv informationerne: ")
        list1 = command.split()
    return list1


def status(x=False):
    stat = rtd.program_state
    if x:
        print(stat)
    return stat


def position(x=False):
    pos = rtd.tool_frame
    if x:
        print(pos)
    return pos


def configuration(x=False):
    conf = rtd.qactual
    if x:
        print(conf)
    return conf


def move(x, y, z):
    x = float(x)/1000
    y = float(y)/1000
    z = float(z)/1000
    stat = status()
    if stat == 1:
        robot.move_xyz(x, y, z)
    elif stat == 0:
        print("Robotten er ikke forbundet!")
    else:
        print("Robotten er i bevægelse")


def moveA(x, y, z, rz):
    x = float(x)/1000  # 0.3
    y = float(y)/1000  # 0.5
    z = float(z)/1000  # 0.02
    rz = float(rz)  # 3
    rz = rz*2*math.pi/360

    stat = status()
    if stat == 1:
        # sender informationerne til robotten, så det bliver udført
        robot.move_xyza(x, y, z, rz)
    elif stat == 0:
        print("Robotten er ikke forbundet!")
    else:
        print("Robotten er i bevægelse")


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


def open_gripper():
    stat = status()
    if stat == 1:
        robot.open_gripper()
    elif stat == 0:
        print("Robotten er ikke forbundet!")
    else:
        print("Robotten er i bevægelse")


def close_gripper():
    stat = status()
    if stat == 1:
        robot.close_gripper()
    elif stat == 0:
        print("Robotten er ikke forbundet!")
    else:
        print("Robotten er i bevægelse")


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


# Eksempel:
# xs = [1, 2, 3, 4, 5, 6]
# ys = [1, 4, 9, 16, 25, 36]
# plt.plot(xs,ys, 'b*')
# plt.xlabel("x")
# plt.ylabel("y=x^2")
# plt.title("Plot of y=x^2")
# plt.show()


while True:
    try:
        ready = False
        msg = input("\nSkriv her: ")

        if not msg:
            break

        elif msg.startswith("q"):
            break

        elif msg.startswith("home"):
            robot.move_home()

        elif msg.startswith("start"):
            if ready:
                robot.move_home()
                wait(1)
                wait()
                pass

        else:
            print("\nDu skrev " + str(msg))
    except Exception as e:
        print(e)
        break
rtd.disconnect()
print("Tak for nu")
