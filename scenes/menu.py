import pygame          # Biblioteca principal para gráficos, sonido y entradas
import math            # Para usar funciones como seno en animaciones
from config import COLOR_TEXTO, COLOR_BOTON  # Colores definidos en config.py
from utils.background import FondoEspacial   # Fondo espacial con estrellas y nave
# Función que muestra el menú principal del juego
def mostrar_menu(pantalla, ancho, alto):
    # Cargar fuentes personalizadas para título, subtítulo y botones
    fuente_titulo = pygame.font.Font("assets/fonts/Orbitron-Regular.ttf", 70)
    fuente_subtitulo = pygame.font.Font("assets/fonts/Orbitron-Regular.ttf", 55)
    fuente_botones = pygame.font.Font("assets/fonts/Audiowide-Regular.ttf", 40)

    # Crear fondo animado (estrellas y nave flotando)
    fondo = FondoEspacial(pantalla, ancho, alto)

    # Posiciones base para los botones
    base_y = alto // 2 + 85
    boton_jugar = pygame.Rect(ancho // 2 - 100, base_y, 200, 50)
    boton_salir = pygame.Rect(ancho // 2 - 100, base_y + 70, 200, 50)

    # Bucle principal del menú
    while True:
        # Manejo de eventos del usuario
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"  # Cierra el juego
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return "salir"  # Tecla ESC cierra el juego
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(evento.pos):
                    return "juego"  # Cambia a la escena de juego
                if boton_salir.collidepoint(evento.pos):
                    return "salir"

        # Dibujar fondo espacial animado
        fondo.dibujar()

        # Definir colores entre los que oscilará el título
        color_base = (180, 100, 255)
        color_brillo = (255, 160, 255)

        # Oscilación del color con seno para el título principal
        t = (math.sin(pygame.time.get_ticks() * 0.002) + 1) / 2
        r = int(color_base[0] + (color_brillo[0] - color_base[0]) * t)
        g = int(color_base[1] + (color_brillo[1] - color_base[1]) * t)
        b = int(color_base[2] + (color_brillo[2] - color_base[2]) * t)
        color_dinamico = (r, g, b)

        # Oscilación de color para subtítulo con desfase
        t_sub = (math.sin(pygame.time.get_ticks() * 0.002 + 2) + 1) / 2
        r2 = int(color_base[0] + (color_brillo[0] - color_base[0]) * t_sub)
        g2 = int(color_base[1] + (color_brillo[1] - color_base[1]) * t_sub)
        b2 = int(color_base[2] + (color_brillo[2] - color_base[2]) * t_sub)
        color_dinamico_sub = (r2, g2, b2)

        # Renderizado del título con color animado y sombra
        texto_titulo = fuente_titulo.render("Reparación de Emergencia", True, color_dinamico)
        texto_sombra = fuente_titulo.render("Reparación de Emergencia", True, (0, 0, 0))

        # Renderizado del subtítulo con color animado y sombra
        texto_sub_sombra = fuente_subtitulo.render("Misión Métodos Numéricos", True, (0, 0, 0))
        texto_sub = fuente_subtitulo.render("Misión Métodos Numéricos", True, color_dinamico_sub)

        # Padding del panel donde está el título
        padding_x = 40
        padding_y = 20

        # Tamaño automático del panel basado en los textos
        ancho_panel = max(texto_titulo.get_width(), texto_sub.get_width()) + padding_x * 2
        alto_panel = texto_titulo.get_height() + texto_sub.get_height() + padding_y * 3

        # Posición centrada del panel
        panel_x = ancho // 2 - ancho_panel // 2
        panel_y = alto // 5 - 20

        # Crear panel semitransparente para el título
        panel = pygame.Surface((ancho_panel, alto_panel), pygame.SRCALPHA)
        panel.fill((0, 0, 0, 180))  # Negro con transparencia
        pantalla.blit(panel, (panel_x, panel_y))

        # Animación de borde azul pulsante
        t_borde = (math.sin(pygame.time.get_ticks() * 0.004) + 1) / 2
        brillo = int(100 + 155 * t_borde)
        color_borde = (brillo, brillo, 255)

        # Dibujar borde del panel con resplandor
        pygame.draw.rect(
            pantalla,
            color_borde,
            (panel_x, panel_y, ancho_panel, alto_panel),
            width=4,
            border_radius=12
        )

        # Posición del título centrado dentro del panel
        x_titulo = ancho // 2 - texto_titulo.get_width() // 2
        y_titulo = panel_y + 15
        pantalla.blit(texto_sombra, (x_titulo + 3, y_titulo + 3))  # Sombra
        pantalla.blit(texto_titulo, (x_titulo, y_titulo))          # Texto principal

        # Posición del subtítulo debajo del título
        x_sub = ancho // 2 - texto_sub.get_width() // 2
        y_sub = y_titulo + texto_titulo.get_height() + 10
        pantalla.blit(texto_sub_sombra, (x_sub + 3, y_sub + 3))  # Sombra
        pantalla.blit(texto_sub, (x_sub, y_sub))                # Texto principal

        # Renderizar texto de los botones
        texto_jugar = fuente_botones.render("Iniciar Misión", True, COLOR_TEXTO)
        texto_salir = fuente_botones.render("Salir", True, COLOR_TEXTO)

        # Padding interno para los botones
        padding_x = 30
        padding_y = 10

        # Ajustar tamaño y posición del botón JUGAR
        boton_jugar = pygame.Rect(
            ancho // 2 - (texto_jugar.get_width() + padding_x * 2) // 2,
            base_y,
            texto_jugar.get_width() + padding_x * 2,
            texto_jugar.get_height() + padding_y * 2
        )

        # Ajustar tamaño y posición del botón SALIR
        boton_salir = pygame.Rect(
            ancho // 2 - (texto_salir.get_width() + padding_x * 2) // 2,
            base_y + boton_jugar.height + 20,
            texto_salir.get_width() + padding_x * 2,
            texto_salir.get_height() + padding_y * 2
        )

        # Dibujar los botones con color y bordes redondeados
        pygame.draw.rect(pantalla, COLOR_BOTON, boton_jugar, border_radius=8)
        pygame.draw.rect(pantalla, COLOR_BOTON, boton_salir, border_radius=8)

        # Dibujar el texto sobre los botones
        pantalla.blit(texto_jugar, (boton_jugar.x + padding_x, boton_jugar.y + padding_y))
        pantalla.blit(texto_salir, (boton_salir.x + padding_x, boton_salir.y + padding_y))

        # Refrescar pantalla para mostrar los cambios
        pygame.display.flip()
