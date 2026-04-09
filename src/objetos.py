import random
from .constantes import ANCHO, ALTO, TAM_CUADRO

class Comida:
    def __init__(self):
        self.pos = self.generar_posicion()

    def generar_posicion(self):
        # Genera una posicion alineada a la cuadricula
        x = round(random.randrange(0, ANCHO - TAM_CUADRO) / float(TAM_CUADRO)) * TAM_CUADRO
        y = round(random.randrange(0, ALTO - TAM_CUADRO) / float(TAM_CUADRO)) * TAM_CUADRO
        return [x, y]

class Serpiente:
    def __init__(self):
        self.cuerpo = [[ANCHO // 2, ALTO // 2]] # Posicion inicial de la serpiente
        self.dir_x = 0
        self.dir_y = 0
        self.largo = 1

    def mover(self):
        # Calculamos la nueva posicion de la cabeza
        nueva_cabeza = [self.cuerpo[-1][0] + self.dir_x, self.cuerpo[-1][1] + self.dir_y]
        self.cuerpo.append(nueva_cabeza)

        # Si no ha crecido, eliminamos el ultimo segmento para simular movimiento
        if len(self.cuerpo) > self.largo:
            del self.cuerpo[0]