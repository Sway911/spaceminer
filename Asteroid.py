import pygame
from gameSettings import *

class Asteroid():
    def __init__(self,image,position:tuple,splitSize,scaleSize) -> None:
        self.postition=position
        self.image = image        
        self.splitSize = splitSize
        self.scaleSize = scaleSize
        self.asHitbox = pygame.rect.Rect(position[0],position[1],self.image.get_rect().width*self.scaleSize,self.image.get_rect().height*self.scaleSize)
        self.oriantation = 0
        self.materailComp = {"rock": 20, "iron":20,"silicon":10}

    def draw(self,surf):
        tempImg = pygame.transform.scale(self.image,(self.asHitbox.width,self.asHitbox.height))
        surf.blit(tempImg,(self.asHitbox.centerx,self.asHitbox.centery))

    def rotate(self):
        pass

    def returnComp(self):
        return self.materailComp    
    
