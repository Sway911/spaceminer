import pygame
from gameSettings import *

class Asteroid():
    def __init__(self,image,position:tuple,splitSize,scaleSize) -> None:        
        self.postition = pygame.Vector2((position[0],position[1]))
        self.image = image        
        self.splitSize = splitSize
        self.scaleSize = scaleSize
        self.image_rectangle = self.image.get_rect()
        self.asHitbox = pygame.rect.Rect(self.postition.x,self.postition.y,self.image_rectangle.width*self.scaleSize,self.image_rectangle.height*self.scaleSize)
        self.oriantation = 0
        self.materailComp = {"rock": 20, "iron":20,"silicon":10}

    def draw(self,surf):
        tempImg = pygame.transform.scale(self.image,(self.asHitbox.width,self.asHitbox.height))
        surf.blit(tempImg,(self.asHitbox.x,self.asHitbox.y))
        pygame.draw.rect(surf,WHITE,self.asHitbox,1,1)

    def rotate(self):
        pass

    def returnComp(self):
        return self.materailComp    
    
    def checkMouseClickCollition(self,mousePos):
        return self.asHitbox.collidepoint(mousePos)
