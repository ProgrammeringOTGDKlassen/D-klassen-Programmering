import socket

class Robot_programmer():

    def __init__(self):
        #Socket til at sende kommandoer til robotten
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.settimeout(10)
        self.connected = False

    def connect(self, ip='10.130.58.13', simulate=False):
        self.TCP_IP = ip
        TCP_PORT = 30002
        BUFFER_SIZE = 1024

        if not simulate:
            try:
                print("robot Opening IP Address" + self.TCP_IP)
                self.s.connect((self.TCP_IP, TCP_PORT))
                response = self.s.recv(BUFFER_SIZE)
                self.connected = True
            except socket.error:
                print("Socket error")
                self.connected = False
                self.s.close()
        else:
            self.connected = False

    def move_home(self):
        if self.connected:
            #Prædefineret home-position:
            #(Når vi skal sende en streng til robotten,
            # skal den konverteres til et bytearrayself.
            # derfor står der b' foran strengen.)
            self.s.send(b'  movej([0,-1.5708, 1.5708, -1.5708, -1.5708, 0])\n')
    
    def move_xyza(self, x, y, z, rz):
        if self.connected:
            self.s.send(b'def myProg():\n')
            self.s.send(b'  var_1=get_actual_tcp_pose()\n')
            st = '  var_1[0] = {}\n'.format(x)
            self.s.send(bytearray(st,'utf8'))
            st = '  var_1[1] = {}\n'.format(y)
            self.s.send(bytearray(st,'utf8'))
            st = '  var_1[2] = {}\n'.format(z)
            self.s.send(bytearray(st,'utf8'))
            st = '  l = [3.14,0,{}] \n'.format(rz)
            self.s.send(bytearray(st,'utf8'))
            self.s.send(b' aa= rpy2rotvec(l)\n')
            self.s.send(b' var_1[3] = aa[0]\n')
            self.s.send(b' var_1[4] = aa[1]\n')
            self.s.send(b' var_1[5] = aa[2]\n')
            self.s.send(b'  movel(var_1)\n')
            self.s.send(b'end\n')      
              
    def send_curve(self, x, y, z):
        if self.connected:
            self.s.send(b'def myProg():\n')
            for i in range(len(x)):
                self.s.send(b'  var_1=get_actual_tcp_pose()\n')
                st = '  var_1[0] = {}\n'.format(float(x[i])/1000)
                self.s.send(bytearray(st,'utf8'))
                st = '  var_1[1] = {}\n'.format(float(y[i])/1000)
                self.s.send(bytearray(st,'utf8'))
                st = '  var_1[2] = {}\n'.format(z/1000)
                self.s.send(bytearray(st,'utf8'))
                self.s.send(b'  movel(var_1)\n')            
            self.s.send(b'end\n')
            
            
    def move_xyz(self, x, y, z):
        if self.connected:
            #Når vi skal sende en streng til robotten, 
            # skal den konverteres til et bytearrayself.
            # derfor står der b' foran strengen.
            self.s.send(b'def myProg():\n')
            #Vi læser robottens aktuelle konfiguration,
            # for at genbruge rotationen.
            self.s.send(b'  var_1=get_actual_tcp_pose()\n')
            st = '  var_1[0] = {}\n'.format(x)
            # Hvis vi har indsat en værdi i strengen
            # med format, skal strengen konverteres
            # til et bytearray, før den sendes til robotten.
            self.s.send(bytearray(st,'utf8'))
            st = '  var_1[1] = {}\n'.format(y)
            self.s.send(bytearray(st,'utf8'))
            st = '  var_1[2] = {}\n'.format(z)
            self.s.send(bytearray(st,'utf8'))
            self.s.send(b'  movel(var_1)\n')
            self.s.send(b'end\n')


    def open_gripper(self):
        TCP_PORT = 29999
        BUFFER_SIZE = 1024
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        try:
        	print("Opening IP Address" + self.TCP_IP)
        	s.connect((self.TCP_IP, TCP_PORT))
        	response = s.recv(BUFFER_SIZE)
        except socket.error:
        	print("Socket error")
        	s.close()
        
        
        s.send(b"load /programs/opengrip.urp\n")
        response = s.recv(BUFFER_SIZE)
        print("Response: " + str(response))
        
        s.send(b"play\n")
        response = s.recv(BUFFER_SIZE)
        print("Response: " + str(response))
        
        s.close()
        
    def close_gripper(self):
        TCP_PORT = 29999
        BUFFER_SIZE = 1024
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        try:
        	print("Opening IP Address" + self.TCP_IP)
        	s.connect((self.TCP_IP, TCP_PORT))
        	response = s.recv(BUFFER_SIZE)
        except socket.error:
        	print("Socket error")
        	s.close()
        
        
        s.send(b"load /programs/closegrip.urp\n")
        response = s.recv(BUFFER_SIZE)
        print("Response: " + str(response))
        
        s.send(b"play\n")
        response = s.recv(BUFFER_SIZE)
        print("Response: " + str(response))
        
        s.close()
        
