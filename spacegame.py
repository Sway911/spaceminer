import pygame
from pygame.locals import *
import sys
from gameSettings import *
import Ship as ship

pygame.init();

screen = pygame.display.set_mode((WIDTH,HEIGHT))


# 1) basic movement
# 2) rotate movement
# 3) radar System
# 4) asteriod grabber
# 5) basic hud( position, fuel, cargo capacity)
# 6) basic spaceport

# Load assets
spaceship_image = pygame.image.load("C:\pythonapps\pygames\images\\firstspaceship.png").convert()
asteriod_image = pygame.image.load("C:\pythonapps\pygames\images\imgasteriod.png").convert()
shipHitBox = asteriod_image.get_rect()
defaultgamefont = pygame.font.SysFont("Arial", 18)

myShip = ship.Ship(spaceship_image)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            keypressed = pygame.key.get_pressed()
            if keypressed[K_a]:
                # spaceship_image = pygame.transform.rotate(spaceship_image,180)
                myShip.rotate(-1)                
            if keypressed[K_d]:
                myShip.rotate(1)
            if keypressed[K_s]:
                pass
            if keypressed[K_w]:
                pass

    # keypressed = pygame.key.get_pressed()    
    # if keypressed[K_a]:
    #     spaceship_image = pygame.transform.rotate(spaceship_image,180)
    # if keypressed[K_d]:
    #     pass
    screen.fill(BLACK)
    
    screen.blit(spaceship_image,(20,30))
    screen.blit(asteriod_image,(260,100))
    screen.blit(asteriod_image,(190,200))
    screen.blit(asteriod_image,(100,40))
    
    screen.blit(myShip.rotImage,myShip.position)

    imageRecDetails = defaultgamefont.render(f'Ship Image centre: {shipHitBox.center} Height:{shipHitBox.height} Width:{shipHitBox.width}',False,WHITE)
    screen.blit(imageRecDetails,(300,300))
    rotatedRectangleOfShip= myShip.image.get_rect()
    rotatedImageRecDetails = defaultgamefont.render(f'Rotating Image centre: {rotatedRectangleOfShip.center} Height:{rotatedRectangleOfShip.height} Width:{rotatedRectangleOfShip.width}',False,WHITE)
    screen.blit(rotatedImageRecDetails,(300,340))
    rotatedImageRecPosDetails = defaultgamefont.render(f'Rotating Image X: {rotatedRectangleOfShip.x} Y:{rotatedRectangleOfShip.y} ',False,WHITE)
    screen.blit(rotatedImageRecPosDetails,(300,360))

    pygame.display.update()