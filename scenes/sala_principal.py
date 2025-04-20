def sala_principal(pantalla, ANCHO, ALTO):
    import pygame
    import sys
    from utils.personaje import Personaje  # Importar clase Personaje

    clock = pygame.time.Clock()
    FPS = 60

    # Fondo de la sala
    fondo = pygame.image.load("assets/imagenes/sala_principal.png")
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    # Crear personaje
    escala = min(ANCHO / 1366, ALTO / 768)
    personaje = Personaje(x=ANCHO // 2, y=ALTO // 2, alto_pantalla=ALTO, escala=escala)

    # Áreas bloqueadas (paredes sin puertas)
    paredes = []

    # Pared superior completa (consolas, no hay puerta)
    paredes.append(pygame.Rect(
        0,
        0,
        ANCHO,
        int(ALTO * 200 / 768)
    ))

    # Pared izquierda excepto puerta
    paredes.append(pygame.Rect(
        0,
        int(ALTO * 198 / 768),
        int(ANCHO * 135 / 1366),
        int(ALTO * 130 / 768)
    ))
    paredes.append(pygame.Rect(
        0,
        int(ALTO * 450 / 768),
        int(ANCHO * 135 / 1366),
        int(ALTO * 280 / 768)
    ))

    # Pared derecha excepto puerta
    paredes.append(pygame.Rect(
        int(ANCHO * 1228 / 1366),
        0,
        int(ANCHO * 140 / 1366),
        int(ALTO * 325 / 768)
    ))
    paredes.append(pygame.Rect(
        int(ANCHO * 1228 / 1366),
        int(ALTO * 465 / 768),
        int(ANCHO * 140 / 1366),
        int(ALTO * 280 / 768)
    ))

    # Pared inferior excepto puerta al centro
    paredes.append(pygame.Rect(
        0,
        int(ALTO * 633 / 768),
        int(ANCHO * 620 / 1366),
        int(ALTO * 130 / 768)
    ))
    paredes.append(pygame.Rect(
        int(ANCHO * 750 / 1366),
        int(ALTO * 633 / 768),
        int(ANCHO * 600 / 1366),
        int(ALTO * 130 / 768)
    ))

    jugando = True
    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"

        # Guardar posición anterior
        posicion_anterior = pygame.Rect(personaje.x, personaje.y, personaje.imagen_actual.get_width()
                                        , personaje.imagen_actual.get_height())

        # Movimiento
        teclas = pygame.key.get_pressed()
        personaje.manejar_input(teclas)

        # Verificar colisiones
        personaje_rect = pygame.Rect(personaje.x, personaje.y, personaje.imagen_actual.get_width()
                                     , personaje.imagen_actual.get_height())
        for pared in paredes:
            if personaje_rect.colliderect(pared):
                personaje.x = posicion_anterior.x
                personaje.y = posicion_anterior.y
                break

        # Dibujar todo
        pantalla.blit(fondo, (0, 0))
        personaje.dibujar(pantalla)

        # (opcional) Dibujar áreas bloqueadas para depuración
        for pared in paredes:
            pygame.draw.rect(pantalla, (255, 0, 0), pared, 2)

        # Detectar entrada por la puerta derecha (a Sala de Propulsión)
        puerta_derecha_rect = pygame.Rect(
            int(ANCHO * 1228 / 1366),
            int(ALTO * 325 / 768),
            int(ANCHO * 140 / 1366),
            int(ALTO * 140 / 768)
        )

        if personaje_rect.colliderect(puerta_derecha_rect):
            return "sala_propulsion" 

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()
