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

    def CalculateTails(self):
        for p in range(len(self.tails)-1, -1, -1):
            if p == 0:
                self.tails[p].x = self.oldx
                self.tails[p].y = self.oldy
            else:
                self.tails[p].x = self.tails[p-1].x;
                self.tails[p].y = self.tails[p-1].y;

    def MoveHead(self, d):
        if d.x != 0:
            x = self.x + d.x * 60
            if len(self.tails) > 0:
                if x != self.tails[0].x:
                    self.oldx = self.x
                    self.oldy = self.y
                    self.x += d.x * 60
                    self.CalculateTails()
            else:
                self.x += d.x * 60
        elif d.y != 0:
            y = self.y + d.y * 60
            if len(self.tails) > 0:
                if y != self.tails[0].y:
                    self.oldx = self.x
                    self.oldy = self.y
                    self.y += d.y * 60
                    self.CalculateTails()
            else:
                self.y += d.y * 60

    def CheckSnakeCollides(self):
        if len(self.tails) == 0:
            return False
    
        for t in self.tails:
            if t.x == self.x and t.y == self.y:
                return True

    def EatFeed(self, feed):
        if self.x == feed.x and self.y == feed.y:
            feed.x = -100 ## place feed somewhere out of screen
            feed.y = -100
            self.SpawnTail()
            return True
        else:
            return False

    def DrawSnake(self):
        for t in self.tails:
            pygame.draw.rect(screen, (255,0,0), pygame.Rect((t.x, t.y), (SNAKEBLOCKSIZE-10, SNAKEBLOCKSIZE-10)))
        pygame.draw.rect(screen, (0,255,0), pygame.Rect((self.x, self.y), (SNAKEBLOCKSIZE-10, SNAKEBLOCKSIZE-10)))

    
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
feed = pygame.Vector2(0,0) 
###

snake = Snake(180,60)

def SpawnFeed():
    r1 = WIDTH / SNAKEBLOCKSIZE
    r2 = HEIGHT / SNAKEBLOCKSIZE
    x = random.randrange(0, r1) * 60
    y = random.randrange(0, r2) * 60
    feed.x = x
    feed.y = y

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
            #MoveHead(dir)
            #EatFeed()

            snake.MoveHead(dir)
            if snake.EatFeed(feed):
                SpawnFeed()
            
    screen.fill((0,0,0))
    snake.DrawSnake()

    if snake.CheckSnakeCollides():
        print("Game Over!")
        sys.exit()
    

    ## Draw feed
    pygame.draw.rect(screen, (10,100,110), pygame.Rect((feed.x, feed.y), (60-10, 60-10)))


    pygame.display.flip()
