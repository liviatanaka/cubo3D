import pygame
from constantes import *
import numpy as np
from Cubo import Cubo

class Tela_cubo():
    """
    Classe responsável pela renderização do cubo em uma tela.
    """
        
    def __init__(self):
        """
        Construtor da classe Tela_cubo.

        Atributos:
            pa (int): valor inicial é zero.
            cubo (Cubo): objeto da classe Cubo, que será renderizado na tela.
            ang (int): valor inicial é zero, utilizado para a rotação do cubo.
            ang_x (int): valor inicial é zero, utilizado para a rotação do cubo no eixo x.
            vel (int): valor inicial é um, representa a velocidade de rotação do cubo.
            d (int): valor inicial é 400, representa a distância da câmera ao cubo.
        """
        self.pa = 0
        self.cubo = Cubo()
        self.ang = 0
        self.ang_x = 0
        self.vel = 1
        self.d = 400

    def atualiza(self):
        """
        Método que atualiza o ângulo de rotação do cubo e realiza ações do teclado e mouse.

        Returns:
            None ou Tela_cubo: Retorna None quando o evento de fechar a janela é acionado ou retorna
            a própria instância da classe Tela_cubo.

        """

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
        """
        Método responsável por renderizar o cubo na tela.

        Args:
            screen (Surface): superfície em que o cubo será renderizado.

        """
        
        objeto_rotacionado = self.cubo.rotacao_cubo(self.ang)
        xp, yp = self.cubo.projecao_cubo(self.d, objeto_rotacionado)

        # desenho ##########################################################################################################
        
        screen.fill(PRETO)
        aresta = np.array([[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4], [0, 4], [1, 5], [2, 6], [3, 7]])
        i = 0
        while i < len(aresta):
            x = aresta[i]
            # Desenha uma linha entre os dois pontos da aresta e coloca na tela.
            pygame.draw.line(screen, AZUL, (xp[x[0]] + WIDTH//2, yp[x[0]] + HEIGHT//2), (xp[x[1]] + WIDTH//2, yp[x[1]] + HEIGHT//2), 5)
            i += 1

        i = 0
        while i < len(xp):
            x = xp[i]
            y = yp[i]
            # Desenha um circulo no ponto e coloca na tela.
            pygame.draw.circle(screen, VERM, (x +WIDTH//2, y + HEIGHT//2), 5)

            i += 1
