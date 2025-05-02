def sala_principal(pantalla, ANCHO, ALTO, entrada_por="menu"):
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

    if entrada_por == "menu":
        personaje = Personaje(x=ANCHO // 2, y=ALTO // 2, alto_pantalla=ALTO, escala=escala)

    elif entrada_por == "propulsion":
        personaje = Personaje(
            x=int(ANCHO * 1100 / 1366),  # Justo saliendo de la puerta derecha
            y=int(ALTO * 350 / 768),
            alto_pantalla=ALTO,
            escala=escala
        )

    elif entrada_por == "sala_comunicaciones":
        personaje = Personaje(
            x=int(ANCHO * 620 / 1366),  # Justo saliendo de la puerta derecha
            y=int(ALTO * 520 / 768),
            alto_pantalla=ALTO,
            escala=escala
        )

    elif entrada_por == "sala_ventilacion":
        personaje = Personaje(
            x=int(ANCHO * 180 / 1366),  # Justo saliendo de la puerta izquierda
            y=int(ALTO * 340 / 768),
            alto_pantalla=ALTO,
            escala=escala
        )
    
    # Puedes agregar más entradas aquí si en el futuro conectas más puertas:
    # elif entrada_por == "energia":
    #     personaje = Personaje(...)

    else:
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

        
        #Detectar entrada por la puerta derecha (a Sala de Propulsión)
        puerta_derecha_rect = pygame.Rect(
            int(ANCHO * 1228 / 1366),
            int(ALTO * 325 / 768),
            int(ANCHO * 140 / 1366),
            int(ALTO * 140 / 768)
        )

        puerta_inferior_rect = pygame.Rect(
            int(ANCHO * 618 / 1366),
            int(ALTO * 632 / 768),
            int(ANCHO * 133 / 1366),
            int(ALTO * 130 / 768)
        )

        puerta_izquierda_rect = pygame.Rect(
            int(ANCHO * 50 / 1366),
            int(ALTO * 330 / 768),
            int(ANCHO * 90 / 1366),
            int(ALTO * 120 / 768)
        )

        # (opcional) Dibujar áreas bloqueadas para depuración
        for pared in paredes:
            pygame.draw.rect(pantalla, (255, 0, 0), pared, 2)
        
        pygame.draw.rect(pantalla, (0, 255, 0), puerta_derecha_rect, 2)
        pygame.draw.rect(pantalla, (0, 255, 0), puerta_inferior_rect, 2)
        pygame.draw.rect(pantalla, (0, 255, 0), puerta_izquierda_rect, 2)


        if personaje_rect.colliderect(puerta_derecha_rect):
            return "sala_propulsion", "principal"

        if personaje_rect.colliderect(puerta_inferior_rect):
            return "sala_comunicaciones", "principal"
        
        if personaje_rect.colliderect(puerta_izquierda_rect):
            return "sala_ventilacion", "principal"

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()
