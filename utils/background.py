import pygame          # Biblioteca para gráficos, imágenes y pantalla
import random          # Para generar posiciones y velocidades aleatorias
import math            # Para usar seno, coseno y rotaciones

class Estrella:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.reset()  # Inicializa la estrella con valores aleatorios
    def reset(self):
        # Posición aleatoria dentro de la pantalla
        self.x = random.randint(0, self.ancho)
        self.y = random.randint(0, self.alto)

        # Velocidad aleatoria total
        velocidad_total = random.uniform(0.5, 3.0)

        # Dirección aleatoria (ángulo en radianes)
        angulo = random.uniform(0, 2 * 3.1416)

        # Velocidad descompuesta en x y y
        self.dx = velocidad_total * math.cos(angulo)
        self.dy = velocidad_total * math.sin(angulo)

        # Tamaño aleatorio de la estrella
        self.tamano = random.randint(1, 3)

        # Color blanco brillante aleatorio (intensidad variable)
        intensidad = random.randint(180, 255)
        self.color = (intensidad, intensidad, intensidad)
    def actualizar(self):
        # Mover la estrella en su dirección
        self.x += self.dx
        self.y += self.dy

        # Si sale de pantalla, se reinicia en una nueva posición aleatoria
        if self.x < 0 or self.x > self.ancho or self.y < 0 or self.y > self.alto:
            self.reset()
    def dibujar(self, pantalla):
        # Dibuja un pequeño círculo como estrella
        pygame.draw.circle(pantalla, self.color, (int(self.x), int(self.y)), self.tamano)
class FondoEspacial:
    def __init__(self, pantalla, ancho, alto, cantidad_estrellas=100, escala=1.0):
        self.pantalla = pantalla
        self.ancho = ancho
        self.alto = alto

        # Crea una lista de estrellas animadas
        self.estrellas = [Estrella(ancho, alto) for _ in range(cantidad_estrellas)]

        # Carga la imagen de la nave
        original = pygame.image.load("assets/imagenes/nave-menu2.png").convert_alpha()
        tamaño = int(200 * escala)
        self.nave_imagen = pygame.transform.scale(original, (tamaño, tamaño))

        # Escala la nave a un tamaño manejable
        self.nave_imagen = pygame.transform.scale(original, (200, 200))

        # Posición inicial de la nave
        self.nave_x = 0
        self.nave_velocidad = 1.0  # Velocidad horizontal
        self.tiempo = 0  # Contador para animaciones

        # Posiciones verticales actuales y objetivo (para movimiento suave)
        self.nave_y = alto // 2
        self.nave_y_objetivo = self.nave_y
    def dibujar_nave(self):
        self.tiempo += 0.01  # Simula el paso del tiempo

        # Movimiento vertical objetivo con función seno
        amplitud = self.alto // 2
        frecuencia = 0.015
        centro_y = self.alto // 3

        self.nave_y_objetivo = centro_y + amplitud * math.sin(frecuencia * self.nave_x + self.tiempo)

        # Agrega micro-oscilación para hacerlo más natural
        self.nave_y_objetivo += 10 * math.sin(0.2 * self.tiempo)

        # Interpolación hacia el objetivo (suavizado)
        velocidad_suavizado = 0.05
        self.nave_y += (self.nave_y_objetivo - self.nave_y) * velocidad_suavizado
        # Cálculo de inclinación basado en la dirección vertical
        diferencia = self.nave_y_objetivo - self.nave_y
        angulo_inclinacion = max(min(diferencia * 0.4, 25), -25)  # Entre -20° y 20°

        # Rotar la imagen para simular inclinación
        nave_rotada = pygame.transform.rotate(self.nave_imagen, -angulo_inclinacion)

        # Ajustar la posición para que la rotación no mueva el centro visual
        rect = nave_rotada.get_rect(center=(self.nave_x + self.nave_imagen.get_width() // 2,
                                            self.nave_y + self.nave_imagen.get_height() // 2))

        # Dibujar la nave rotada
        self.pantalla.blit(nave_rotada, rect.topleft)
        # Mover la nave horizontalmente
        self.nave_x += self.nave_velocidad

        # Si sale de pantalla, reaparece por la izquierda
        if self.nave_x > self.ancho:
            self.nave_x = -self.nave_imagen.get_width()
    def dibujar_gradiente(self):
        for i in range(self.alto):
            factor = i / self.alto  # 0 arriba → 1 abajo

            # Crea un degradado vertical de negro a azul oscuro
            r = int(5 * (1 - factor))   # rojo casi siempre 0
            g = int(10 * (1 - factor))  # verde casi 0
            b = int(25 + 30 * factor)   # azul oscuro

            color = (r, g, b)

            # Dibuja una línea horizontal del degradado
            pygame.draw.line(self.pantalla, color, (0, i), (self.ancho, i))
    def dibujar(self):
        self.dibujar_gradiente()  # Degradado del cielo
        self.dibujar_nave()       # Nave animada
        for estrella in self.estrellas:
            estrella.actualizar()  # Mueve estrella
            estrella.dibujar(self.pantalla)  # La dibuja

