import socket, pickle, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.19', 4444))

s.listen(2)

class sendthis():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    x = 0
    y = 0

while True:
    conn,addr = s.accept()
    s = sendthis(10,10)
    #print(sys.getsizeof(serialized))

    while True:
        s.x += 1
        s.y += 1
        serialized = pickle.dumps(s) 
        conn.send(serialized)
