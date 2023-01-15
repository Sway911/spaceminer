import pygame
import math
from gameSettings import *

class Ship():
    def __init__(self,image):
        self.position = (200,500)
        self.direction = 0
        self.current_speed = 0
        self.max_speed = 100
        self.fluel_level=100
        self.fuel_capacity = 100
        self.cargo_level=100
        self.cargo_capacity = 100
        self.image = image
        self.hitbox = pygame.Rect(WIDTH/2,HEIGHT/2,0,0)        
        self.rotImage = image
        self.thruster = 0
        self.accelatare_capacity=2

    def draw(self,surf):
        # surf.blit
        # surf.blit(self.rotImage,(20,30))
        surf.blit(self.rotImage,(self.hitbox.centerx,self.hitbox.centery))

    def rotate(self,dt,nudge):
        """
        Control the direction of ship
        """
        if self.direction+nudge < 0:
            self.direction = 360
        
        if self.direction+nudge > 360:
            self.direction = 0
            
        self.direction+=nudge
        self.rotImage = pygame.transform.rotate(self.image,self.direction)
        print(self.direction)

    def propultion_thruster(self):
        pass

    def propell_ship(self):
        newPosition = (round(math.sin(math.radians(self.direction)),0),round(math.cos(math.radians(self.direction)),0))
        if self.thruster != 0:
            self.hitbox.x += newPosition[0]
            self.hitbox.y += newPosition[1]
        print(newPosition)
