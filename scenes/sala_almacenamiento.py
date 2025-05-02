import pygame
import sys
from utils.personaje import Personaje
import utils.errors as errors


def sala_almacenamiento(pantalla, ANCHO, ALTO, entrada_por="principal"):
    fondo = pygame.image.load("Assets/imagenes/sala_almacenamiento.jpeg").convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    escala = min(ANCHO / 1366, ALTO / 768)
    # 📍 Posicionar al personaje según desde dónde entra
    if entrada_por == "sala_comunicaciones":
        jugador = Personaje(
            x=int(ANCHO * 650 / 1366),
            y=int(ALTO * 190 / 768),
            alto_pantalla=ALTO,
            escala=escala
        )

    else:
        jugador = Personaje(x=ANCHO // 2, y=ALTO // 2, alto_pantalla=ALTO, escala=escala)


    #ERRORES
    for error in errors.errores_activos:
        if error[0] == "almacenamiento":
            print("almacenamiento")
            ###PINTAR ERROR

    # 🟦 Puerta superior
    puerta_superior = pygame.Rect(
        int(ANCHO * 564 / 1366),
        0,
        int(ANCHO * 235 / 1366),
        int(ALTO * 90 / 768)
    )

    # 🟦 Puerta inferior
    puerta_inferior = pygame.Rect(
        int(ANCHO * 564 / 1366),
        int(ALTO * 590 / 768),
        int(ANCHO * 235 / 1366),
        int(ALTO * 190 / 768)
    )
    int(ALTO * 675 / 768),

    # 🧱 Paredes bloqueadas (ajustar con la imagen final si cambian elementos)
    paredes = []

    # Pared izquierda excepto puerta
    paredes.append(pygame.Rect(
        0,
        0,
        int(ANCHO * 100 / 1366),
        int(ALTO * 650 / 768)
    ))
  
    # Pared superior excepto puerta
    paredes.append(pygame.Rect(
        0,
        0,
        int(ANCHO * 563 / 1366),
        int(ALTO * 90 / 768)
    ))
    
    paredes.append(pygame.Rect(
        int(ANCHO * 800 / 1366),
        0,
        int(ANCHO * 800 / 1366),
        int(ALTO * 90 / 768)
    ))

  
    #Pared derecha sin puertas
    paredes.append(pygame.Rect(
        int(ANCHO * 1250 / 1366),
        0,
        int(ANCHO * 150 / 1366),
        int(ALTO * 650 / 768)
    ))
    
    # Pared inferior
    paredes.append(pygame.Rect(
        0,
        int(ALTO * 588 / 768),
        int(ANCHO * 563 / 1366),
        int(ALTO * 190 / 768)
    ))
    paredes.append(pygame.Rect(
        int(ANCHO * 800 / 1366),
        int(ALTO * 588 / 768),
        int(ANCHO * 800 / 1366),
        int(ALTO * 190 / 768)
    ))

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
      
        pygame.draw.rect(pantalla, (0, 128, 255), puerta_superior, 2)  # Azul = puerta superior
        pygame.draw.rect(pantalla, (0, 128, 255), puerta_inferior, 2)  # Azul = puerta inferior
       

        # Visualizar paredes (colisiones)
        for pared in paredes:
            pygame.draw.rect(pantalla, (255, 0, 0), pared, 2)  # Rojo = pared (colisión)

      

        if jugador.rect.colliderect(puerta_superior):
            return ("sala_comunicaciones", "almacenamiento")  # Reemplaza con la sala correspondiente
        
        if jugador.rect.colliderect(puerta_inferior):
            return ("sala_almacenamiento", "sala_almacenamiento")

        pygame.display.flip()
        reloj.tick(60)