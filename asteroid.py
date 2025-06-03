import pygame
import random
from constants import *

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius

class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        for group in Asteroid.containers:
            group.add(self)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
          return
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)

        # Create two new velocities from the original
        vel1 = self.velocity.rotate(random_angle) * 1.2
        vel2 = self.velocity.rotate(-random_angle) * 1.2

        # Spawn the two new asteroids
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = vel1

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = vel2