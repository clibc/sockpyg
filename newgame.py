import sys, pygame, random
from enum import Enum

class Directions(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

WIDTH = 1080
HEIGHT = 840
SNAKEBLOCKSIZE = 60
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.oldx = 0
        self.oldy = 0
        self.tails = []

    def SpawnTail(self):
        self.tails.append(Tail(-100, -100))

    def CalculateTails():
        for p in range(len(self.tails)-1, -1, -1):
            if p == 0:
                self.tails[p].x = head.oldx
                self.tails[p].y = head.oldy
            else:
                self.tails[p].x = tails[p-1].x;
                self.tails[p].y = tails[p-1].y;

    
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

####
CurrentDir = -1
head = Head(180,60)
tails = []
feed = pygame.Vector2(0,0) 
###

def SpawnFeed():
    r1 = WIDTH / SNAKEBLOCKSIZE
    r2 = HEIGHT / SNAKEBLOCKSIZE
    x = random.randrange(0, r1-1) * 60
    y = random.randrange(0, r2-2) * 60
    feed.x = x
    feed.y = y

def SpawnTail():
    tails.append(Tail(-100, -100))

def CalculateTails():
    for p in range(len(tails)-1, -1, -1):
        if p == 0:
            tails[p].x = head.oldx
            tails[p].y = head.oldy
        else:
            tails[p].x = tails[p-1].x;
            tails[p].y = tails[p-1].y;

def MoveHead(d):
    if d.x != 0:
        x = head.x + d.x * 60
        if len(tails) > 0:
            if x != tails[0].x:
                head.oldx = head.x
                head.oldy = head.y
                head.x += d.x * 60
                CalculateTails()
        else:
            head.x += d.x * 60
    elif d.y != 0:
        y = head.y + d.y * 60
        if len(tails) > 0:
            if y != tails[0].y:
                head.oldx = head.x
                head.oldy = head.y
                head.y += d.y * 60
                CalculateTails()
        else:
            head.y += d.y * 60

def CheckSnakeCollides():
    if len(tails) == 0:
        return False
    
    for t in tails:
        if t.x == head.x and t.y == head.y:
            return True
            
def EatFeed():
    if head.x == feed.x and head.y == feed.y:
        feed.x = -100 ## place feed somewhere out of screen
        feed.y = -100
        SpawnTail()
        SpawnFeed()
        
def DrawSnake():
    for t in tails:
        pygame.draw.rect(screen, (255,0,0), pygame.Rect((t.x, t.y), (SNAKEBLOCKSIZE-10, SNAKEBLOCKSIZE-10)))
    pygame.draw.rect(screen, (0,255,0), pygame.Rect((head.x, head.y), (SNAKEBLOCKSIZE-10, SNAKEBLOCKSIZE-10)))


SpawnFeed()
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
            MoveHead(dir)
            EatFeed()

    screen.fill((0,0,0))
    DrawSnake()

    if CheckSnakeCollides():
        print("Game Over!")
        sys.exit()
    

    ## Draw feed
    pygame.draw.rect(screen, (10,100,110), pygame.Rect((feed.x, feed.y), (60-10, 60-10)))


    pygame.display.flip()
