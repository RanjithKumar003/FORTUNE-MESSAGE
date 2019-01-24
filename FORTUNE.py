import random
import pygame
from pygame.locals import *
pygame.init()
clr= 255, 128, 128
pygame.display.set_caption("Fortune")
font = pygame.font.SysFont("comicsansms",10)
print("===================================================")
print("              _______. ")
print("   ______    | .   . |\ ")
print("  /     /\   |   .   |.\ ")
print(" /  '  /  \  | .   . |.'| ")
print("/_____/. . \ |_______|.'| ")
print("\ . . \    /  \ ' .   \'| ")
print(" \ . . \  /    \____'__\| ")
print("  \_____\/ ")
print("                            ")
print("====================================================")
print(" PRESS ENTER TO ROLL THE DICE AND CHECK YOUR MESSAGE ")
print("====================================================")
def RollTwoDice():
    die1=random.randint(1, 6)
    die2=random.randint(1, 6)
    roll=die1 + die2
    if die1 == 1:
        ShowDie1()
    elif die1==2:
        ShowDie2()
    elif die1==3:
        ShowDie3()
    elif die1==4:
        ShowDie4()
    elif die1==5:
        ShowDie5()
    elif die1==6:
        ShowDie6()
#Next dice
    if die2==1:
        ShowDie1()
    elif die2==2:
        ShowDie2()
    elif die2==3:
        ShowDie3()
    elif die2==4:
        ShowDie4()
    elif die2==5:
        ShowDie5()
    elif die2==6:
        ShowDie6()
    return roll
def ShowDie1():
    print('---------')
    print('|       |')
    print('|   1   |')
    print('|       |')
    print('---------')
    return
def ShowDie2():
    print('---------')
    print('|       |')
    print('|   2   |')
    print('|       |')
    print('---------')
    return
def ShowDie3():
    print('---------')
    print('|       |')
    print('|   3   |')
    print('|       |')
    print('---------')
    return
def ShowDie4():
    print('---------')
    print('|       |')
    print('|   4   |')
    print('|       |')
    print('---------')
    return
def ShowDie5():
    print('---------')
    print('|       |')
    print('|   5   |')
    print('|       |')
    print('---------')
    return
def ShowDie6():
    print('---------')
    print('|       |')
    print('|   6   |')
    print('|       |')
    print('---------')
    return

print("Press \'Enter\' to roll the dice")
input()
myRoll=RollTwoDice()
print("You rolled a "+str(myRoll)+'!')
gamedisplay = pygame.display.set_mode ((1400, 500))
pygame.display.set_caption ('FORTUNE MESSAGE')
font = pygame.font.SysFont("comicsansms", 25)
text = font.render("PRESS HERE TO CHECK YOUR FORTUNE MESSAGE", True, (0, 0, 0))
gamedisplay.fill((153, 217, 234))
gamedisplay.blit(text,(250,250))

pygame.display.flip()
running = 1
while (running == 1):
    for event in pygame.event.get():
            if event.type is MOUSEBUTTONDOWN:
                gamedisplay=pygame.display.set_mode((1200,500))
                message=["Even if you fall down seven times, Stand up at the eighth time","Do the work with your whole heart, you will succeed","Seek out the significance of your problem at this time. Try to understand","Don't get worry about failure, it just teaches you a lesson for your success","Don't worry about the money. The best things in life are free","Fortune not found, abort, retry or ignore","Success lies in the hands of those who want it","Answer just what your heart prompts you","The early bird gets the worm, but the second mouse gets the cheese","Some pursue happiness; you create it","Any day above the ground is a good day","Nothing is so much to be feared as fear"]
                font = pygame.font.SysFont("comicsansms",25)
                text = font.render(message[myRoll-1], True,(0,128,0))
                gamedisplay.fill(clr)
                gamedisplay.blit(text,(50,250))
                pygame.display.flip()