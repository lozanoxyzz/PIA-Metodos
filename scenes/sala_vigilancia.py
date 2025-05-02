import pygame
import sys
from utils.personaje import Personaje

def sala_vigilancia(pantalla, ANCHO, ALTO, entrada_por="principal"):
    fondo = pygame.image.load("Assets/imagenes/sala_vigilancia.png").convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    escala = min(ANCHO / 1366, ALTO / 768)

    # 🎮 Posición inicial del jugador según puerta de entrada
    if entrada_por == "sala_ventilacion":
        jugador = Personaje(
            x=int(ANCHO * 700 / 1366),  # entrando por la derecha
            y=int(ALTO * 250 / 768),
            alto_pantalla=ALTO,
            escala=escala
        )
    elif entrada_por == "sala_comunicaciones":
        jugador = Personaje(
            x=int(ANCHO * 1100 / 1366),
            y=int(ALTO * 350 / 768),
            alto_pantalla=ALTO,
            escala=escala
        )
    else:
        jugador = Personaje(x=ANCHO // 2, y=ALTO // 2, alto_pantalla=ALTO, escala=escala)

    # 🟦 Puerta derecha
    puerta_derecha = pygame.Rect(
        int(ANCHO * 1250 / 1366),
        int(ALTO * 250 / 768),
        int(ANCHO * 120 / 1366),
        int(ALTO * 200 / 768)
    )

    # 🟩 Puerta superior
    puerta_superior = pygame.Rect(
        int(ANCHO * 550 / 1366),
        int(ALTO * 50 / 768),
        int(ANCHO * 230 / 1366),
        int(ALTO * 150 / 768)
    )

    # 🧱 Colisiones
    paredes = []

    # Pared derecha (excepto puerta)
    paredes.append(pygame.Rect(
        int(ANCHO * 1250 / 1366),
        0,
        int(ANCHO * 120 / 1366),
        int(ALTO * 250 / 768)
    ))
    paredes.append(pygame.Rect(
        int(ANCHO * 1250 / 1366),
        int(ALTO * 450 / 768),
        int(ANCHO * 120 / 1366),
        int(ALTO * 318 / 768)
    ))

    # Pared superior (excepto puerta)
    paredes.append(pygame.Rect(
        0,
        int(ALTO * 50 / 768),
        int(ANCHO * 550 / 1366),
        int(ALTO * 160 / 768)
    ))
    paredes.append(pygame.Rect(
        int(ANCHO * 780 / 1366),
        int(ALTO * 50 / 768),
        int(ANCHO * 546 / 1366),
        int(ALTO * 100 / 768)
    ))

    # Pared izquierda completa
    paredes.append(pygame.Rect(0, 0, int(ANCHO * 120 / 1366), int(ALTO * 700 / 768)))
    
    # Pared inferior completa
    paredes.append(pygame.Rect(0, int(ALTO * 650 / 768), ANCHO, int(ALTO * 100 / 768)))

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
        pygame.draw.rect(pantalla, (0, 128, 255), puerta_derecha, 2)     # Azul = puerta derecha
        pygame.draw.rect(pantalla, (0, 255, 0), puerta_superior, 2)      # Verde = puerta inferior

        # Visualizar colisiones
        for pared in paredes:
            pygame.draw.rect(pantalla, (255, 0, 0), pared, 2)

        # Transiciones de sala
        if jugador.rect.colliderect(puerta_derecha):
            return ("sala_comunicaciones", "sala_vigilancia")

        if jugador.rect.colliderect(puerta_superior):
            return ("sala_ventilacion", "sala_vigilancia")  # reemplaza "sala_x" con la siguiente sala real

        pygame.display.flip()
        reloj.tick(60)
