import pygame, sys

pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def Draw_Player(p):
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(p.x, p.y, 60, 60))

class Player:
    x = 0.0
    y = 0.0
    health = 0
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
    

p = Player(200,300)
        
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
                
    screen.fill((0,0,0))
    Draw_Player(p)
    pygame.display.flip()

