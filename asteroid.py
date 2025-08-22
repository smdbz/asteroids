import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        split1 = self.velocity.rotate(random.uniform(20, 50))
        split2 = self.velocity.rotate(-random.uniform(20, 50))
        radius1 = self.radius - ASTEROID_MIN_RADIUS
        radius2 = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, radius1)
        asteroid1.velocity = split1 * 1.2

        asteroid2 = Asteroid(self.position.x, self.position.y, radius2)
        asteroid2.velocity = split2 * 1.2