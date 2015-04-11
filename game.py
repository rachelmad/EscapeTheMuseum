import random, pygame, sys
from pygame.locals import *

#Global variables
FPS = 15                         #Frames per second
WINDOWWIDTH = 800
WINDOWHEIGHT = 600

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
BGCOLOR = BLACK

def main():
    global FPSCLOCK, DISPLAYSURF         #Global variables

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    
    while True:
        manOnMoonRoom()
        constellation()
        dinosaurRoom()


def manOnMoonRoom():
    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()     
        
        DISPLAYSURF.fill(BGCOLOR)
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        

def constellationRoom():
    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()     
        
        DISPLAYSURF.fill(BGCOLOR)
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        

def dinosaurRoom():
    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()     
        
        DISPLAYSURF.fill(BGCOLOR)
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)	

def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()