import pygame
from pygame.locals import *
import sys
from gameSettings import *
import Ship as ship
import Hud as hud
import time

pygame.init();

screen = pygame.display.set_mode((WIDTH,HEIGHT))


# 1) basic movement
# 2) rotate movement
# 3) radar System
# 4) asteriod grabber
# 5) basic hud( position, fuel, cargo capacity)
# 6) basic spaceport

# Load assets
spaceship_image = pygame.image.load("C:\pythonapps\spaceminer\images\\firstspaceship.png").convert()
asteriod_image = pygame.image.load("C:\pythonapps\spaceminer\images\imgasteriod.png").convert()

defaultgamefont = pygame.font.SysFont("Arial", 18)
menuFont = pygame.font.SysFont("Arial", 18)
fontHeight=18

myShip = ship.Ship(spaceship_image)
bottomHud = hud.Hud(pygame.rect.Rect(0,HEIGHT-100,WIDTH,100))

#test


previosTime = time.time()

while True:
    dt = previosTime - time.time()
    previosTime = time.time()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            keypressed = pygame.key.get_pressed()            
            if keypressed[K_s]:
                pass
            if keypressed[K_w]:
                pass
            if keypressed[K_SPACE]:
                myShip.thruster=0

    keypressed = pygame.key.get_pressed()    
    if keypressed[K_w]:
        if myShip.thruster<100:
            myShip.thruster+=1
    if keypressed[K_s]:
        if myShip.thruster>0:
            myShip.thruster-=1
    if keypressed[K_d]:
        myShip.rotate(dt,1)
    if keypressed[K_a]:        
        myShip.rotate(dt,-1)   
    
    screen.fill(BLACK)
    
    # screen.blit(spaceship_image,(20,30))
    screen.blit(asteriod_image,(260,100))
    screen.blit(asteriod_image,(190,200))
    screen.blit(asteriod_image,(100,40))
    
    # screen.blit(myShip.rotImage,myShip.position)
    myShip.draw(screen)

    myShip.propell_ship()
    
    # Draws the hud frame
    bottomHud.drawHudFrame(screen)
    # Populates the text on hud frame on left
    hudText1 = menuFont.render(f'Map Size:',False,WHITE)
    screen.blit(hudText1,(20,bottomHud.frame.top))
    hudText2 = menuFont.render(f'Map Sector:',False,WHITE)
    screen.blit(hudText2,(20,bottomHud.frame.top+fontHeight))
    hudText3 = menuFont.render(f'Ship Position: {myShip.hitbox.center}',False,WHITE)
    screen.blit(hudText3,(20,bottomHud.frame.top+fontHeight*2))
    hudText4 = menuFont.render(f'Camera Position:',False,WHITE)
    screen.blit(hudText4,(20,bottomHud.frame.top+fontHeight*3))
    # Populates the text on hud frame on Centre
    hudText10 = menuFont.render(f'ThurstPower: {myShip.thruster}',False,WHITE)
    screen.blit(hudText10,(WIDTH/2-30,bottomHud.frame.top))
    # Populates the text on hud frame on Right
    hudText5 = menuFont.render(f'Speed: {myShip.current_speed}',False,WHITE)
    screen.blit(hudText5,(WIDTH-180,bottomHud.frame.top))
    hudText6 = menuFont.render(f'Direction: {myShip.direction}',False,WHITE)
    screen.blit(hudText6,(WIDTH-180,bottomHud.frame.top+fontHeight))
    hudText7 = menuFont.render(f'Fuel:{myShip.fluel_level}/{myShip.fuel_capacity}',False,WHITE)
    screen.blit(hudText7,(WIDTH-180,bottomHud.frame.top+fontHeight*2))
    hudText8 = menuFont.render(f'Cargo Capacity: {myShip.cargo_level}/{myShip.cargo_capacity}',False,WHITE)
    screen.blit(hudText8,(WIDTH-180,bottomHud.frame.top+fontHeight*3))

    pygame.display.update()