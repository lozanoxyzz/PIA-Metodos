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
## UBICACION DE IMAGEN, RESULTADO, METODO
problemas_comunicaciones_interpolacion = [("Assets/imagenes_problemas/imagen_prueba.jpeg",100,"Interpolacion Lineal"),  # Interpolacion Lineal
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg",100,"Interpolacion Lineal"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg",100,"Interpolacion Lineal"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100,"Interpolacion Lineal"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100,"Interpolacion Lineal"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100,"Interpolacion Lineal"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Adelante"),  # Newton Hacia Adelante
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Adelante"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Adelante"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Adelante"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Adelante"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Adelante"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Atras"),  # Newton Hacia Atras
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Atras"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Atras"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Atras"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Atras"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Atras"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton con Diferencias Divididas"),  #Newton con Diferencias Divididas
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton con Diferencias Divididas"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton con Diferencias Divididas"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton con Diferencias Divididas"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton con Diferencias Divididas"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton con Diferencias Divididas"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Lagrange"),  #Lagrange
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Lagrange"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Lagrange"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Lagrange"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Lagrange"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Lagrange")]

problemas_ventilacion_nolineales = [("Assets/imagenes_problemas/imagen_prueba.jpeg",100,"Grafico"),  # Grafico
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg",100,"Grafico"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg",100,"Grafico"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100,"Grafico"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100,"Grafico"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100,"Grafico"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100,"Bisectriz"),  # Bisectriz
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100,"Bisectriz"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100,"Bisectriz"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100,"Bisectriz"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100,"Bisectriz"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100,"Bisectriz"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Punto Fijo"),  # Punto Fijo
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Punto Fijo"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Punto Fijo"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Punto Fijo"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Punto Fijo"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Punto Fijo"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton - Raphson"),  #Newton - Raphson
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton - Raphson"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton - Raphson"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton - Raphson"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton - Raphson"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton - Raphson"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Falsa Posicion"),  #Falsa Posicion
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Falsa Posicion"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Falsa Posicion"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Falsa Posicion"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Falsa Posicion"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Falsa Posicion"),
                                           ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Secante"), #Secante
                                           ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Secante"),
                                           ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Secante"),
                                           ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Secante"),
                                           ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Secante"),
                                           ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Secante"),]

problemas_vigilancia_lineales =  [("Assets/imagenes_problemas/imagen_prueba.jpeg",100, "Montante"),  # Montante
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg",100, "Montante"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg",100, "Montante"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Montante"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Montante"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Montante"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Gauss Jordan"),  # Gauss-Jordan
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Gauss Jordan"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Gauss Jordan"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Gauss Jordan"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Gauss Jordan"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Gauss Jordan"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Eliminacion Gaussiana"),  # Eliminacion Gaussiana
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Eliminacion Gaussiana"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Eliminacion Gaussiana"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Eliminacion Gaussiana"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Eliminacion Gaussiana"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Eliminacion Gaussiana"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Gauss - Seidel"),  #Gauss - Seidel
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Gauss - Seidel"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Gauss - Seidel"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Gauss - Seidel"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Gauss - Seidel"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Gauss - Seidel"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Jacobi"),  #Jacobi
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Jacobi"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Jacobi"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Jacobi"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Jacobi"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Jacobi")]

problemas_propulsion_minimos = [("Assets/imagenes_problemas/imagen_prueba.jpeg",100,"Interpolacion Lineal", "Linea Recta"),  # Linea Recta
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg",100, "Linea Recta"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg",100, "Linea Recta"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Linea Recta"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Linea Recta"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Linea Recta"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Cuadratica"),  # Cuadratica
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Cuadratica"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Cuadratica"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Cuadratica"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Cuadratica"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Cuadratica"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Cubica"),  # Cubica
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Cubica"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Cubica"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Cubica"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Cubica"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Cubica"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Lineal con Funcion"),  #Lineal con Funcion
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Lineal con Funcion"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Lineal con Funcion"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Lineal con Funcion"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Lineal con Funcion"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Lineal con Funcion"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Cuadratica con Funcion"),  #Cuadratica con Funcion
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Cuadratica con Funcion"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Cuadratica con Funcion"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Cuadratica con Funcion"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Cuadratica con Funcion"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Cuadratica con Funcion")]

problemas_energia_integracion = [("Assets/imagenes_problemas/imagen_prueba.jpeg",100,"Regla Trapezoidal"),  # Regla Trapezoidal
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg",100,"Regla Trapezoidal"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg",100,"Regla Trapezoidal"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100,"Regla Trapezoidal"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100,"Regla Trapezoidal"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100,"Regla Trapezoidal"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Regla 1/3 Simpson"),  # Regla 1/3 Simpson
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Regla 1/3 Simpson"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Regla 1/3 Simpson"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Regla 1/3 Simpson"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Regla 1/3 Simpson"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Regla 1/3 Simpson"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Regla 3/8 Simpson"),  # Regla 3/8 Simpson
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Regla 3/8 Simpson"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Regla 3/8 Simpson"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Regla 3/8 Simpson"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Regla 3/8 Simpson"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Regla 3/8 Simpson"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton - Cotes Cerradas"),  #Newton - Cotes Cerradas
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton - Cotes Cerradas"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton - Cotes Cerradas"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton - Cotes Cerradas"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton - Cotes Cerradas"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton - Cotes Cerradas"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton - Cotes Abiertas"),  #Newton - Cotes Abiertas
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton - Cotes Abiertas"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton - Cotes Abiertas"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton - Cotes Abiertas"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton - Cotes Abiertas"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton - Cotes Abiertas")]

problemas_almacenamiento_edo = [("Assets/imagenes_problemas/imagen_prueba.jpeg",100,"Interpolacion Lineal"),  # Interpolacion Lineal
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg",100,"Interpolacion Lineal"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg",100,"Interpolacion Lineal"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100,"Interpolacion Lineal"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100,"Interpolacion Lineal"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100,"Interpolacion Lineal"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Adelante"),  # Newton Hacia Adelante
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Adelante"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Adelante"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Adelante"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Adelante"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Adelante"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Atras"),  # Newton Hacia Atras
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Atras"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Atras"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Atras"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Atras"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton Hacia Atras"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton con Diferencias Divididas"),  #Newton con Diferencias Divididas
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton con Diferencias Divididas"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton con Diferencias Divididas"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton con Diferencias Divididas"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton con Diferencias Divididas"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Newton con Diferencias Divididas"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Lagrange"),  #Lagrange
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Lagrange"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Lagrange"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Lagrange"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Lagrange"),
                                          ("Assets/imagenes_problemas/imagen_prueba.jpeg", 100, "Lagrange")]



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
error =   ("almacenamiento", [1150,380])

if error[0] == "vigilancia":
    problema = random.choice(problemas_vigilancia_lineales)
elif error[0] == "comunicaciones":
    problema = random.choice(problemas_comunicaciones_interpolacion)
elif error[0] == "ventilacion":
    problema = random.choice(problemas_ventilacion_nolineales)
elif error[0] == "energia":
    problema = random.choice(problemas_energia_integracion)
elif error[0] == "propulsion":
    problema = random.choice(problemas_propulsion_minimos)
elif error[0] == "almacenamiento":
    problema = random.choice(problemas_almacenamiento_edo)



# error = random.choice(lista_errores)
errores_activos.append(error)



