import pygame
import sys
from utils.personaje import Personaje

def sala_energia(pantalla, ANCHO, ALTO):
    fondo = pygame.image.load("Assets/imagenes/sala_energia.png").convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    escala = min(ANCHO / 1366, ALTO / 768)
    
    jugador = Personaje(
    x=int(ANCHO * 760 / 1366),
    y=int(ALTO * 120 / 768),
    alto_pantalla=ALTO,
    escala=escala
    )

    # 🟩 Puerta izquierda
    puerta_izquierda = pygame.Rect(
        0,
        int(ALTO * 250 / 768),
        int(ANCHO * 120 / 1366),
        int(ALTO * 200 / 768)
    )

    # 🟦 Puerta superior
    puerta_superior = pygame.Rect(
        int(ANCHO * 690 / 1366),
        0,
        int(ANCHO * 180 / 1366),
        int(ALTO * 100 / 768)
    )

    # 🧱 Paredes bloqueadas (ajustar con la imagen final si cambian elementos)
    paredes = []

    # Pared izquierda excepto puerta
    paredes.append(pygame.Rect(
        0,
        0,
        int(ANCHO * 120 / 1366),
        int(ALTO * 250 / 768)
    ))
    paredes.append(pygame.Rect(
        0,
        int(ALTO * 450 / 768),
        int(ANCHO * 120 / 1366),
        int(ALTO * 320 / 768)
    ))

    # Pared superior excepto puerta
    paredes.append(pygame.Rect(
        0,
        0,
        int(ANCHO * 680 / 1366),
        int(ALTO * 100 / 768)
    ))
    paredes.append(pygame.Rect(
        int(ANCHO * 870 / 1366),
        0,
        int(ANCHO * 500 / 1366),
        int(ALTO * 100 / 768)
    ))

    # Pared derecha completa
    paredes.append(pygame.Rect(
        int(ANCHO * 1260 / 1366),
        0,
        int(ANCHO * 120 / 1366),
        ALTO
    ))

    # Pared inferior completa
    paredes.append(pygame.Rect(
        0,
        int(ALTO * 940 / 768),
        ANCHO,
        int(ALTO * 100 / 768)
    ))

    reloj = pygame.time.Clock()
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        posicion_anterior = jugador.rect.copy()
        teclas = pygame.key.get_pressed()
        jugador.manejar_input(teclas)

        for pared in paredes:
            if jugador.rect.colliderect(pared):
                jugador.rect.topleft = posicion_anterior.topleft
                jugador.x = posicion_anterior.x
                jugador.y = posicion_anterior.y
                break

        pantalla.blit(fondo, (0, 0))
        jugador.dibujar(pantalla)

        # Visualizar puertas
        pygame.draw.rect(pantalla, (0, 255, 0), puerta_izquierda, 2)     # Verde = puerta izquierda
        pygame.draw.rect(pantalla, (0, 128, 255), puerta_superior, 2)    # Azul = puerta superior

        # Visualizar paredes (colisiones)
        for pared in paredes:
            pygame.draw.rect(pantalla, (255, 0, 0), pared, 2)            # Rojo = pared (colisión)
        if jugador.rect.colliderect(puerta_izquierda):
            return "sala_propulsion"

        if jugador.rect.colliderect(puerta_superior):
            return "otra_sala"  # Reemplaza con la sala correspondiente

        pygame.display.flip()
        reloj.tick(60)
