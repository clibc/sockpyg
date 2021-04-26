import networking

s = networking.Server('192.168.1.15', 4444, True)

while True:
    string = input("You:")
    s.Send(string)
    data = s.Receive(1000)
    print("Other: ", data)
