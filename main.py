# import the pygame module, so you can use it
import pygame
from Game import *
import Entities

from dev import *

# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Python Game DevPost Hackathon")
     
    # create a surface on screen that has the size of WIDTH x HEIGHT
    screen = pygame.display.set_mode((600,400))
     
    # define a variable to control the main loop
    running = True

    print('State Stack: ', Game.stateStack)
    Game.appendState(Game.State.NONE)
    print('State Stack: ', Game.stateStack)
    Game.popState()
    print('State Stack: ', Game.stateStack)

    player = Entities.Square()
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        match Game.currentState():
            case Game.State.NONE:
                # print('Nothing happens')
                continue
            case Game.State.PAUSE:
                print('PAUSED')
            case Game.State.MAINMENU:
                print('MENU')
            case Game.State.DEV:
                devState()

     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
