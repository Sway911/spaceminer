import pygame
import math
from gameSettings import *

class Ship():
    def __init__(self,image):     
        self.direction = 0
        self.position = pygame.Vector2((float(WIDTH/2),float(HEIGHT/2)))
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
        #delta time adjustmets for varios actions
        self.adjustmentSpeed = 30   # sets base multiplyer during delta time
        self.thrusterBaseSpeed=2    

    def draw(self,surf:pygame.display):
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
        # print(self.direction)

    def propultion_forward_thruster(self,dt):
        if self.thruster<100:
            self.thruster += 1
        
    def propultion_backward_thruster(self,dt):
        if self.thruster>0:
            self.thruster-=1
    
    def shipSlip(dt,slipAmount):
        #get direction and get new point 90 degrees away
        #increment position value
        #reassign rounded rectangle position value
        pass

    #gets new position and adjusts by delta time and then further adjust to get constant speed percentage of thruster speed
    def propell_ship(self,dt):
        newPosition = (math.sin(math.radians(self.direction)),math.cos(math.radians(self.direction)))
        if self.thruster != 0:
            self.position.x += newPosition[0]*dt*(self.adjustmentSpeed*self.thruster/100)
            self.position.y += newPosition[1]*dt*(self.adjustmentSpeed*self.thruster/100)
            self.hitbox.x = round(self.position.x,0)
            self.hitbox.y = round(self.position.y,0)
            
