import pygame
import math
from gameSettings import *

class Ship():
    def __init__(self,image):
        
        self.positionx = float(WIDTH/2)
        self.positiony = float(HEIGHT/2)
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
        self.adjustmentSpeed = 30

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

    def propell_ship(self,dt):
        newPosition = (math.sin(math.radians(self.direction)),math.cos(math.radians(self.direction)))
        if self.thruster != 0:
            self.positionx += newPosition[0]*dt*self.adjustmentSpeed
            self.positiony += newPosition[1]*dt*self.adjustmentSpeed
            # self.hitbox.x += round(newPosition[0]*dt,0)
            # self.hitbox.y += round(newPosition[1]*dt,0)
            self.hitbox.x = round(self.positionx,0)
            self.hitbox.y = round(self.positiony,0)
        print(f"just pos {newPosition[0]},{newPosition[1]}")
        print(f"with dt {newPosition[0]*dt},{newPosition[1]*dt}")
        print(f"with dt with round {round(newPosition[0]*dt)},{round(newPosition[1]*dt)}")
        # print(self.hitbox.x,self.hitbox.y)
