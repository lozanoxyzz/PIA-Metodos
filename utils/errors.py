import random
import math
import pygame

# Colores
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Posición fija del "error"
ERROR_POS = (400, 300)

####CLASE CHISPAS
class Spark:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(1, 3)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.life = random.randint(10, 30)
        self.radius = random.randint(1, 3)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.05  # gravedad ligera
        self.life -= 1
        self.radius = max(0.5, self.radius - 0.05)

    def draw(self, surface):
        if self.life > 0:
            pygame.draw.circle(surface, YELLOW, (int(self.x), int(self.y)), int(self.radius))

class EmisorChispa:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sparks = []
        self.radio_interaccion = 50
        self.interactuado = False

    def update(self):
        for _ in range(2):
            self.sparks.append(Spark(self.x, self.y))
        for spark in self.sparks[:]:
            spark.update()
            if spark.life <= 0:
                self.sparks.remove(spark)

    def draw(self, pantalla):
        for spark in self.sparks:
            spark.draw(pantalla)


    def jugador_cerca(self, jugador_rect):
        dx = jugador_rect.centerx - self.x
        dy = jugador_rect.centery - self.y
        distancia = math.hypot(dx, dy) - 10
        return distancia < self.radio_interaccion


#(UBICACION, COORDENADAS DEL ERROR)
lista_errores = [("almacenamiento", [1150,380]),
                 ("almacenamiento", [800,160]),
                 ("comunicaciones", [300, 230]),
                 ("comunicaciones", [300, 1000]),
                 ("energia", [1150, 210]),
                 ("energia", [740, 580]),
                 ("propulsion", [1150,200]),
                 ("propulsion", [950,200]),
                 ("ventilacion", [520,180]),
                 ("ventilacion", [440, 500]),
                 ("vigilancia", [270, 200]),
                 ("vigilancia", [420, 210]),]

errores_activos = []
error = random.choice(lista_errores)
errores_activos.append(error)



