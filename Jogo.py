import pygame 
from constantes import *
from Tela_cubo import Tela_cubo

class Jogo():
    """Representa um jogo com uma tela em 3D de um cubo utilizando a biblioteca Pygame.

    Atributos:
        screen (pygame.Surface): superfície da janela do jogo.
        tela_atual (Tela_cubo): instância da classe Tela_cubo responsável pelo desenho da tela atual.
        fonte (pygame.font.Font): objeto que representa uma fonte de texto utilizada no jogo.
        clock (pygame.time.Clock): objeto que controla o número de frames por segundo.
        fps (int): número de frames por segundo desejado.

    Métodos:
        __init__: inicializa a classe e cria a janela do jogo.
        atualiza: atualiza a tela atual e limita o número de frames por segundo com o uso do objeto Clock.
        game_loop: roda o loop principal do jogo, desenhando a tela atual e atualizando a janela.
        finaliza: encerra a biblioteca Pygame.
    """
    def __init__(self):
        """Inicializa a classe e cria a janela do jogo."""
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Cubo 3D")

        self.tela_atual = Tela_cubo()
        self.fonte = pygame.font.SysFont('Anton', 50)
        self.clock = pygame.time.Clock()
        self.fps = 60
    
    def atualiza(self):
        """Atualiza a tela atual e limita o número de frames por segundo com o uso do objeto Clock.

        Retorna:
            bool: True se o jogo deve continuar rodando, False se a tela atual é None e o jogo deve ser finalizado.
        """
        self.tela_atual = self.tela_atual.atualiza()
        self.clock.tick(self.fps)

        if self.tela_atual is None:
            return False
        
        return True
    
    def game_loop(self):
        """Roda o loop principal do jogo, desenhando a tela atual e atualizando a janela."""
        while self.atualiza():
            self.tela_atual.desenha(self.screen)
            pygame.display.update()
    
    def finaliza(self):
        """Encerra a biblioteca Pygame."""
        pygame.quit()


