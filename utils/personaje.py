import pygame
import random

class Personaje:
    def __init__(self, x, y, alto_pantalla, escala=1.0):
        self.x = x
        self.y = y
        self.velocidad = int(4 * escala)
        self.escala = escala
        self.alto_pantalla = alto_pantalla

        # Cargar las imágenes
        self.imagenes = {
            "idle": pygame.image.load("assets/imagenes/personaje_idle.png").convert_alpha(),
            "caminar_izq_izq": pygame.image.load("assets/imagenes/caminar_izq_izq.png").convert_alpha(),
            "caminar_izq_der": pygame.image.load("assets/imagenes/caminar_izq_der.png").convert_alpha(),
            "caminar_der_izq": pygame.image.load("assets/imagenes/caminar_der_izq.png").convert_alpha(),
            "caminar_der_der": pygame.image.load("assets/imagenes/caminar_der_der.png").convert_alpha(),
            "caminar_frente_izq": pygame.image.load("assets/imagenes/caminar_frente_izq.png").convert_alpha(),
            "caminar_frente_der": pygame.image.load("assets/imagenes/caminar_frente_der.png").convert_alpha(),
            "caminar_espalda_izq": pygame.image.load("assets/imagenes/caminar_espalda_izq.png").convert_alpha(),
            "caminar_espalda_der": pygame.image.load("assets/imagenes/caminar_espalda_der.png").convert_alpha()
        }

        # Escalado proporcional
        self.imagenes = {
            clave: pygame.transform.scale(img, self.calcular_tamano(img))
            for clave, img in self.imagenes.items()
        }

        self.imagen_actual = self.imagenes["idle"]
        self.direccion = "idle"
        self.ultimo_cambio = pygame.time.get_ticks()
        self.frame_actual = 0

        ancho, alto = self.imagen_actual.get_size()
        self.rect = pygame.Rect(self.x, self.y, ancho, alto)

        # Sombra
        ancho, alto = self.imagen_actual.get_size()
        self.sombra = pygame.Surface((ancho * 0.6, 10), pygame.SRCALPHA)
        pygame.draw.ellipse(self.sombra, (0, 0, 0, 100), self.sombra.get_rect())

        # Partículas
        self.particulas = []

    def calcular_tamano(self, imagen):
        alto_base = 95
        alto = int((alto_base / 768) * self.alto_pantalla)
        aspect_ratio = imagen.get_width() / imagen.get_height()
        ancho = int(alto * aspect_ratio)
        return (ancho, alto)

    def manejar_input(self, teclas):
        movimiento = False
        ahora = pygame.time.get_ticks()
        direccion_horizontal = ""
        direccion_vertical = ""

        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.x -= self.velocidad
            direccion_horizontal = "izq"
            movimiento = True
        elif teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.x += self.velocidad
            direccion_horizontal = "der"
            movimiento = True

        if teclas[pygame.K_w] or teclas[pygame.K_UP]:
            self.y -= self.velocidad
            direccion_vertical = "espalda"
            movimiento = True
        elif teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            self.y += self.velocidad
            direccion_vertical = "frente"
            movimiento = True

        if movimiento:
            centro_x = self.x + self.imagen_actual.get_width() // 2
            base_y = self.y + self.imagen_actual.get_height() - 10
            self.particulas.append(Particula(centro_x, base_y, escala=self.escala))

            # Cambiar imagen cada 200 ms
            if ahora - self.ultimo_cambio > 200:
                self.ultimo_cambio = ahora
                self.frame_actual = (self.frame_actual + 1) % 2

                if direccion_horizontal:
                    clave = f"caminar_{direccion_horizontal}_{'izq' if self.frame_actual == 0 else 'der'}"
                elif direccion_vertical:
                    clave = f"caminar_{direccion_vertical}_{'izq' if self.frame_actual == 0 else 'der'}"
                else:
                    clave = "idle"

                self.imagen_actual = self.imagenes.get(clave, self.imagenes["idle"])
        else:
            self.imagen_actual = self.imagenes["idle"]
            
        self.rect.topleft = (self.x, self.y)

    def dibujar(self, pantalla):
        sombra_rect = self.sombra.get_rect(center=(self.x + self.imagen_actual.get_width() // 2, self.y + self.imagen_actual.get_height()))
        pantalla.blit(self.sombra, sombra_rect)
        pantalla.blit(self.imagen_actual, (self.x, self.y))

        for particula in self.particulas[:]:
            particula.actualizar()
            particula.dibujar(pantalla)
            if particula.vida <= 0:
                self.particulas.remove(particula)

class Particula:
    def __init__(self, x, y, escala=1.0):
        self.x = x + random.uniform(-5, 5) * escala
        self.y = y + random.uniform(-3, 3) * escala
        self.radio = random.randint(3, 6) * escala
        self.color = (200, 150, 100)
        self.velocidad_y = random.uniform(-0.4, -1.2) * escala
        self.velocidad_x = random.uniform(-0.6, 0.6) * escala
        self.vida = 18
        self.alpha = 200

    def actualizar(self):
        self.x += self.velocidad_x
        self.y += self.velocidad_y
        self.vida -= 1
        self.alpha = max(0, self.alpha - 8)
        self.radio = max(0.5, self.radio - 0.1)

    def dibujar(self, pantalla):
        if self.vida > 0:
            superficie = pygame.Surface((12, 12), pygame.SRCALPHA)
            pygame.draw.circle(superficie, (*self.color, self.alpha), (6, 6), int(self.radio))
            pantalla.blit(superficie, (self.x, self.y))
