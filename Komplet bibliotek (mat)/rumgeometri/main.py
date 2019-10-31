from rTData import RTData
from rumgeom import *

# ip1: 10.130.58.11
# ip2: 10.130.58.12
# ip3: 10.130.58.13
# ip4: 10.130.58.14

data = RTData()

data.connect("10.130.58.11")
print(data.qtarget)
print(data.qdtarget)
print(data.qddtarget)
print(data.qactual)
print(data.tool_frame)
#data.perform_task("hh")

while True:
    s = input("Enter a command: ")
    args = s.split(" ")
    data.perform_task(s)
    if args[0].lower() == "stop":
        data.send_command(s)
    elif args[0].lower() == "play":
        data.perform_task(args[1])
def get_tool_pose():
    #Vi skal fucking have dem her
    k_x = 0
    k_y = 0
    k_z = 0
    data = 0
