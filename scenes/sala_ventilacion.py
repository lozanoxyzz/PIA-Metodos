import pygame
import sys
from utils.personaje import Personaje
import utils.errors as errors
sparks = []

def sala_ventilacion(pantalla, ANCHO, ALTO, entrada_por="principal"):
    fondo = pygame.image.load("Assets/imagenes/sala_ventilacion.png").convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    # VERIFICACION DE ERROR EXISTENTE EN LA SALA
    for error in errors.errores_activos:
        if error[0] == "ventilacion":
            emisor_chispa = errors.EmisorChispa(ANCHO * error[1][0] / 1366, ALTO * error[1][1] / 768)

    escala = min(ANCHO / 1366, ALTO / 768)

    # 🎮 Posición inicial del jugador según puerta de entrada
    if entrada_por == "principal":
        jugador = Personaje(
            x=int(ANCHO * 1100 / 1366),  # entrando por la derecha
            y=int(ALTO * 310 / 768),
            alto_pantalla=ALTO,
            escala=escala
        )
    elif entrada_por == "sala_vigilancia":
        jugador = Personaje(
            x=int(ANCHO * 680 / 1366),
            y=int(ALTO * 450 / 768),
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

    # 🟩 Puerta inferior
    puerta_inferior = pygame.Rect(
        int(ANCHO * 570 / 1366),
        int(ALTO * 600 / 768),
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

    # Pared inferior (excepto puerta)
    paredes.append(pygame.Rect(
        0,
        int(ALTO * 600 / 768),
        int(ANCHO * 570 / 1366),
        int(ALTO * 100 / 768)
    ))
    paredes.append(pygame.Rect(
        int(ANCHO * 800 / 1366),
        int(ALTO * 580 / 768),
        int(ANCHO * 546 / 1366),
        int(ALTO * 100 / 768)
    ))

    # Pared izquierda completa
    paredes.append(pygame.Rect(0, 0, int(ANCHO * 450 / 1366), int(ALTO * 200 / 768)))
    paredes.append(pygame.Rect(0, 370, int(ANCHO * 450 / 1366), int(ALTO * 250 / 768)))
    paredes.append(pygame.Rect(0, 210 , int(ANCHO * 330 / 1366), int(ALTO * 160 / 768)))


    # Pared superior completa
    paredes.append(pygame.Rect(0, 0, ANCHO, int(ALTO * 150 / 768)))

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

        # DIBUJO DE CHISPAS
        for error in errors.errores_activos:
            if error[0] == "ventilacion":
                emisor_chispa.update()
                emisor_chispa.draw(pantalla)

        #INTERACCION
        for error in errors.errores_activos:
            if error[0] == "ventilacion":
                if emisor_chispa.jugador_cerca(jugador.rect):
                    font = pygame.font.SysFont(None, 24)
                    texto = font.render("Presiona F para interactuar", True, (255, 255, 255))
                    pantalla.blit(texto, (20, 20))

                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_f] and not emisor_chispa.interactuado:
                        print("⚡ ¡Has interactuado con la chispa!")
                        emisor_chispa.interactuado = True  # evita repetir acción


        # Visualizar puertas
        pygame.draw.rect(pantalla, (0, 128, 255), puerta_derecha, 2)     # Azul = puerta derecha
        pygame.draw.rect(pantalla, (0, 255, 0), puerta_inferior, 2)      # Verde = puerta inferior

        # Visualizar colisiones
        for pared in paredes:
            pygame.draw.rect(pantalla, (255, 0, 0), pared, 2)

        # Transiciones de sala
        if jugador.rect.colliderect(puerta_derecha):
            return ("sala_principal", "sala_ventilacion")

        if jugador.rect.colliderect(puerta_inferior):
            return ("sala_vigilancia", "sala_ventilacion")  # reemplaza "sala_x" con la siguiente sala real

        pygame.display.flip()
        reloj.tick(60)
