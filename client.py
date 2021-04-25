import socket, sys, pickle, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.19', 1111))

class sendthis():
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

while True:
    data = s.recv(89)
    data = pickle.loads(data)
    print("Enemy position: ", data.x, data.y)
    data.x += 1
    data.y += 1
    s.send(pickle.dumps(data))
    time.sleep(0.01)
    
s.close()
