import pygame
import sys
# Importamos nuestras propias piezas del puzzle
from src.constantes import *
from src.objetos import Serpiente, Comida
from src.motor import obtener_record, guardar_record

class Game:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Snake Pro Modular")
        self.reloj = pygame.time.Clock()
        self.fuente = pygame.font.SysFont("Arial", 20)
        self.reset()

    def reset(self):
        self.serpiente = Serpiente()
        self.comida = Comida()
        self.puntos = 0
        self.record_actual = obtener_record()

    def mostrar_hud(self):
        texto = f"SCORE: {self.puntos}   MAX: {self.record_actual}"
        img = self.fuente.render(texto, True, BLANCO)
        self.pantalla.blit(img, (10, 10))

    def ejecutar(self):
        while True:
            # 1. Eventos
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP and self.serpiente.dir_y == 0:
                        self.serpiente.dir_y = -TAM_CUADRO; self.serpiente.dir_x = 0
                    elif evento.key == pygame.K_DOWN and self.serpiente.dir_y == 0:
                        self.serpiente.dir_y = TAM_CUADRO; self.serpiente.dir_x = 0
                    elif evento.key == pygame.K_LEFT and self.serpiente.dir_x == 0:
                        self.serpiente.dir_x = -TAM_CUADRO; self.serpiente.dir_y = 0
                    elif evento.key == pygame.K_RIGHT and self.serpiente.dir_x == 0:
                        self.serpiente.dir_x = TAM_CUADRO; self.serpiente.dir_y = 0

            # 2. Lógica de movimiento
            self.serpiente.mover()
            cabeza = self.serpiente.cuerpo[-1]

            # 3. Colisiones (Paredes o Cuerpo)
            if (cabeza[0] < 0 or cabeza[0] >= ANCHO or 
                cabeza[1] < 0 or cabeza[1] >= ALTO or 
                cabeza in self.serpiente.cuerpo[:-1]):
                guardar_record(self.puntos)
                self.reset()

            # 4. Comer
            if cabeza == self.comida.pos:
                self.puntos += 10
                self.serpiente.largo += 1
                self.comida.pos = self.comida.generar_posicion()

            # 5. Dibujar
            self.pantalla.fill(NEGRO)
            # Dibujar comida
            pygame.draw.rect(self.pantalla, ROJO, (self.comida.pos[0], self.comida.pos[1], TAM_CUADRO, TAM_CUADRO))
            # Dibujar serpiente
            for seg in self.serpiente.cuerpo:
                pygame.draw.rect(self.pantalla, VERDE, (seg[0], seg[1], TAM_CUADRO, TAM_CUADRO))
            
            self.mostrar_hud()
            pygame.display.flip()
            self.reloj.tick(VELOCIDAD)

if __name__ == "__main__":
    juego = Game()
    juego.ejecutar()