import pygame
from constants import *
from player import Player
def main():
    pygame.init #initializes pygame
    print("Starting Asteroids!")
    print("Screen width: 1280 \nScreen height: 720")

    dt = 0
    clock = pygame.time.Clock() #initializes fps clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #sets window size
    
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    

    running = True
    while running: # this is the "game loop". it runs until the user quits, and keeps the program running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        player.draw(screen) #this sets the solid color of the gui window
        player.update(dt) 
        pygame.display.flip() # this updates what pygame draws to the screen
        clock.tick(60) #clock sets the fps, in this case to 60
        dt = clock.tick(60)/1000 #this decouples the game physics from the rendering speed 













if __name__ == "__main__":
    main()
