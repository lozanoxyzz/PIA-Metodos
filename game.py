from settings import *
import random
import pygame
import time

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.state = STATE_MENU

    def render(self):
        """
        Render the game based on current state.
        """
        # Clear the screen
        self.screen.fill(BLACK)

        if self.state == STATE_MENU:
            self.render_menu()

    def render_menu(self):
        ## CREA ESTRELLAS
        stars = []
        for _ in range(NUM_STARS):
            x = random.randint(0, STAR_WIDTH)
            y = random.randint(0, STAR_HEIGHT)
            size = random.randint(1, 2)  # tamaño de la estrella
            stars.append((x, y, size))

        ## FONDO ESPACIO
        for n in range(600):  # altura de la pantalla
            # Gradiente de color, empieza con negro y gradualmente va hacia un color más claro
            r = int(0 + (n / 600) * 20)  # rojo
            g = int(0 + (n / 600) * 20)  # verde
            b = int(30 + (n / 600) * 40)  # azul (más intenso en el fondo)
            pygame.draw.line(self.screen, (r, g, b), (0, n), (800, n))

        # Dibujar estrellas
        for star in stars:
            pygame.draw.circle(self.screen, WHITE, (star[0], star[1]), star[2])

        time.sleep(0.20)

