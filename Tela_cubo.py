import pygame
from constantes import *
import numpy as np
from Cubo import Cubo

class Tela_cubo():
    
    def __init__(self):
        self.pa = 0
        self.cubo = Cubo()
        self.ang = 0
        self.ang_x = 0
        self.vel = 1
        self.d = 400

    def atualiza(self):

        self.ang += self.vel

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_i:
                    pass
                if event.key == pygame.K_RIGHT:
                    self.ang_x += self.vel
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # zoom in
                    self.d *= 1.1
                elif event.button == 5:  # zoom out
                    self.d /= 1.1
        
        return self

    def desenha(self, screen):
        
        objeto_rotacionado = self.cubo.rotacao_cubo(self.ang)
        xp, yp = self.cubo.projecao_cubo(self.d, objeto_rotacionado)

        # desenho ##########################################################################################################
        
        screen.fill(PRETO)
        aresta = np.array([[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4], [0, 4], [1, 5], [2, 6], [3, 7]])
        i = 0
        while i < len(aresta):
            x = aresta[i]
            pygame.draw.line(screen, AZUL, (xp[x[0]] + WIDTH//2, yp[x[0]] + HEIGHT//2), (xp[x[1]] + WIDTH//2, yp[x[1]] + HEIGHT//2), 5)
            i += 1

        i = 0
        while i < len(xp):
            x = xp[i]
            y = yp[i]
            pygame.draw.circle(screen, VERM, (x +WIDTH//2, y + HEIGHT//2), 5)

            i += 1
