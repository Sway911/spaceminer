import pygame
from pygame.locals import *
import sys
from gameSettings import *
import Ship as ship
import Asteroid as assteriod
import Hud as hud
import time

pygame.init();

screen = pygame.display.set_mode((WIDTH,HEIGHT))


# 1) basic movement, thrusters basic done, rotate basic done, slide still outstanding
# 2) rotate movement, need to recenter image
# 3) select and scan asteriod
# 3) implement momentum for ship
# implement mine and split of asteriod
# 3) radar System first do ping and hit of asteriods
# 4) asteriod grabber
# 5) basic hud( position, fuel, cargo capacity)
# 6) basic spaceport

# Load assets
spaceship_image = pygame.image.load("C:\pythonapps\spaceminer\images\\firstspaceship.png").convert()
asteriod_image = pygame.image.load("C:\pythonapps\spaceminer\images\imgasteriod.png").convert()

defaultgamefont = pygame.font.SysFont("Arial", 18)
menuFont = pygame.font.SysFont("Arial", 18)
fontHeight=18

print(asteriod_image.get_rect().width)

myShip = ship.Ship(spaceship_image)
bottomHud = hud.Hud(pygame.rect.Rect(0,HEIGHT-100,WIDTH,100))
asteriodField1 = []
asteriod1 = assteriod.Asteroid(asteriod_image,(260,100),2,1)
asteriodField1.append(asteriod1)
asteriod2 = assteriod.Asteroid(asteriod_image,(190,200),3,2)
asteriodField1.append(asteriod2)
asteriod3 = assteriod.Asteroid(asteriod_image,(100,40),5,6)
asteriodField1.append(asteriod3)

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

    mousePos = pygame.mouse.get_pos()
    keypressed = pygame.key.get_pressed()

    if keypressed[K_w]:
        myShip.propultion_forward_thruster(dt)
        # if myShip.thruster<100:
        #     myShip.thruster+=1
    if keypressed[K_s]:
        myShip.propultion_backward_thruster(dt)
        # if myShip.thruster>0:
        #     myShip.thruster-=1
    if keypressed[K_d]:
        myShip.rotate(dt,-1)
    if keypressed[K_a]:        
        myShip.rotate(dt,1)
    if keypressed[K_q]:
        myShip.shipSlip(dt,-1)
    if keypressed[K_e]:
        myShip.shipSlip(dt,1)
    
    screen.fill(BLACK)
    
    # screen.blit(spaceship_image,(20,30))
    # screen.blit(asteriod_image,(260,100))
    # screen.blit(asteriod_image,(190,200))
    # screen.blit(asteriod_image,(100,40))
    asteriod1.draw(screen)
    asteriod2.draw(screen)
    asteriod3.draw(screen)
    

    # screen.blit(myShip.rotImage,myShip.position)
    myShip.draw(screen)

    myShip.propell_ship(dt)
    
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
    hudText11 = menuFont.render(f'MousePosition: {mousePos}',False,WHITE)
    screen.blit(hudText11,(WIDTH/2-30,bottomHud.frame.top+fontHeight))
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