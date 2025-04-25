import pygame
import sys
from scenes.menu import mostrar_menu
from config import FPS, NOMBRE_JUEGO
from scenes.sala_principal import sala_principal
from scenes.sala_propulsion import sala_propulsion
from scenes.sala_energia import sala_energia
from scenes.sala_comunicaciones import sala_comunicaciones
from scenes.sala_almacenamiento import sala_almacenamiento

pygame.init()
info = pygame.display.Info()
ANCHO, ALTO = info.current_w, info.current_h

pantalla = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)
pygame.display.set_caption(NOMBRE_JUEGO)
clock = pygame.time.Clock()

escena_actual = "menu"
origen = "menu"

while True:
    if isinstance(escena_actual, tuple):
        escena, origen = escena_actual
    else:
        escena, origen = escena_actual, "menu"

    if escena == "menu":
        escena_actual = mostrar_menu(pantalla, ANCHO, ALTO)

    elif escena == "juego":
        escena_actual = sala_principal(pantalla, ANCHO, ALTO, entrada_por=origen)

    elif escena == "sala_principal":
        escena_actual = sala_principal(pantalla, ANCHO, ALTO, entrada_por=origen)

    elif escena == "sala_propulsion":
        escena_actual = sala_propulsion(pantalla, ANCHO, ALTO, entrada_por=origen)

    elif escena == "sala_energia":
        escena_actual = sala_energia(pantalla, ANCHO, ALTO, entrada_por=origen)

    elif escena == "sala_comunicaciones":
        escena_actual = sala_comunicaciones(pantalla, ANCHO, ALTO, entrada_por=origen)
        
    elif escena == "sala_almacenamiento":
        escena_actual = sala_almacenamiento(pantalla, ANCHO, ALTO, entrada_por=origen)

    elif escena == "salir":
        pygame.quit()
        sys.exit()
    clock.tick(FPS)
