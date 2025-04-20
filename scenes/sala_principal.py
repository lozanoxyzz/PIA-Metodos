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
    paredes.append(pygame.Rect(0, 0, ANCHO, 200))

    # Pared izquierda excepto puerta
    paredes.append(pygame.Rect(0, 200, 135, 122))      # tramo superior sin puerta
    paredes.append(pygame.Rect(0, 600, 135, ALTO - 600))  # tramo inferior sin puerta

    # Pared derecha excepto puerta
    paredes.append(pygame.Rect(ANCHO - 60, 0, 60, 250))
    paredes.append(pygame.Rect(ANCHO - 60, 430, 60, ALTO - 430))

    # Pared inferior excepto puerta al centro
    paredes.append(pygame.Rect(0, ALTO - 60, ANCHO // 2 - 100, 60))           # izquierda
    paredes.append(pygame.Rect(ANCHO // 2 + 100, ALTO - 60, ANCHO, 60))       # derecha

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
