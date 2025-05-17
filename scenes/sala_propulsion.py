import pygame
import sys
from utils.personaje import Personaje
import utils.errors as errors
sparks = []

def sala_propulsion(pantalla, ANCHO, ALTO, entrada_por="principal"):
    fondo = pygame.image.load("Assets/imagenes/sala_propulsion.png").convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    # VERIFICACION DE ERROR EXISTENTE EN LA SALA
    for error in errors.errores_activos:
        if error[0] == "propulsion":
            emisor_chispa = errors.EmisorChispa(ANCHO * error[1][0] / 1366, ALTO * error[1][1] / 768)

    escala = min(ANCHO / 1366, ALTO / 768)
    
    if entrada_por == "principal":
        jugador = Personaje(
            x=int(ANCHO * 165 / 1366),  # Justo saliendo de la puerta izquierda
            y=int(ALTO * 290 / 768),
            alto_pantalla=ALTO,
            escala=escala
        )
    elif entrada_por == "energia":
        jugador = Personaje(
            x=int(ANCHO * 650 / 1366),  # Justo saliendo de la puerta inferior
            y=int(ALTO * 470 / 768),
            alto_pantalla=ALTO,
            escala=escala
        )
    else:
        jugador = Personaje(x=ANCHO // 2, y=ALTO // 2, alto_pantalla=ALTO, escala=escala)

    # ERRORES
    for error in errors.errores_activos:
        if error[0] == "propulsion":
            print("propulsion")
            ###PINTAR ERROR

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
        int(ALTO * 150 / 768)
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
    modo_interaccion = False
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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

        # DIBUJO DE CHISPAS
        for error in errors.errores_activos:
            if error[0] == "propulsion":
                emisor_chispa.update()
                emisor_chispa.draw(pantalla)

        # (opcional) Visualiza paredes para debug
        for pared in paredes:
            pygame.draw.rect(pantalla, (255, 0, 0), pared, 2)
        
        # 🧪 Visualizar colisiones para pruebas
        pygame.draw.rect(pantalla, (0, 255, 0), puerta_izquierda, 2)
        pygame.draw.rect(pantalla, (255, 255, 0), puerta_inferior, 2)

        # INTERACCION
        for error in errors.errores_activos:
            if error[0] == "propulsion":
                if emisor_chispa.jugador_cerca(jugador.rect):
                    font = pygame.font.SysFont(None, 24)
                    texto = font.render("Presiona F para interactuar", True, (255, 255, 255))
                    pantalla.blit(texto, (20, 20))

                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_f] and not emisor_chispa.interactuado:
                        modo_interaccion = True
                        emisor_chispa.interactuado = True

        if jugador.rect.colliderect(puerta_izquierda):
            return ("sala_principal", "propulsion")

        if jugador.rect.colliderect(puerta_inferior):
            return ("sala_energia", "propulsion")




        pygame.display.flip()
        reloj.tick(60)
