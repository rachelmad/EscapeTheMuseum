import random, pygame, sys
import Tkinter
import tkMessageBox
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
        #manOnMoonRoom()
        #constellationRoom()
        dinosaurRoom()
        dinosaurRoom()
        grandRoom()


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
    constellationBackground = pygame.image.load('constellations.jpg')
    constellationBackground = pygame.transform.scale(constellationBackground, (WINDOWWIDTH, WINDOWHEIGHT))
    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()

        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(constellationBackground, (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
        
def dinosaurRoom():
    dinosaurBackGround = pygame.image.load('dinosaur.jpg')
    dinosaurBackGround = pygame.transform.scale(dinosaurBackGround, (WINDOWWIDTH, WINDOWHEIGHT))
    clueClicked = False
    clueText = None
    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                if (mousex > 530 and mousex < 540 and mousey > 355 and mousey < 365):
                    clueClicked = True
                    clueText = "Clue 1"
                elif (mousex > 170 and mouse < 195 and mousey > 405 and mousey < 415):
                    clueClicked = True
                    clueText = "Clue 2"
                elif (mousex > 450 and mouse < 475 and mousey > 425 and mousey < 440):
                    clueClicked = True
                    clueText = "Clue 3"
                elif (mousex > 300 and mouse < 315 and mousey > 405 and mousey < 415):
                    clueClicked = True
                    clueText = "Clue 4"
        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(dinosaurBackGround, (0, 0))
        if clueClicked:
            clueClicked = displayClue(clueText, mousex, mousey)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def grandRoom():
    grandBackGround = pygame.image.load('grandEntryHall.jpg')
    grandBackGround = pygame.transform.scale(grandBackGround, (WINDOWWIDTH, WINDOWHEIGHT))
    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()

        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(grandBackGround, (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def displayClue(text, mousex, mousey):
    bigRect = pygame.Rect(50, 50, WINDOWWIDTH - 100, WINDOWHEIGHT - 100)
    smallRect = pygame.Rect(55, 55, WINDOWWIDTH - 110, WINDOWHEIGHT - 110)
    pygame.draw.rect(DISPLAYSURF, BLACK, bigRect)
    pygame.draw.rect(DISPLAYSURF, WHITE, smallRect)
    
    bigButton = pygame.Rect(WINDOWWIDTH / 2 - 50, WINDOWHEIGHT - 150, 100, 50)
    smallButton = pygame.Rect(WINDOWWIDTH / 2 - 45, WINDOWHEIGHT - 145, 90, 40)
    pygame.draw.rect(DISPLAYSURF, BLACK, bigButton)
    pygame.draw.rect(DISPLAYSURF, RED, smallButton)
    
    clueFont = pygame.font.Font('freesansbold.ttf', 35)
    clueSurf = clueFont.render(text, True, BLACK)
    clueRect = clueSurf.get_rect()
    clueRect.midtop = (WINDOWWIDTH / 2, 80)
    
    okSurf = clueFont.render("OK", True, BLACK)
    okRect = okSurf.get_rect()
    okRect.midtop = (WINDOWWIDTH / 2, WINDOWHEIGHT - 140)
    
    DISPLAYSURF.blit(clueSurf, clueRect)
    DISPLAYSURF.blit(okSurf, okRect)
    
    if (mousex > (WINDOWWIDTH / 2 - 50) and mousex < (WINDOWWIDTH / 2 - 50) + 100 and mousey > (WINDOWHEIGHT - 150) and mousey < (WINDOWHEIGHT - 150 + 50)):
        return False
        
    return True
    
    
def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()