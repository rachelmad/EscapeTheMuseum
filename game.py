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
        constellationRoom()
        dinosaurRoom()


def manOnMoonRoom():
    manOnMoonBackGround = pygame.image.load('manOnTheMoon.jpg')
    manOnMoonBackGround = pygame.transform.scale(manOnMoonBackGround, (WINDOWWIDTH, WINDOWHEIGHT))
    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()

        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(manOnMoonBackGround, (0, 0))
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
    dinosaurBackGround = pygame.image.load('dinosaur.jpg')
    dinosaurBackGround = pygame.transform.scale(dinosaurBackGround, (WINDOWWIDTH, WINDOWHEIGHT))
    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()     
        
        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(dinosaurBackGround, (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS)	


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()