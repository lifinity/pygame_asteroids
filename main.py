import sys
import pygame
from constants import *
from shot import Shot
from score import Score
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    state = STATE_GAME
    paused = False
    announce_font = pygame.font.SysFont(DEFAULT_FONT, DEFAULT_FONT_SIZE * 2)
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Score.containers = (updatable, drawable)
    
    score = Score()
    asteroid_field = AsteroidField()
    player = Player()
    dt = 0

    def reset_game():
        for asteroid in asteroids:
            asteroid.kill()
            del asteroid

        for shot in shots:
            shot.kill()
            del shot

        player.reset()
        score.reset()

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if state == STATE_GAMEOVER:
                    if event.key == pygame.K_y:
                        reset_game()
                        state = STATE_GAME
                    if event.key == pygame.K_n:
                        return

                if event.key == pygame.K_p:
                    paused = not paused

        if state == STATE_GAME:
            if not paused:
                updatable.update(dt)

            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.collides(shot):
                        shot.kill()
                        asteroid.split()
                        score.boost(asteroid.value)

                if asteroid.collides(player):
                    state = STATE_GAMEOVER

            screen.fill(COLOR_BLACK)

            for sprite in drawable:
                sprite.draw(screen)

            pygame.display.flip()

            dt = clock.tick(FPS_LIMIT) / 1000

        if state == STATE_GAMEOVER:
            screen.fill(COLOR_BLACK)

            gg_text = announce_font.render("TRY AGAIN? Y/N", False, COLOR_WHITE)
            gg_rect = gg_text.get_rect(center = (SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) - HEIGHT_OFFSET))
            screen.blit(gg_text, gg_rect)

            pygame.display.flip()

if __name__ == "__main__":
    main()