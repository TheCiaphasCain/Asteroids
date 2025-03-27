import pygame
from constants import *
def main():
    pygame.init #initializes pygame
    print("Starting Asteroids!")
    print("Screen width: 1280 \nScreen height: 720")
    clock = pygame.time.Clock() #initializes fps clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #sets window size
    running = True
    while running: # this is the "game loop". it runs until the user quits, and keeps the program running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black") #this sets the solid color of the gui window
        pygame.display.flip() # this updates what pygame draws to the screen
        clock.tick(60) #clock sets the fps, in this case to 60











if __name__ == "__main__":
    main()
