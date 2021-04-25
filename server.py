import socket, pickle, sys, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.19', 1111))

s.listen(1)

class sendthis():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    x = 0
    y = 0

while True:
    conn,addr = s.accept()
    s = sendthis(10,10)
    while True:
        serialized = pickle.dumps(s) 
        s.x += 1
        s.y += 1
        conn.send(serialized)
        data = conn.recv(89)
        data = pickle.loads(data)

        s = data
        print("data come in :", data.x, data.y)
        time.sleep(0.01)


conn.close()
