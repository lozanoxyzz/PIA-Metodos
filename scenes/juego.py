import pygame  # Biblioteca principal para gráficos y entrada de usuario
from config import COLOR_TEXTO  # Color del texto configurado en config.py
from utils.background import FondoEspacial  # Fondo animado con estrellas y nave
# Función que representa la escena del juego (nivel activo)
def jugar(pantalla, ancho, alto):
    # Crear fuente del texto usando una fuente del sistema ("consolas")
    fuente = pygame.font.SysFont("consolas", 28)

    # Renderizar texto que aparece en el centro (nivel 1)
    texto = fuente.render("Nivel 1 - ¡Busca los fallos en la nave!", True, COLOR_TEXTO)

    # Crear el fondo espacial animado
    fondo = FondoEspacial(pantalla, ancho, alto)

    # Bucle principal del nivel
    while True:
        # Revisar los eventos del usuario
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"  # Cierra completamente el juego
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return "menu"  # Regresa al menú principal si se presiona ESC
                # Dibujar el fondo animado (estrellas y nave)
        fondo.dibujar()

        # Dibujar el texto centrado horizontalmente
        pantalla.blit(texto, (ancho // 2 - texto.get_width() // 2, alto // 2))

        # Actualizar la pantalla para mostrar los cambios
        pygame.display.flip()

