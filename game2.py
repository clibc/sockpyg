import pygame, sys

import networking

s = networking.Server('192.168.1.15', 4000, False)

pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100

    def MoveLeft(self, val=60):
        self.x -= val
    def MoveRight(self, val=60):
        self.x += val
    def MoveUp(self, val=60):
        self.y -= val
    def MoveDown(self, val=60):
        self.y += val

    def Draw(self):
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(p.x, p.y, 60, 60))

class Bullet:
    x = 0.0
    y = 0.0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
p = Player(200,300)
b = Bullet(0,0)
        
while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()
        elif(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_a):
                p.MoveLeft()
            if(event.key == pygame.K_d):
                p.MoveRight()
            if(event.key == pygame.K_w):
                p.MoveUp()
            if(event.key == pygame.K_s):
                p.MoveDown()

    pos = pygame.mouse.get_pos()
    #print(pos[0], pos[1])

    screen.fill((0,0,0))
    p.Draw()

    p2 = s.Receive(1000)

    pygame.draw.rect(screen, (255,0,0), pygame.Rect(p2.x, p2.y, 60, 60))
    
    s.Send(p)
    
    pygame.display.flip()
