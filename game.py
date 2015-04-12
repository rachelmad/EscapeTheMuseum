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
                if (mousex > 680 and mousex < 780 and mousey > 475 and mousey < 580):
                    while True:
                        #manOnMoonRoom()
<<<<<<< HEAD

                        #constellationRoom()
                        #dinosaurRoom()
                        

                        grandRoom()
=======
                        constellationRoom()
                        #dinosaurRoom()
                        #grandRoom()
>>>>>>> e5bc30b210dedf0abe08b734ad4e6a7dde689b66
        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(startBackground, (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def manOnMoonRoom():
    manOnMoonBackGround = pygame.image.load('manOnTheMoon.jpg')
    manOnMoonBackGround = pygame.transform.scale(manOnMoonBackGround, (WINDOWWIDTH, WINDOWHEIGHT))
    clueClicked = 0
    clueText = None
    score = 0
    answered = [0, 0, 0, 0]
    showAnswer = False
    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                if (mousex > 430 and mousex < 630 and mousey > 355 < 450 ):
                    clueClicked = -1
                    clueText = "The First Man on the moon.."
                    answer1 = "Bob Dylan"
                    answer2 = "Michael Collins"
                    answer3 = "Neil Armstrong"
                    answer = 3
                elif (mousex > 350 and mousex < 790 and mousey < 215 and mousey > 57):
                    clueClicked = -1
                    clueText = "Landed the first humans on the moon"
                    answer1 = "Lunar Rover"
                    answer2 = "Apollo 11"
                    answer3 = "Eagle"
                    answer = 2
                elif (mousex > 0 and mousex < 300 and mousey > 118 and mousey < 320 ):
                    clueClicked = -1
                    clueText = "Which is not one of the moon phases?"
                    answer1 = "New Moon"
                    answer2 = "Last Quarter"
                    answer3 = "Half Moon"
                    answer = 3

        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(manOnMoonBackGround, (0, 0))
        if clueClicked < 0 or showAnswer == True:
            if showAnswer == True and clueClicked == 0:
                showAnswer = resultBox("Try again :(", mousex, mousey)
            elif showAnswer == True and clueClicked > 0:
                showAnswer = resultBox("Correct!", mousex, mousey)
            else:
                clueClicked = displayClue(clueText, mousex, mousey, answer1, answer2, answer3, answer)
                if clueClicked >= 0:
                    showAnswer = True
                    print score
                    if answered[clueClicked - 1] == 0:
                        score += 1
                        answered[clueClicked - 1] = 1
                        print score
        if score == 3:
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        

def constellationRoom():
    constellationBkgd = pygame.image.load('constellations.jpg')
    constellationBkgd = pygame.transform.scale(constellationBkgd, (WINDOWWIDTH, WINDOWHEIGHT))
    clueClicked = 0
    clueText = None
    score = 0
    answered = [0, 0, 0, 0]
    showAnswer = False
    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                print mousex
                print mousey
                if (mousex > 125 and mousex < 165 and mousey > 229 and mousey < 269):
                    clueClicked = -1
                    clueText = "The ___ is the only known star in our galaxy which is not part of a constellation."
                    answer1 = "Rigel"
                    answer2 = "Sun"
                    answer3 = "Capella A"
                    answer = 2
                elif (mousex > 80 and mousex < 120 and mousey > 546 and mousey < 586):
                    clueClicked = -1
                    clueText = "How many zodiac constellations are there?"
                    answer1 = "13"
                    answer2 = "14"
                    answer3 = "11"
                    answer = 1
                elif (mousex > 479 and mousex < 529 and mousey > 309 and mousey < 349):
                    clueClicked = -1
                    clueText = "The _____ star lets navigators figure out their latitude to help ships travel across the oceans."
                    answer1 = "Bright"
                    answer2 = "South"
                    answer3 = "North"
                    answer = 3
                elif (mousex > 637 and mousex < 677 and mousey > 476 and mousey < 516):
                    clueClicked = -1
                    clueText = "Ursa Major is visible in the Southern Hemisphere."
                    answer1 = "True"
                    answer2 = "False"
                    answer3 = "Maybe"
                    answer = 2
        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(constellationBkgd, (0, 0))
        if clueClicked < 0 or showAnswer == True:
            if showAnswer == True and clueClicked == 0:
                showAnswer = resultBox("Try again :(", mousex, mousey)
            elif showAnswer == True and clueClicked > 0:
                showAnswer = resultBox("Correct!", mousex, mousey)
            else:
                clueClicked = displayClue(clueText, mousex, mousey, answer1, answer2, answer3, answer)
                if clueClicked >= 0:
                    showAnswer = True
                    print score
                    if answered[clueClicked - 1] == 0:
                        score += 1
                        answered[clueClicked - 1] = 1 
                        print score               
        if clueClicked < 0:
            clueClicked = displayClue(clueText, mousex, mousey, answer1, answer2, answer3, answer)
            if clueClicked > 0 and answered[clueClicked - 1] == 0:
                score += 1
                answered[clueClicked - 1] = 1
        if score == 4:
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
        
def dinosaurRoom():
    dinosaurBackGround = pygame.image.load('dinosaur.jpg')
    dinosaurBackGround = pygame.transform.scale(dinosaurBackGround, (WINDOWWIDTH, WINDOWHEIGHT))
    clueClicked = 0
    clueText = None
    score = 0
    answered = [0, 0, 0, 0]
    showAnswer = False
    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                if (mousex > 510 and mousex < 540 and mousey > 335 and mousey < 365):
                    clueClicked = -1
                    clueText = "When did dinosaurs die out"
                    answer1 = "65,000 years ago"
                    answer2 = "65 million years ago"
                    answer3 = "65 billion years ago"
                    answer = 2
                elif (mousex > 170 and mousex < 195 and mousey > 405 and mousey < 415):
                    clueClicked = -1
                    clueText = "Dinosaurs laid eggs"
                    answer1 = "Always"
                    answer2 = "Sometimes"
                    answer3 = "Never"
                    answer = 1
                elif (mousex > 450 and mousex < 475 and mousey > 425 and mousey < 440):
                    clueClicked = -1
                    clueText = "Dinosaur fossils have been found in..."
                    answer1 = "Africa, Asia, and Antartica"
                    answer2 = "Asia, Africa, and North America"
                    answer3 = "All seven continents"
                    answer = 3
                elif (mousex > 300 and mousex < 315 and mousey > 405 and mousey < 415):
                    clueClicked = -1
                    clueText = "People who study dinosaurs are called..."
                    answer1 = "Dinotologists"
                    answer2 = "Paleontologists"
                    answer3 = "Fossilogists"
                    answer = 2
        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(dinosaurBackGround, (0, 0))
        if clueClicked < 0 or showAnswer == True:
            if showAnswer == True and clueClicked == 0:
                showAnswer = resultBox("Try again :(", mousex, mousey)
            elif showAnswer == True and clueClicked > 0:
                showAnswer = resultBox("Correct!", mousex, mousey)
            else:
                clueClicked = displayClue(clueText, mousex, mousey, answer1, answer2, answer3, answer)
                if clueClicked >= 0:
                    showAnswer = True
                    print score
                    if answered[clueClicked - 1] == 0:
                        score += 1
                        answered[clueClicked - 1] = 1 
                        print score               
        if score == 4:
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def grandRoom():
    grandBackGround = pygame.image.load('grandEntryHall.jpg')
    grandBackGround = pygame.transform.scale(grandBackGround, (WINDOWWIDTH, WINDOWHEIGHT))
    clueClicked = 0
    clueText = None
    score = 0
    answered = [0, 0, 0, 0]
    showAnswer = False
    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                print mousex
                print mousey
                if (mousex > 557 and mousex < 573 and mousey > 320 and mousey < 379):
                   clueClicked = -1
                   clueText = "Who is the famous Romanov Daughter?"
                   answer1 = "Marilyn Monroe"
                   answer2 = "Tatiana"
                   answer3 = "Anastasia"
                   answer = 3
                elif (mousex > 291 and mousex < 306 and mousey > 9 and mousey < 23):
                    clueClicked = -1
                    clueText = "What illness did the Romanov son have?"
                    answer1 = "Hemophilia"
                    answer2 = "Scurvy"
                    answer3 = "Measles"
                    answer = 1
                elif (mousex > 742 and mousex < 790 and mousey > 318 and mousey < 355):
                    clueClicked = -1
                    clueText = "Where did the Romanovs live?"
                    answer1 = "Germany"
                    answer2 = "Iceland"
                    answer3 = "Russia"
                    answer = 3
                elif (mousex > 45 and mousex < 72 and mousey > 310 and mousey < 335):
                    clueClicked = -1
                    clueText = "The Romanov family advisor was..."
                    answer1 = "Vladimir Putin"
                    answer2 = "Rasputin"
                    answer3 = "Karl Marx"
                    answer = 2
        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(grandBackGround, (0, 0))
        if clueClicked < 0 or showAnswer == True:
            if showAnswer == True and clueClicked == 0:
                showAnswer = resultBox("Try again :(", mousex, mousey)
            elif showAnswer == True and clueClicked > 0:
                showAnswer = resultBox("Correct!", mousex, mousey)
            else:
                clueClicked = displayClue(clueText, mousex, mousey, answer1, answer2, answer3, answer)
                if clueClicked >= 0:
                    showAnswer = True
                    print score
                    if answered[clueClicked - 1] == 0:
                        score += 1
                        answered[clueClicked - 1] = 1 
                        print score               
        if score == 4:
            return

    
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
            return 2
        if (mousex > 90 and mousex < 90 + 35 and mousey > 400 and mousey < 400 + 35):
            return 0
    if correct == 3:
        if (mousex > 90 and mousex < 90 + 35 and mousey > 200 and mousey < 200 + 35):
            return 0
        if (mousex > 90 and mousex < 90 + 35 and mousey > 300 and mousey < 300 + 35):
            return 0
        if (mousex > 90 and mousex < 90 + 35 and mousey > 400 and mousey < 400 + 35):
            return 3
        
    return -1
    
    
def resultBox(text, mousex, mousey):
    bigRect = pygame.Rect(50, 50, WINDOWWIDTH - 100, WINDOWHEIGHT - 100)
    smallRect = pygame.Rect(55, 55, WINDOWWIDTH - 110, WINDOWHEIGHT - 110)
    pygame.draw.rect(DISPLAYSURF, BLACK, bigRect)
    pygame.draw.rect(DISPLAYSURF, WHITE, smallRect)
    
    clueFont = pygame.font.Font('freesansbold.ttf', 35)
    clueSurf = clueFont.render(text, True, BLACK)
    clueRect = clueSurf.get_rect()
    clueRect.midtop = (WINDOWWIDTH / 2, 80)
    
    DISPLAYSURF.blit(clueSurf, clueRect)
    
    bigButton1 = pygame.Rect(WINDOWWIDTH / 2 - 50, WINDOWHEIGHT - 130, 100, 50)
    smallButton1 = pygame.Rect(WINDOWWIDTH /2 - 45, WINDOWHEIGHT - 125, 90, 40)
    pygame.draw.rect(DISPLAYSURF, BLACK, bigButton1)
    pygame.draw.rect(DISPLAYSURF, RED, smallButton1)
    
    okSurf = clueFont.render("OK", True, BLACK)
    okRect = okSurf.get_rect()
    okRect.midtop = (WINDOWWIDTH / 2, WINDOWHEIGHT - 120)
    
    DISPLAYSURF.blit(okSurf, okRect)
    
    if (mousex > WINDOWWIDTH / 2 - 50 and mousex < WINDOWWIDTH / 2 - 50 + 150 and mousey > WINDOWHEIGHT - 130 and mousey < WINDOWHEIGHT - 130 + 50):
        return False
        
    return True
    
def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()

