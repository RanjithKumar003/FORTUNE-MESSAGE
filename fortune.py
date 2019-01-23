import random
import pygame
from pygame.locals import  *
pygame.init()
pygame.display.set_caption("Fortune")

print("              _______. ")
print("   ______    | .   . |\ ")
print("  /     /\   |   .   |.\ ")
print(" /  '  /  \  | .   . |.'| ")
print("/_____/. . \ |_______|.'| ")
print("\ . . \    /  \ ' .   \'| ")
print(" \ . . \  /    \____'__\| ")
print("  \_____\/ ")
print("                            ")
print("__________________________")
print(" ROLL THE DICE")
print("--------------------------")

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



input()
myRoll=RollTwoDice()
print("You rolled a "+str(myRoll)+'!')
message=["your are going to loss somthing","Your going to eat more today","You are going to meet you patner","Your are ready to learn lesson from failure","Going to get victory for your efforts","Going to get loot","Your going to fool by someone","Your are going to miss someone","Your going to meet some important person","Becarefull","Going to waste this day","Wonderfull gift is waiting for you"]

gamedisplay=pygame.display.set_mode((1080,750))
font = pygame.font.SysFont("comicsansms",50)
text1= font.render("Press \'Enter\' to check your fortune",True, (0,128,0))
text = font.render(message[myRoll-1], True,(0,128,0))
#gamedisplay.fill(255,255,255)
gamedisplay.blit(text1,(100, 100))
gamedisplay.blit(text,(250, 250))
pygame.display.flip()