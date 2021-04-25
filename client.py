import socket
import sys
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.19', 4444))

class sendthis():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    x = 0
    y = 0

while True:
    data = s.recv(89)
    data = pickle.loads(data)

    print("Enemy position: ", data.x, data.y)
