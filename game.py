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
BLUE      = (  0,   0, 255)
YELLOW    = (255, 255,   0)
BGCOLOR = BLACK

def main():
    global FPSCLOCK, DISPLAYSURF         #Global variables
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    startPage()


def startPage():
    startBackground = pygame.image.load('coverpage.jpg')
    startBackground = pygame.transform.scale(startBackground, (WINDOWWIDTH, WINDOWHEIGHT))
    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                print mousex
                print mousey
                if (mousex > 680 and mousex < 780 and mousey > 475 and mousey < 580):
                    while True:
                        manOnMoonRoom()
                        constellationRoom()
                        dinosaurRoom()
                        grandRoom()
        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(startBackground, (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

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
    clueClicked = 0
    clueText = None
    answer1 = None
    answer2 = None
    answer3 = None
    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                if (mousex > 530 and mousex < 540 and mousey > 355 and mousey < 365):
                    clueClicked = -1
                    clueText = "Clue 1"
                    answer1 = "blah"
                    answer2 = "blah"
                    answer3 = "blah"
                elif (mousex > 170 and mousex < 195 and mousey > 405 and mousey < 415):
                    clueClicked = -1
                    clueText = "Clue 2"
                    answer1 = "blah"
                    answer2 = "blah"
                    answer3 = "blah"
                elif (mousex > 450 and mousex < 475 and mousey > 425 and mousey < 440):
                    clueClicked = -1
                    clueText = "Clue 3"
                    answer1 = "blah"
                    answer2 = "blah"
                    answer3 = "blah"
                elif (mousex > 300 and mousex < 315 and mousey > 405 and mousey < 415):
                    clueClicked = -1
                    clueText = "Clue 4"
                    answer1 = "blah"
                    answer2 = "blah"
                    answer3 = "blah"
        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(dinosaurBackGround, (0, 0))
        if clueClicked < 0:
            clueClicked = displayClue(clueText, mousex, mousey, answer1, answer2, answer3, 1)
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


def displayClue(text, mousex, mousey, answer1, answer2, answer3, correct):
    bigRect = pygame.Rect(50, 50, WINDOWWIDTH - 100, WINDOWHEIGHT - 100)
    smallRect = pygame.Rect(55, 55, WINDOWWIDTH - 110, WINDOWHEIGHT - 110)
    pygame.draw.rect(DISPLAYSURF, BLACK, bigRect)
    pygame.draw.rect(DISPLAYSURF, WHITE, smallRect)
    
    clueFont = pygame.font.Font('freesansbold.ttf', 35)
    clueSurf = clueFont.render(text, True, BLACK)
    clueRect = clueSurf.get_rect()
    clueRect.midtop = (WINDOWWIDTH / 2, 80)
    
    oneSurf = clueFont.render(answer1, True, BLACK)
    oneRect = oneSurf.get_rect()
    oneRect.topleft = (150, 200)
    
    twoSurf = clueFont.render(answer2, True, BLACK)
    twoRect = twoSurf.get_rect()
    twoRect.topleft = (150, 300)
    
    threeSurf = clueFont.render(answer3, True, BLACK)
    threeRect = threeSurf.get_rect()
    threeRect.topleft = (150, 400)
    
    DISPLAYSURF.blit(clueSurf, clueRect)
    DISPLAYSURF.blit(oneSurf, oneRect)
    DISPLAYSURF.blit(twoSurf, twoRect)
    DISPLAYSURF.blit(threeSurf, threeRect)
    
    bigButton1 = pygame.Rect(90, 200, 35, 35)
    smallButton1 = pygame.Rect(95, 205, 25, 25)
    pygame.draw.rect(DISPLAYSURF, BLACK, bigButton1)
    pygame.draw.rect(DISPLAYSURF, RED, smallButton1)
    
    bigButton2 = pygame.Rect(90, 300, 35, 35)
    smallButton2 = pygame.Rect(95, 305, 25, 25)
    pygame.draw.rect(DISPLAYSURF, BLACK, bigButton2)
    pygame.draw.rect(DISPLAYSURF, YELLOW, smallButton2)
    
    bigButton3 = pygame.Rect(90, 400, 35, 35)
    smallButton3 = pygame.Rect(95, 405, 25, 25)
    pygame.draw.rect(DISPLAYSURF, BLACK, bigButton3)
    pygame.draw.rect(DISPLAYSURF, BLUE, smallButton3)
    
    if correct == 1:
        if (mousex > 90 and mousex < 90 + 35 and mousey > 200 and mousey < 200 + 35):
            return 1
        if (mousex > 90 and mousex < 90 + 35 and mousey > 300 and mousey < 300 + 35):
            return 0
        if (mousex > 90 and mousex < 90 + 35 and mousey > 400 and mousey < 400 + 35):
            return 0
    if correct == 2:
        if (mousex > 90 and mousex < 90 + 35 and mousey > 200 and mousey < 200 + 35):
            return 0
        if (mousex > 90 and mousex < 90 + 35 and mousey > 300 and mousey < 300 + 35):
            return 1
        if (mousex > 90 and mousex < 90 + 35 and mousey > 400 and mousey < 400 + 35):
            return 0
    if correct == 3:
        if (mousex > 90 and mousex < 90 + 35 and mousey > 200 and mousey < 200 + 35):
            return 0
        if (mousex > 90 and mousex < 90 + 35 and mousey > 300 and mousey < 300 + 35):
            return 0
        if (mousex > 90 and mousex < 90 + 35 and mousey > 400 and mousey < 400 + 35):
            return 1
        
    return -1
    
    
def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()