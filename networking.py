import socket, pickle, sys, time

class Server:
    def __init__(self, ip_addr, port, isServer):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip_addr = ip_addr
        self.port = port
        self.isServer = isServer
        
        if isServer==True:
            self.socket.bind((self.ip_addr, self.port))
            self.socket.listen(1)
            self.conn, self.addr = self.socket.accept()
        else:
            self.socket.connect((ip_addr, port))
            
            
    def Send(self,data):
        serialized = pickle.dumps(data)
        
        if self.isServer==True:
            self.conn.send(serialized)
        else:
            self.socket.send(serialized)
        
        time.sleep(0.1)
        
    def Receive(self, size):
        if self.isServer==True:
            data = self.conn.recv(size)
        else:
            data = self.socket.recv(size)
            
        data = pickle.loads(data)
        return data
