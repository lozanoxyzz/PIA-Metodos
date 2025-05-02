import random
#(UBICACION, COORDENADAS DEL ERROR)

errores_activos = []

lista_errores = [("almacenamiento", []),
                 ("almacenamiento", []),
                 ("comunicaciones", []),
                 ("comunicaciones", []),
                 ("energia", []),
                 ("energia", []),
                 ("propulsion", []),
                 ("propulsion", []),
                 ("ventilacion", []),
                 ("ventilacion", []),
                 ("vigilancia", []),
                 ("vigilancia", []),]


error = random.choice(lista_errores)
errores_activos.append(error)


