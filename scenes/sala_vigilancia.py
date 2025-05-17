import pygame
import sys
from utils.personaje import Personaje
import utils.errors as errors
sparks = []



def sala_vigilancia(pantalla, ANCHO, ALTO, entrada_por="principal"):
    fondo = pygame.image.load("Assets/imagenes/sala_vigilancia.png").convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    # VERIFICACION DE ERROR EXISTENTE EN LA SALA
    for error in errors.errores_activos:
        if error[0] == "vigilancia":
            emisor_chispa = errors.EmisorChispa(ANCHO * error[1][0] / 1366, ALTO * error[1][1] / 768)

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

    # ERRORES
    for error in errors.errores_activos:
        if error[0] == "vigilancia":
            print("vigilancia")
            ###PINTAR ERROR

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
        int(ALTO * 100 / 768)
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
        int(ALTO * 100 / 768)
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
    modo_interaccion = False
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Salir del modo de interacción con ESC
            if modo_interaccion and evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    modo_interaccion = False
                    emisor_chispa.interactuado = False

        if modo_interaccion:
            ventana_ancho = int(ANCHO * 1000 / 1366)
            ventana_alto =  int(ALTO * 650 / 768)
            ventana_x = (ANCHO - ventana_ancho) // 2
            ventana_y = (ALTO - ventana_alto) // 2

            pygame.draw.rect(pantalla, (20, 30, 60), (ventana_x, ventana_y, ventana_ancho, ventana_alto))  # fondo
            pygame.draw.rect(pantalla, (0, 255, 255), (ventana_x, ventana_y, ventana_ancho, ventana_alto), 4)  # borde

            font = pygame.font.SysFont(None, 24)
            texto = font.render("Presiona ESC para cerrar", True, (255, 255, 255))
            pantalla.blit(texto, (ventana_x + 20, ventana_y + ventana_alto - 40))

            # Si ya tienes una imagen:
            img = pygame.image.load("Assets/imagenes_problemas/imagen_prueba.jpeg")
            img_escalada = pygame.transform.scale(img, (int(ANCHO * 400 / 1366), int(ALTO * 600 / 768)))
            pantalla.blit(img_escalada, (ventana_x + 20, ventana_y + 20))

            pygame.display.flip()
            reloj.tick(60)
            continue  # <- Muy importante: detiene el juego mientras esté activa la ventana

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
            if error[0] == "vigilancia":
                emisor_chispa.update()
                emisor_chispa.draw(pantalla)

        # Visualizar puertas
        pygame.draw.rect(pantalla, (0, 128, 255), puerta_derecha, 2)     # Azul = puerta derecha
        pygame.draw.rect(pantalla, (0, 255, 0), puerta_superior, 2)      # Verde = puerta inferior

        #INTERACCION
        for error in errors.errores_activos:
            if error[0] == "vigilancia":
                if emisor_chispa.jugador_cerca(jugador.rect):
                    font = pygame.font.SysFont(None, 24)
                    texto = font.render("Presiona F para interactuar", True, (255, 255, 255))
                    pantalla.blit(texto, (20, 20))

                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_f] and not emisor_chispa.interactuado:
                        modo_interaccion = True
                        emisor_chispa.interactuado = True

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
