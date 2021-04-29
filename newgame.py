import sys, pygame
from enum import Enum

class Directions(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

WIDTH = 500
HEIGHT = 500
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Head:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.oldx = 0
        self.oldy = 0

class Tail:
    def __init__(self, x, y, isHead = False):
        self.x = x
        self.y = y

CurrentDir = -1
head = Head(200,200)
tails = [Tail(260,200), Tail(320,200), Tail(380,200)]

def CalculateTails():
    for p in range(len(tails)-1, -1, -1):
        if p == 0:
            tails[p].x = head.oldx
            tails[p].y = head.oldy
        else:
            tails[p].x = tails[p-1].x;
            tails[p].y = tails[p-1].y;

def MoveHead(direction):
    x = head.x + direction.x * 60
    y = head.y + direction.y * 60

    head.oldx = head.x
    head.oldy = head.y

    if x != tails[0].x and y != tails[0].y:
        head.x += direction.x * 60
        head.y += direction.y * 60
        return True

    print(x,y, tails[0].x, tails[0].y)
    return False
        
        
        
while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()
        elif(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_a):
                CurrentDir = Directions.LEFT
            if(event.key == pygame.K_d):
                CurrentDir = Directions.RIGHT
            if(event.key == pygame.K_w):
                CurrentDir = Directions.UP
            if(event.key == pygame.K_s):
                CurrentDir = Directions.DOWN

            dir = pygame.Vector2(0,0) 
            if CurrentDir == Directions.UP:
                dir.x = 0
                dir.y = -1
            elif CurrentDir == Directions.DOWN:
                dir.x = 0
                dir.y = 1
            elif CurrentDir == Directions.LEFT:
                dir.x = -1
                dir.y = 0
            elif CurrentDir == Directions.RIGHT:
                dir.x = 1
                dir.y = 0
            if MoveHead(dir):
                CalculateTails()

    screen.fill((0,0,0))



    for t in tails:
        pygame.draw.rect(screen, (255,0,0), pygame.Rect((t.x, t.y), (60, 60)))

    pygame.draw.rect(screen, (0,255,0), pygame.Rect((head.x, head.y), (60, 60)))
        

    pygame.display.flip()
