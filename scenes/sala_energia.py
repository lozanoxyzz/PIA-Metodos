import pygame
import sys
from utils.personaje import Personaje

def sala_energia(pantalla, ANCHO, ALTO, entrada_por="propulsion"):
    fondo = pygame.image.load("Assets/imagenes/sala_energia.png").convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    escala = min(ANCHO / 1366, ALTO / 768)
    # 📍 Posicionar al personaje según desde dónde entra
    if entrada_por == "propulsion":
        jugador = Personaje(
            x=int(ANCHO * 650 / 1366),
            y=int(ALTO * 140 / 768),
            alto_pantalla=ALTO,
            escala=escala
        )
    elif entrada_por == "otra_sala":
        jugador = Personaje(
            x=int(ANCHO * 670 / 1366),
            y=int(ALTO * 120 / 768),
            alto_pantalla=ALTO,
            escala=escala
        )
    else:
        jugador = Personaje(x=ANCHO // 2, y=ALTO // 2, alto_pantalla=ALTO, escala=escala)

    # 🟩 Puerta izquierda
    puerta_izquierda = pygame.Rect(
        0,
        int(ALTO * 250 / 768),
        int(ANCHO * 120 / 1366),
        int(ALTO * 200 / 768)
    )

    # 🟦 Puerta superior
    puerta_superior = pygame.Rect(
        int(ANCHO * 564 / 1366),
        0,
        int(ANCHO * 235 / 1366),
        int(ALTO * 120 / 768)
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
        int(ANCHO * 563 / 1366),
        int(ALTO * 190 / 768)
    ))
    paredes.append(pygame.Rect(
        int(ANCHO * 800 / 1366),
        0,
        int(ANCHO * 800 / 1366),
        int(ALTO * 190 / 768)
    ))

    # Pared derecha completa
    paredes.append(pygame.Rect(
        int(ANCHO * 1290 / 1366),
        0,
        int(ANCHO * 120 / 1366),
        ALTO
    ))

    # Pared inferior completa
    paredes.append(pygame.Rect(
        0,
        int(ALTO * 675 / 768),
        ANCHO,
        int(ALTO * 100 / 768)
    ))

    cuadro_central = pygame.Rect(
        ANCHO // 2 - 150,  # centro menos la mitad del ancho
        ALTO // 2 - 80,   # centro menos la mitad del alto
        300,
        250
    )
    paredes.append(cuadro_central)

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
       
        pygame.draw.rect(pantalla, (255, 0, 0), cuadro_central, 2)

        if jugador.rect.colliderect(puerta_izquierda):
            return ("otra_sala", "energia")

        if jugador.rect.colliderect(puerta_superior):
            return ("sala_propulsion", "energia")  # Reemplaza con la sala correspondiente

        pygame.display.flip()
        reloj.tick(60)
