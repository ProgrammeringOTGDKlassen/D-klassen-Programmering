import time
import struct
import threading
import socket
from math import sin
import time

class RTData():
    def __init__(self):
        self.connected = False
        self.fmt = '>Q'
        for i in range(132):
            self.fmt += 'd'
        self.s = None
        self.package_size = 0
        self.time = 0
        self.qtarget = [0,0,0,0,0,0]
        self.qdtarget = [0,0,0,0,0,0]
        self.qddtarget = [0,0,0,0,0,0]
        self.qactual = [0,0,0,0,0,0]
        self.tool_frame = [0,0,0,0,0,0]
        self.program_state = 0
        self.thread = threading.Thread(target=self.read)

    def connect(self, ip, simulate=False):
        TCP_IP = ip
        TCP_PORT = 30003
        BUFFER_SIZE = 1060

        self.simulate = simulate

        if not self.simulate:

            if not self.connected:
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.settimeout(10)
                try:
                    print("Opening IP Address" + TCP_IP)
                    self.s.connect((TCP_IP, TCP_PORT))
                    response = self.s.recv(BUFFER_SIZE)
                    self.connected = True
                except socket.error:
                	 print("Socket error")
                	 self.s.close()
        else:
            self.connected = True

        if self.connected:
            self.thread.start()

    def disconnect(self):
        if self.connected:
            print('Stopping thread')
            self.connected = False
            if self.s is not None:
                self.s.close()
            time.sleep(1)
            print('Thread stopped')


    def read(self):

        if not self.simulate:
            while self.connected :
                BUFFER_SIZE = 1060
                response = self.s.recv(BUFFER_SIZE)
                self.parse_message(response)
        else:
            while self.connected:
                self.time += 1
                time.sleep(0.05)
                self.qactual[0] = 360*sin(self.time*0.05)
        print('Thread finished')


    def parse_message(self, data):
        data = b'\x00\x00\x00\x00' + data
        #print('fmt: '+fmt)
        #print('len: ' + str(len(data)))
        if len(data) == 1064:
            #print(time.time())
            t = struct.unpack(self.fmt, data)
            #print(t)

            self.package_size = t[0]
            self.time = t[1]
            self.qtarget = []
            self.qdtarget = []
            self.qddtarget = []
            self.qactual = []
            self.tool_frame = []
            for i in range(2,8):
                self.qtarget.append(t[i])
            self.qdtarget = []
            for i in range(8,16):
                self.qdtarget.append(t[i])
            self.qddtarget = []
            for i in range(16,24):
                self.qddtarget.append(t[i])
            self.qactual = []
            for i in range(32,38):
                self.qactual.append(t[i])
            self.tool_frame = []
            for i in range(56,62):
                self.tool_frame.append(t[i])
            self.program_state = t[-1]

            #out_file = open("data.bin", "wb") # open for [w]riting as [b]inary
            #out_file.write(data)
            #out_file.close()
