def sala_principal(pantalla, ANCHO, ALTO):
    import pygame
    import sys

    clock = pygame.time.Clock()
    FPS = 60

    # Fondo de la sala
    fondo = pygame.image.load("assets/imagenes/sala_principal.png")
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    # Jugador temporal
    jugador = pygame.Surface((40, 40))
    jugador.fill((255, 100, 100))
    jugador_rect = jugador.get_rect(center=(ANCHO // 2, ALTO // 2))

    velocidad = 5

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
        int(ALTO * 200 / 768),
        int(ANCHO * 135 / 1366),
        int(ALTO * 130 / 768)
    ))
    paredes.append(pygame.Rect(
        0,
        int(ALTO * 440 / 768),
        int(ANCHO * 135 / 1366),
        int(ALTO * 280 / 768)
    ))

    # Pared derecha excepto puerta
    paredes.append(pygame.Rect(
        int(ANCHO * 1228 / 1366),
        0,
        int(ANCHO * 140 / 1366),
        int(ALTO * 340 / 768)
    ))
    paredes.append(pygame.Rect(
        int(ANCHO * 1228 / 1366),
        int(ALTO * 440 / 768),
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

        # Guardar la posición anterior por si hay colisión
        pos_anterior = jugador_rect.copy()

        # Movimiento
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            jugador_rect.x -= velocidad
        if teclas[pygame.K_RIGHT]:
            jugador_rect.x += velocidad
        if teclas[pygame.K_UP]:
            jugador_rect.y -= velocidad
        if teclas[pygame.K_DOWN]:
            jugador_rect.y += velocidad

        # Verificar colisiones con las paredes
        for pared in paredes:
            if jugador_rect.colliderect(pared):
                jugador_rect = pos_anterior  # Revertir movimiento
                break

        # Dibujar todo
        pantalla.blit(fondo, (0, 0))
        pantalla.blit(jugador, jugador_rect)

        # (opcional) Dibujar áreas bloqueadas para depuración
        for pared in paredes:
            pygame.draw.rect(pantalla, (255, 0, 0), pared, 2)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()
