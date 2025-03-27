import pygame 
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    pygame.init() #initializes pygame
    print("Starting Asteroids!")
    print("Screen width: 1280 \nScreen height: 720")

    dt = 0
    clock = pygame.time.Clock() #initializes fps clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #sets window size
    updatable = pygame.sprite.Group() #creates a group of objects that can be updated

    drawable = pygame.sprite.Group() #creates a group of objects that can be drawn

    enemy = pygame.sprite.Group()

    AsteroidField.containers = (updatable)

    Asteroid.containers = (enemy,drawable,updatable)

    Player.containers = (updatable, drawable) #adds player object to both groups


    Asteroid_field = AsteroidField()

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    

    running = True
    while running: # this is the "game loop". it runs until the user quits, and keeps the program running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen) #this sets the solid color of the gui window
        updatable.update(dt)
        for asteroid_sprite in enemy:
            if asteroid_sprite.collision(player) == True:
                print("game over!")
                sys.exit()
        pygame.display.flip() # this updates what pygame draws to the screen
        clock.tick(60) #clock sets the fps, in this case to 60
        dt = clock.tick(60)/1000 #this decouples the game physics from the rendering speed 












if __name__ == "__main__":
    main()
