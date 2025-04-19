# Example file showing a basic pygame "game loop"
import pygame
from settings import *
import random
import time
from game import Game


def main():
    # pygame setup
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
    clock = pygame.time.Clock()

    game = Game(screen)
    game.render_menu()

    running = True
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.render()
        pygame.display.flip()

        clock.tick(FPS)  # limits FPS to 60

    pygame.quit()

main()