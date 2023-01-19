import pygame
from gameSettings import *

class Asteroid():
    def __init__(self,image,position:tuple,splitSize,scaleSize) -> None:
        self.postition=position
        self.image = image        
        self.asHitbox = pygame.rect.Rect(position[0],position[1],0,0)
        self.oriantation = 0
        self.splitSize = splitSize
        self.scaleSize = scaleSize
        self.materailComp = {"rock": 20, "iron":20,"silicon":10}

    def draw(self,surf):
        surf.blit(self.image,(self.asHitbox.centerx,self.asHitbox.centery))

    def rotate(self):
        pass

    def returnComp(self):
        return self.materailComp    
    
