import pygame 
from constantes import *
from Tela_cubo import Tela_cubo

class Jogo():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Cubo 3D")

        self.tela_atual = Tela_cubo()
        self.fonte = pygame.font.SysFont('Anton', 50)
        self.clock = pygame.time.Clock()
        self.fps = 60
    
    def atualiza(self):

        self.tela_atual = self.tela_atual.atualiza()
        self.clock.tick(self.fps)

        if self.tela_atual is None:
            return False
        
        return True
    
    def game_loop(self):
        while self.atualiza():
            self.tela_atual.desenha(self.screen)
            pygame.display.update()
    
    def finaliza(self):
        pygame.quit()


