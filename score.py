import pygame
from constants import SCORE_SCREEN_POS, DEFAULT_FONT, DEFAULT_FONT_SIZE, COLOR_WHITE

class Score(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.value = 0
        self.font = pygame.font.SysFont(DEFAULT_FONT, DEFAULT_FONT_SIZE)

    def boost(self, points):
        self.value += points
    
    def reset(self):
        self.value = 0

    def draw(self, screen):
        score_txt = self.font.render(f"{self.value:.0f}", False, COLOR_WHITE)
        screen.blit(score_txt, SCORE_SCREEN_POS)
    
    # score auto-increases over time
    def update(self, dt):
        self.value += dt * 10