import pygame
import sys
from scenes.menu import mostrar_menu
from scenes.juego import jugar
from config import FPS, NOMBRE_JUEGO
from scenes.sala_principal import sala_principal

# Inicializar Pygame
pygame.init()

# Obtener resolución de pantalla
info = pygame.display.Info()
ANCHO, ALTO = info.current_w, info.current_h

pantalla = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)
pygame.display.set_caption(NOMBRE_JUEGO)
clock = pygame.time.Clock()

escena_actual = "menu"

while True:
    if escena_actual == "menu":
        escena_actual = mostrar_menu(pantalla, ANCHO, ALTO)
    elif escena_actual == "juego":
        escena_actual = sala_principal(pantalla, ANCHO, ALTO)# 👈 Aquí se llama a la Sala Principal
    elif escena_actual == "salir":
        pygame.quit()
        sys.exit()

    clock.tick(FPS)
