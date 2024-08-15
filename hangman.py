import pygame
import sys
import random
import time
import re

from pygame.locals import *

BLACK = (0, 0, 0)
BEIGE = (245, 245, 220)
BISTRE = (61, 43, 31)
BLUE = (23, 236, 236)
BROWN = (150, 75, 0)

LEFT_CLICK = (1, 0, 0)
RIGHT_CLICK = (0, 0, 1)

pygame.init()

pygame.display.set_caption("Hangman Game")

Display = pygame.display.set_mode((500, 500), 0, 32)

Easy = ["BALL", "BAT", "BABY", "BASKET", "BRING", "BEST"]
Medium = [" balloon", "beautiful", "beginning", "beige", "believe", "benefit", \
          "breathe", "brief", "bureaucracy", "business"]
Hard = ["BACKGROUND", "BOOKWORM", "Bandwagon", "Barefoot", "THUNDERSTORM", \
        "Biography", "Backbone", "Brotherhood", "Breathtaking", \
        "Boisterous", "Bewildered", "Benevolent"]
Color = ["BLACK", "Beige", "Bistre", "BLUE", "BROWN"]

Font = pygame.font.Font("freesansbold.ttf", 33)
Font2 = pygame.font.Font("freesansbold.ttf", 20)

Display.fill(BLUE)


def Num(choice):
    Num = 0
    if choice == 1:
        Num == random.randint(0, len(Easy) - 1)

    elif choice == 2:
        Num = random.randint(0, len(Medium) - 1)

    elif choice == 3:
        Num = random.randint(0, len(Hard) - 1)

    elif choice == 4:
        Num = random.randint(0, len(Color) - 1)

    return Num


def Menu(num, choice):
    if (choice == 1):
        Letter = Easy[num]

    elif (choice == 2):
        Letter = Medium[num]

    elif (choice == 3):
        Letter = Hard[num]

    elif (choice == 4):
        Letter = Color[num]

    return Letter


def HM(condition):
    if (condition == 0):
        pygame.draw.line(Display, BROWN, (10, 400), (300, 400), 8)  
        pygame.draw.line(Display, BROWN, (50, 50), (50, 400), 8)  
        pygame.draw.line(Display, BROWN, (50, 60), (250, 60), 8)  
        pygame.draw.line(Display, BROWN, (150, 60), (150, 100), 8)  
        pygame.draw.circle(Display, BROWN, (150, 150), 50, 8)  # head
        pygame.draw.line(Display, BROWN, (150, 200), (150, 300), 8)  
        pygame.draw.line(Display, BROWN, (150, 210), (100, 250), 8) 
        pygame.draw.line(Display, BROWN, (150, 210), (200, 250), 8)  
        pygame.draw.line(Display, BROWN, (150, 300), (100, 350), 8) 
        pygame.draw.line(Display, BROWN, (150, 300), (200, 350), 8) 

    elif (condition == 1):
        pygame.draw.line(Display, BLACK, (10, 400), (300, 400), 8)  

    elif (condition == 2):
        pygame.draw.line(Display, BLACK, (50, 50), (50, 400), 8) 

    elif (condition == 3):
        pygame.draw.line(Display, BLACK, (50, 60), (250, 60), 8) 

    elif (condition == 4):
        pygame.draw.line(Display, BLACK, (150, 60), (150, 100), 8)  

    elif (condition == 5):
        pygame.draw.circle(Display, BLACK, (150, 150), 50, 8)  

    elif (condition == 6):
        pygame.draw.line(Display, BLACK, (150, 200), (150, 300), 8)  

    elif (condition == 7):
        pygame.draw.line(Display, BLACK, (150, 210), (100, 250), 8)  

    elif (condition == 8):
        pygame.draw.line(Display, BLACK, (150, 210), (200, 250), 8) 

    elif (condition == 9):
        pygame.draw.line(Display, BLACK, (150, 300), (100, 350), 8)  

    elif (condition == 10):
        pygame.draw.line(Display, BLACK, (150, 300), (200, 350), 8) 

    elif (condition == 11):
        pygame.draw.line(Display, BLUE, (10, 400), (300, 400), 8)  
        pygame.draw.line(Display, BLUE, (50, 50), (50, 400), 8)  
        pygame.draw.line(Display, BLUE, (50, 60), (250, 60), 8)  
        pygame.draw.line(Display, BLUE, (150, 60), (150, 100), 8)  
        pygame.draw.circle(Display, BLUE, (150, 150), 50, 8) 
        pygame.draw.line(Display, BLUE, (150, 200), (150, 300), 8)  
        pygame.draw.line(Display, BLUE, (150, 210), (100, 250), 8)  
        pygame.draw.line(Display, BLUE, (150, 210), (200, 250), 8)  
        pygame.draw.line(Display, BLUE, (150, 300), (100, 350), 8)  
        pygame.draw.line(Display, BLUE, (150, 300), (200, 350), 8)  


def FHM():
    pygame.draw.line(Display, BISTRE, (10, 400), (190, 400), 8)  
    pygame.draw.line(Display, BISTRE, (30, 90), (30, 400), 8) 
    pygame.draw.line(Display, BISTRE, (30, 100), (160, 100), 8) 
    pygame.draw.line(Display, BISTRE, (100, 100), (100, 120), 8) 
    pygame.draw.circle(Display, BISTRE, (100, 170), 50, 8) 
    pygame.draw.line(Display, BISTRE, (100, 220), (100, 320), 8) 
    pygame.draw.line(Display, BISTRE, (100, 230), (50, 270), 8)  
    pygame.draw.line(Display, BISTRE, (100, 230), (150, 270), 8)  
    pygame.draw.line(Display, BISTRE, (100, 320), (50, 360), 8) 
    pygame.draw.line(Display, BISTRE, (100, 320), (150, 360), 8)  


def StartGame():
    Display.blit(pygame.font.Font("freesansbold.ttf", 40).render("HANGMAN GAME", True, BLACK), (20, 20))
    Display.blit(Font2.render("WORD STARTS WITH LETTER B", True, BLACK), (60, 60))
    Display.blit(Font.render("Level Difficulty", True, BLACK), (200, 150))
    Display.blit(Font2.render("1-Easy", True, BLACK), (200, 200))
    Display.blit(Font2.render("2-Medium", True, BLACK), (200, 250))
    Display.blit(Font2.render("3-Hard", True, BLACK), (200, 300))
    Display.blit(Font2.render("4-Color", True, BLACK), (200, 350))


def main():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BEIGE = (245, 245, 220)
    BISTRE = (0, 255, 0)
    BLUE = (0, 0, 255)
    BROWN = (200, 200, 200)

    TheChoice = 0

    StartGame()

    FHM()

    Condition = True
    while Condition:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if (event.key == K_1) or (event.key == 257): 
                    TheChoice = 1
                    Condition = False
                    break
                elif event.key == K_2 or event.key == 258:  
                    TheChoice = 2
                    Condition = False
                    break
                elif event.key == K_3 or event.key == 259:  
                    TheChoice = 3
                    Condition = False
                    break
                elif event.key == K_4 or event.key == 260: 
                    TheChoice = 4
                    Condition = False
                    break

            elif event.type == MOUSEBUTTONDOWN:
                
                if (pygame.mouse.get_pos()[0] > 200 and \
                        pygame.mouse.get_pos()[1] > 200 and \
                        pygame.mouse.get_pos()[0] < 265 and \
                        pygame.mouse.get_pos()[1] < 215):
                    TheChoice = 1
                    Condition = False
                    break
                # Medium
                elif (pygame.mouse.get_pos()[0] > 200 and \
                      pygame.mouse.get_pos()[1] > 250 and \
                      pygame.mouse.get_pos()[0] < 295 and \
                      pygame.mouse.get_pos()[1] < 265):
                    TheChoice = 2
                    Condition = False
                    break
                # Hard
                elif (pygame.mouse.get_pos()[0] > 200 and \
                      pygame.mouse.get_pos()[1] > 300 and \
                      pygame.mouse.get_pos()[0] < 265 and \
                      pygame.mouse.get_pos()[1] < 315):
                    TheChoice = 3
                    Condition = False
                    break
                # Color
                elif (pygame.mouse.get_pos()[0] > 200 and \
                      pygame.mouse.get_pos()[1] > 350 and \
                      pygame.mouse.get_pos()[0] < 270 and \
                      pygame.mouse.get_pos()[1] < 365):
                    TheChoice = 4
                    Condition = False
                    break

        if (TheChoice != 0):
            Display.fill(WHITE)

        pygame.display.update()
        pygame.time.Clock().tick(30)  # 30fps

    # This is to make sure the word and random number is constant
    TheNum = Num(TheChoice)
    TheLetter = Menu(TheNum, TheChoice)
    # TheLetter = "wew"

    # This is to check if it got the word from the list
    # print(TheLetter)

    EmptyMenu = []

    for i in range(len(TheLetter)):
        EmptyMenu.append('-')

    Hide = Font.render("".join(EmptyMenu), True, BLACK)
    Hidden = Hide.get_rect()
    Hidden.center = (350, 250)
    Display.blit(Hide, Hidden)

    Condition = 0; 
    Off = 0  
    TheTime = 0
    Start = time.time()  
    Display.blit(Font2.render("Time(s):", True, BLACK), (300, 10))

    LastKeyPressed = ""

    Display.blit(pygame.font.Font("freesansbold.ttf", 15).render("Press 0 to quit game", True, BLACK), (20, 10))

    while True:
        HM(Condition)
        End = time.time()  
        if (int(End) - int(Start) == 1):
            pygame.draw.rect(Display, WHITE, (385, 0, 100, 50))  
            TheTime = TheTime + 1
            Timer = Font2.render(str(TheTime), True, BLACK)
            Display.blit(Timer, (400, 10))
            Start = time.time()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                LastKeyPressed = event.key
                pygame.draw.rect(Display, WHITE, (220, 200, 280, 100)) 
                pygame.draw.rect(Display, WHITE, (260, 50, 200, 100))  
                UserInput = event.key
                if re.search("[a-z]", chr(event.key)):
                    if ((chr(event.key).upper() in TheLetter) or (chr(event.key).lower() in TheLetter)):
                        for i in range(len(TheLetter)):
                            if ((TheLetter[i] == (chr(event.key)).upper()) or (TheLetter[i] == (chr(event.key)).lower())):
                                EmptyMenu[i] = TheLetter[i]

                    else:
                        Condition = Condition + 1

                    Hide = Font.render("".join(EmptyMenu), True, BLACK)
                    Hidden = Hide.get_rect()
                    Hidden.center = (350, 250)
                    Display.blit(Hide, Hidden)

                else:
                    if (event.key == K_0 or event.key == 256):
                        Display.blit(Font.render("EXIT?", True, BEIGE), (340, 220))
                        Display.blit(Font2.render("Yes", True, BLUE), (340, 270))
                        Display.blit(Font2.render("No", True, BLUE), (415, 270))
                    else:
                        In = Font2.render("INVALID INPUT!!!", True, BEIGE)
                        Input = In.get_rect()
                        Input.center = (350, 100)
                        Display.blit(In, Input)
                        Display.blit(Hide, Hidden)

            elif event.type == KEYUP:
                pygame.draw.rect(Display, WHITE, (260, 50, 200, 100))
            elif event.type == MOUSEBUTTONDOWN:

                if (LastKeyPressed == K_0 or LastKeyPressed == 256):
                    if (pygame.mouse.get_pressed() == LEFT_CLICK):
                        # Yes
                        if (pygame.mouse.get_pos()[0] > 340 and \
                                pygame.mouse.get_pos()[1] > 270 and \
                                pygame.mouse.get_pos()[0] < 385 and \
                                pygame.mouse.get_pos()[1] < 285):
                            pygame.draw.rect(Display, WHITE, (340, 270, 35, 25))
                            Display.blit(Font2.render("Yes", True, BISTRE), (340, 270))

                        elif (pygame.mouse.get_pos()[0] > 415 and \
                              pygame.mouse.get_pos()[1] > 270 and \
                              pygame.mouse.get_pos()[0] < 450 and \
                              pygame.mouse.get_pos()[1] < 285):
                            pygame.draw.rect(Display, WHITE, (415, 270, 35, 25))
                            Display.blit(Font2.render("No", True, BISTRE), (415, 270))


            elif event.type == MOUSEBUTTONUP:  # Yes
                if (LastKeyPressed == K_0 or LastKeyPressed == 256):

                    if (pygame.mouse.get_pos()[0] > 340 and \
                            pygame.mouse.get_pos()[1] > 270 and \
                            pygame.mouse.get_pos()[0] < 385 and \
                            pygame.mouse.get_pos()[1] < 285):

                        pygame.quit()
                        sys.exit()

                    elif (pygame.mouse.get_pos()[0] > 415 and \
                          pygame.mouse.get_pos()[1] > 270 and \
                          pygame.mouse.get_pos()[0] < 450 and \
                          pygame.mouse.get_pos()[1] < 285):
                        pygame.draw.rect(Display, WHITE, (415, 270, 35, 25))
                        Display.blit(Font2.render("No", True, BISTRE), (415, 270))
                        pygame.draw.rect(Display, WHITE, (300, 200, 200, 100))

                        Hide = Font.render("".join(EmptyMenu), True, BLACK)
                        Hidden = Hide.get_rect()
                        Hidden.center = (400, 250)
                        Display.blit(Hide, Hidden)

                        LastKeyPressed = ""


                    else:
                        pygame.draw.rect(Display, WHITE, (340, 270, 35, 25))
                        Display.blit(Font2.render("Yes", True, BLUE), (340, 270))
                        pygame.draw.rect(Display, WHITE, (415, 270, 35, 25))
                        Display.blit(Font2.render("No", True, BLUE), (415, 270))

        if (Condition == 10):
            Display.fill(WHITE)
            HM(Condition + 1)
            Ov = Font2.render("GAME OVER!!!", True, BEIGE)
            Over = Ov.get_rect()
            Over.center = (400, 250)
            Display.blit(Ov, Over)
            Off = 1


        elif (TheLetter == "".join(EmptyMenu)):
            Display.fill(WHITE)
            Cong = Font.render("CONGRATS!!!", True, BISTRE)
            Congrats = Cong.get_rect()
            Congrats.center = (250, 220)
            Display.blit(Cong, Congrats)

            Let = Font2.render("The word is:", True, BLACK)
            Letter = Let.get_rect()
            Letter.center = (250, 250)
            Display.blit(Let, Letter)

            Let2 = Font.render(TheLetter, True, BLACK)
            Letter2 = Let2.get_rect()
            Letter2.center = (250, 285)
            Display.blit(Let2, Letter2)

            Off = 1

        pygame.display.update()
        pygame.time.Clock().tick(30)

        if (Off == 1):
            time.sleep(5)
            pygame.quit()
            sys.exit()


main()
