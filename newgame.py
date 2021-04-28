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

class SnakePart:
    def __init__(self, x, y):
        self.x = x
        self.y = y

CurrentDir = -1
player_parts = [SnakePart(200,200), SnakePart(261,200)]

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

    if CurrentDir == Directions.UP:
        player_parts[0].y -= 60
    elif CurrentDir == Directions.DOWN:
        player_parts[0].y += 60
    elif CurrentDir == Directions.LEFT:
        player_parts[0].x -= 60
    elif CurrentDir == Directions.RIGHT:
        player_parts[0].x += 60

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0), pygame.Rect((player_parts[0].x, player_parts[0].y), (60, 60)))
    pygame.draw.rect(screen, (255,0,0), pygame.Rect((player_parts[1].x, player_parts[1].y), (60, 60)))
    pygame.display.flip()
    pygame.time.wait(500)
