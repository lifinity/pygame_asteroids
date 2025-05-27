import pygame
import random
from circleshape import CircleShape
from constants import COLOR_WHITE, DRAW_LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_BASE_POINTS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.value = int(ASTEROID_MIN_RADIUS / radius) * ASTEROID_BASE_POINTS

    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_WHITE, self.position, self.radius, DRAW_LINE_WIDTH)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        split_angle = random.uniform(20, 50)
        split_radius = self.radius - ASTEROID_MIN_RADIUS

        split_asteroid = Asteroid(self.position.x, self.position.y, split_radius)
        split_asteroid.velocity = self.velocity.rotate(split_angle) * 1.2

        split_asteroid = Asteroid(self.position.x, self.position.y, split_radius)
        split_asteroid.velocity = self.velocity.rotate(-split_angle) * 1.2

    def update(self, dt):
        self.position += self.velocity * dt