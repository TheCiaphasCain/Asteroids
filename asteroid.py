import pygame
import random
import constants
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "orange", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius<= constants.ASTEROID_MIN_RADIUS:
            return 
        rand_angle = random.uniform(20, 50)
        pos_vector = pygame.math.Vector2(self.velocity) #create copies of the velocity vector
        neg_vector = pygame.math.Vector2(self.velocity)

        pos_vector = pos_vector.rotate(rand_angle) #rotates the copies
        neg_vector = neg_vector.rotate(-rand_angle)

        pos_vector *= 1.2 #scale copies by 1.2
        neg_vector *= 1.2
        new_rad = self.radius - constants.ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x,self.position.y,new_rad)
        new_asteroid2 = Asteroid(self.position.x,self.position.y,new_rad)

        new_asteroid1.velocity = pos_vector
        new_asteroid2.velocity = neg_vector
        
        

    



    
