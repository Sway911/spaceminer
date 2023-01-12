import pygame


class Ship():
    def __init__(self,image):
        self.position = (200,500)
        self.direction = 0
        self.current_speed = 0
        self.max_speed = 100
        self.fuel_capacity = 100
        self.image = image
        self.hitbox = pygame.Rect(0,0,0,0)
        self.rotImage = image

    def draw(self,surf):
        pass

    def rotate(self,nudge):
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