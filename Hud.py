import pygame
from gameSettings import *

class Hud():
    def __init__(self,frameRectangle) -> None:
        self.width = WIDTH
        self.height = 80
        self.color = GREEN
        # self.frame = pygame.rect.Rect(0,0,self.width,self.height)
        self.frame = frameRectangle
        self.thick = 3

    def drawHudFrame(self,screen):
        pygame.draw.rect(screen,self.color,self.frame,self.thick)

if __name__ == "__main__":
    print("running as script")

