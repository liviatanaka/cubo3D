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
            cubo (Cubo): objeto da classe Cubo, que será renderizado na tela.
            ang (int): valor inicial é zero, utilizado para a rotação do cubo.
            ang_x (int): valor inicial é zero, utilizado para a rotação do cubo no eixo x.
            vel (int): valor inicial é um, representa a velocidade de rotação do cubo.
            d (int): valor inicial é 400, representa a distância da câmera ao cubo.
        """
        self.cubo = Cubo()
        self.angulos = {"x": 0, "y": 0, "z": 0, "todos": 0}
        self.vel = 1
        self.d = 400
        self.modo = "padrao"
        # padrão -> rotaciona normal em todos os eixos
        # controle -> rotaciona pelas teclas
    def atualiza(self):
        """
        Método que atualiza o ângulo de rotação do cubo e realiza ações do teclado e mouse.

        Returns:
            None ou Tela_cubo: Retorna None quando o evento de fechar a janela é acionado ou retorna
            a própria instância da classe Tela_cubo.

        """

        self.angulos["todos"] += self.vel

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.modo = "padrao"
                if event.key == pygame.K_c:
                    self.modo = "controle"
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # zoom in
                    self.d *= 1.1
                elif event.button == 5:  # zoom out
                    self.d /= 1.1


        if self.modo == "controle":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.angulos["x"] += self.vel
            if keys[pygame.K_s]:
                self.angulos["x"] -= self.vel
            if keys[pygame.K_d]:
                self.angulos["y"] += self.vel
            if keys[pygame.K_a]:
                self.angulos["y"] -= self.vel
            if keys[pygame.K_q]:
                self.angulos["z"] += self.vel
            if keys[pygame.K_e]:
                self.angulos["z"] -= self.vel

        return self

    def desenha(self, screen):
        """
        Método responsável por renderizar o cubo na tela.

        Args:
            screen (Surface): superfície em que o cubo será renderizado.

        """
        
        objeto_rotacionado = self.cubo.rotacao_cubo(self.angulos, self.modo)
        xp, yp = self.cubo.projecao_cubo(self.d, objeto_rotacionado)

        # desenho ##########################################################################################################
        
        screen.fill(PRETO)
        i = 0

        largura = WIDTH//2
        altura = HEIGHT//2
        while i < len(self.cubo.arestas):
            x = self.cubo.arestas[i]
            # Desenha uma linha entre os dois pontos da aresta e coloca na tela.
            pygame.draw.line(screen, AZUL, (xp[x[0]] + largura, yp[x[0]] + altura), (xp[x[1]] +largura, yp[x[1]] + altura), 5)
            i += 1

        i = 0
        while i < len(xp):
            x = xp[i]
            y = yp[i]
            # Desenha um circulo no ponto e coloca na tela.
            pygame.draw.circle(screen, VERM, (x + largura, y + altura), 5)

            i += 1
