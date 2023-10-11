import pygame
from screen import HEIGHT, FLOOR_HEIGHT, FLOOR_START

class Obstacle():
    def __init__(self, x, y,height,width,color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color=color


    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x+FLOOR_START, HEIGHT-FLOOR_HEIGHT-self.y-self.height, self.width, self.height))