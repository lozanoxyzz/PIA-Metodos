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
    respuesta_usuario = ""
    input_activo = False
    click_procesado = False  # evita múltiples envíos con un solo clic
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if modo_interaccion:
                if evento.type == pygame.KEYDOWN and input_activo:
                    if evento.key == pygame.K_BACKSPACE:
                        respuesta_usuario = respuesta_usuario[:-1]
                    elif evento.key == pygame.K_RETURN:
                        pass
                    else:
                        if len(respuesta_usuario) < 20:
                            if evento.unicode.isalnum() or evento.unicode in ".,":
                                respuesta_usuario += evento.unicode

                if evento.type == pygame.MOUSEBUTTONDOWN and not click_procesado:
                    if input_rect.collidepoint(evento.pos):
                        input_activo = True
                    else:
                        input_activo = False

                    if boton_enter.collidepoint(evento.pos):
                        print("✅ Respuesta enviada:", respuesta_usuario)
                        click_procesado = True

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        modo_interaccion = False
                        emisor_chispa.interactuado = False
                        respuesta_usuario = ""
                        input_activo = False

        if modo_interaccion:
            ventana_ancho = int(ANCHO * 1000 / 1366)
            ventana_alto =  int(ALTO * 650 / 768)
            ventana_x = (ANCHO - ventana_ancho) // 2
            ventana_y = (ALTO - ventana_alto) // 2

            pygame.draw.rect(pantalla, (20, 30, 60), (ventana_x, ventana_y, ventana_ancho, ventana_alto))  # fondo
            pygame.draw.rect(pantalla, (0, 255, 255), (ventana_x, ventana_y, ventana_ancho, ventana_alto), 4)  # borde

            # Título: método actual
            font_titulo = pygame.font.SysFont(None, 45, bold=True)
            texto_titulo = font_titulo.render(f"RESUELVE EL PROBLEMA POR EL METODO:", True,
                                              (0, 255, 255))
            pantalla.blit(texto_titulo, (ventana_x + 1100, ventana_y + 130))
            texto_titulo = font_titulo.render(f"{errors.problema[2]}", True,
                                              (0, 255, 255))
            pantalla.blit(texto_titulo, (ventana_x + 1100, ventana_y + 200))

            # Input box
            input_rect = pygame.Rect(ventana_x + 1100, ventana_y + 300, ventana_ancho - 1400, 32)
            pygame.draw.rect(pantalla, (255, 255, 255), input_rect)
            pygame.draw.rect(pantalla, (0, 255, 255), input_rect, 2)

            font_input = pygame.font.SysFont(None, 24)
            render_text = font_input.render(respuesta_usuario, True, (0, 0, 0))
            pantalla.blit(render_text, (input_rect.x + 5, input_rect.y + 5))

            # Botón ENVIAR
            boton_enter = pygame.Rect(input_rect.right + 10, input_rect.y, 100, 32)
            pygame.draw.rect(pantalla, (0, 255, 0), boton_enter)
            texto_boton = font_input.render("ENVIAR", True, (0, 0, 0))
            pantalla.blit(texto_boton, (boton_enter.x + 20, boton_enter.y + 5))

            font = pygame.font.SysFont(None, 24)
            texto = font.render("Presiona ESC para cerrar", True, (255, 255, 255))
            pantalla.blit(texto, (ventana_x + 20, ventana_y + ventana_alto - 40))

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

        if pygame.mouse.get_pressed()[0] == 0:
            click_procesado = False

        if jugador.rect.colliderect(puerta_izquierda):
            return ("sala_principal", "propulsion")

        if jugador.rect.colliderect(puerta_inferior):
            return ("sala_energia", "propulsion")




        pygame.display.flip()
        reloj.tick(60)
