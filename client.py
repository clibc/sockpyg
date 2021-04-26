import networking

s = networking.Server('192.168.1.15', 4444, False)

while True:
    data = s.Receive(1000)
    string = input("You:")
    s.Send(string)
