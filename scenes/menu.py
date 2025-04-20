import pygame
import math
from config import COLOR_TEXTO, COLOR_BOTON
from utils.background import FondoEspacial

def mostrar_menu(pantalla, ancho, alto):
    # Resolución base para escalar
    BASE_ANCHO = 1366
    BASE_ALTO = 768
    escala = min(ancho / BASE_ANCHO, alto / BASE_ALTO)

    # Escalar tamaño de fuente
    fuente_titulo = pygame.font.Font("assets/fonts/Orbitron-Regular.ttf", int(70 * escala))
    fuente_subtitulo = pygame.font.Font("assets/fonts/Orbitron-Regular.ttf", int(55 * escala))
    fuente_botones = pygame.font.Font("assets/fonts/Audiowide-Regular.ttf", int(40 * escala))

    fondo = FondoEspacial(pantalla, ancho, alto, escala=escala)  # Pasamos la escala al fondo

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return "salir"
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(evento.pos):
                    return "juego"
                if boton_salir.collidepoint(evento.pos):
                    return "salir"

        fondo.dibujar()

        color_base = (180, 100, 255)
        color_brillo = (255, 160, 255)

        t = (math.sin(pygame.time.get_ticks() * 0.002) + 1) / 2
        r = int(color_base[0] + (color_brillo[0] - color_base[0]) * t)
        g = int(color_base[1] + (color_brillo[1] - color_base[1]) * t)
        b = int(color_base[2] + (color_brillo[2] - color_base[2]) * t)
        color_dinamico = (r, g, b)

        t_sub = (math.sin(pygame.time.get_ticks() * 0.002 + 2) + 1) / 2
        r2 = int(color_base[0] + (color_brillo[0] - color_base[0]) * t_sub)
        g2 = int(color_base[1] + (color_brillo[1] - color_base[1]) * t_sub)
        b2 = int(color_base[2] + (color_brillo[2] - color_base[2]) * t_sub)
        color_dinamico_sub = (r2, g2, b2)

        texto_titulo = fuente_titulo.render("Reparación de Emergencia", True, color_dinamico)
        texto_sombra = fuente_titulo.render("Reparación de Emergencia", True, (0, 0, 0))

        texto_sub_sombra = fuente_subtitulo.render("Misión Métodos Numéricos", True, (0, 0, 0))
        texto_sub = fuente_subtitulo.render("Misión Métodos Numéricos", True, color_dinamico_sub)

        padding_x = int(40 * escala)
        padding_y = int(20 * escala)

        ancho_panel = max(texto_titulo.get_width(), texto_sub.get_width()) + padding_x * 2
        alto_panel = texto_titulo.get_height() + texto_sub.get_height() + padding_y * 3

        panel_x = ancho // 2 - ancho_panel // 2
        panel_y = int(alto * 0.2)

        panel = pygame.Surface((ancho_panel, alto_panel), pygame.SRCALPHA)
        panel.fill((0, 0, 0, 180))
        pantalla.blit(panel, (panel_x, panel_y))

        t_borde = (math.sin(pygame.time.get_ticks() * 0.004) + 1) / 2
        brillo = int(100 + 155 * t_borde)
        color_borde = (brillo, brillo, 255)

        pygame.draw.rect(
            pantalla,
            color_borde,
            (panel_x, panel_y, ancho_panel, alto_panel),
            width=4,
            border_radius=12
        )

        x_titulo = ancho // 2 - texto_titulo.get_width() // 2
        y_titulo = panel_y + int(15 * escala)
        pantalla.blit(texto_sombra, (x_titulo + 3, y_titulo + 3))
        pantalla.blit(texto_titulo, (x_titulo, y_titulo))

        x_sub = ancho // 2 - texto_sub.get_width() // 2
        y_sub = y_titulo + texto_titulo.get_height() + int(10 * escala)
        pantalla.blit(texto_sub_sombra, (x_sub + 3, y_sub + 3))
        pantalla.blit(texto_sub, (x_sub, y_sub))

        texto_jugar = fuente_botones.render("Iniciar Misión", True, COLOR_TEXTO)
        texto_salir = fuente_botones.render("Salir", True, COLOR_TEXTO)

        padding_btn_x = int(30 * escala)
        padding_btn_y = int(10 * escala)

        base_y = int(alto * 0.6)

        boton_jugar = pygame.Rect(
            ancho // 2 - (texto_jugar.get_width() + padding_btn_x * 2) // 2,
            base_y,
            texto_jugar.get_width() + padding_btn_x * 2,
            texto_jugar.get_height() + padding_btn_y * 2
        )

        boton_salir = pygame.Rect(
            ancho // 2 - (texto_salir.get_width() + padding_btn_x * 2) // 2,
            base_y + boton_jugar.height + int(20 * escala),
            texto_salir.get_width() + padding_btn_x * 2,
            texto_salir.get_height() + padding_btn_y * 2
        )

        pygame.draw.rect(pantalla, COLOR_BOTON, boton_jugar, border_radius=8)
        pygame.draw.rect(pantalla, COLOR_BOTON, boton_salir, border_radius=8)

        pantalla.blit(texto_jugar, (boton_jugar.x + padding_btn_x, boton_jugar.y + padding_btn_y))
        pantalla.blit(texto_salir, (boton_salir.x + padding_btn_x, boton_salir.y + padding_btn_y))

        pygame.display.flip()
