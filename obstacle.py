import pygame
from screen import HEIGHT, FLOOR_HEIGHT, FLOOR_START

class Obstacle():
    def __init__(self, x, y,height,width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width


    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x+FLOOR_START, HEIGHT-FLOOR_HEIGHT-self.y-self.height, self.width, self.height))