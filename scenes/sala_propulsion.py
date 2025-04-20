import pygame
import sys
from utils.personaje import Personaje

def sala_propulsion(pantalla, ANCHO, ALTO):
    fondo = pygame.image.load("Assets/imagenes/sala_propulsion.png").convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    escala = min(ANCHO / 1366, ALTO / 768)
    jugador = Personaje(x=200, y=300, alto_pantalla=ALTO, escala=escala)

    # 🟩 Puerta izquierda
    puerta_izquierda = pygame.Rect(
        0,
        int(ALTO * 250 / 768),
        int(ANCHO * 120 / 1366),
        int(ALTO * 200 / 768)
    )

    # 🟨 Puerta inferior
    puerta_inferior = pygame.Rect(
        int(ANCHO * 590 / 1366),
        int(ALTO * 582 / 768),
        int(ANCHO * 190 / 1366),
        int(ALTO * 170 / 768)
    )

    # 🧱 Paredes bloqueadas (ajusta según imagen real)
    paredes = []

    # Pared superior completa
    paredes.append(pygame.Rect(
        0,
        0,
        ANCHO,
        int(ALTO * 200 / 768)
    ))

    # Pared izquierda excepto puerta
    paredes.append(pygame.Rect(
        0,
        int(ALTO * 190 / 768),
        int(ANCHO * 135 / 1366),
        int(ALTO * 60 / 768)
    ))
    paredes.append(pygame.Rect(
        0,
        int(ALTO * 450 / 768),
        int(ANCHO * 135 / 1366),
        int(ALTO * 280 / 768)
    ))

    # Pared derecha completa
    paredes.append(pygame.Rect(
        int(ANCHO * 1200 / 1366),
        0,
        int(ANCHO * 160 / 1366),
        int(ALTO * 325 / 768)
    ))
    paredes.append(pygame.Rect(
        int(ANCHO * 1200/ 1366),
        int(ALTO * 320 / 768),
        int(ANCHO * 160 / 1366),
        int(ALTO * 340 / 768)
    ))

    # Pared inferior excepto puerta
    paredes.append(pygame.Rect(
        0,
        int(ALTO * 580 / 768),
        int(ANCHO * 590 / 1366),
        int(ALTO * 180 / 768)
    ))
    paredes.append(pygame.Rect(
        int(ANCHO * 780 / 1366),
        int(ALTO * 580 / 768),
        int(ANCHO * 600 / 1366),
        int(ALTO * 185 / 768)
    ))

    reloj = pygame.time.Clock()
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Guardar posición previa
        posicion_anterior = jugador.rect.copy()

        teclas = pygame.key.get_pressed()
        jugador.manejar_input(teclas)

        # Verificar colisiones con paredes
        for pared in paredes:
            if jugador.rect.colliderect(pared):
                jugador.rect.topleft = posicion_anterior.topleft
                jugador.x = posicion_anterior.x
                jugador.y = posicion_anterior.y
                break

        pantalla.blit(fondo, (0, 0))
        jugador.dibujar(pantalla)

        # (opcional) Visualiza paredes para debug
        for pared in paredes:
            pygame.draw.rect(pantalla, (255, 0, 0), pared, 2)
        
        # 🧪 Visualizar colisiones para pruebas
        pygame.draw.rect(pantalla, (0, 255, 0), puerta_izquierda, 2)
        pygame.draw.rect(pantalla, (255, 255, 0), puerta_inferior, 2)

        if jugador.rect.colliderect(puerta_izquierda):
            return "juego"

        if jugador.rect.colliderect(puerta_inferior):
            return "sala_energia"

        pygame.display.flip()
        reloj.tick(60)
