import pygame
from circleshape import CircleShape
from constants import COLOR_WHITE, DRAW_LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_WHITE, self.position, self.radius, DRAW_LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt