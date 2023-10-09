import pygame
class obstacle():
    def __init__(self, x, y,height,width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))