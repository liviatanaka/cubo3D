import pygame
from constantes import *
import numpy as np

class Tela_cubo():
    
    def __init__(self):
        self.pa = 0

    def atualiza(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
        
        return self

    def desenha(self, screen, pin):
        # objeto = np.array([-1, -1, -1, 1])
        # for x in (-1, 1):
        #     for y in (-1, 1):
        #         for z in (-1, 1):
        #             if x == -1 and y == -1 and z == -1:
        #                 continue
        #             objeto = np.vstack((objeto, np.array([x, y, z, 1])))
        objeto = np.array([[-1, -1, -1, 1],
                           [ 1, -1, -1, 1],
                           [ 1,  1, -1, 1],
                           [-1,  1, -1, 1],
                           [-1, -1,  1, 1],
                           [ 1, -1,  1, 1],
                           [ 1,  1,  1, 1],
                           [-1,  1,  1, 1]])

        # objeto = np.array([[-1, -1, 2, 1],
        #             [ 1, -1, 2, 1],
        #             [ 1,  1, 2, 1],
        #             [-1,  1, 2, 1],
        #             [-1, -1,  4, 1],
        #             [ 1, -1,  4, 1],
        #             [ 1,  1,  4, 1],
        #             [-1,  1,  4, 1]])
        

        theta = np.radians(pin)
        R_x = np.array([[1, 0, 0, 0],
                      [0, np.cos(theta), -np.sin(theta), 0],
                      [0, np.sin(theta), np.cos(theta), 0],
                      [0, 0, 0, 1]])
        R_y = np.array([[np.cos(theta), 0, np.sin(theta), 0],
                      [0, 1, 0, 0],
                      [-np.sin(theta), 0,  np.cos(theta), 0],
                      [0, 0, 0, 1]])
        R_z = np.array([[np.cos(theta), -np.sin(theta), 0, 0],
                      [np.sin(theta),np.cos(theta), 0 , 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])
        T = np.array([[1, 0, 0, 0], 
                      [0, 1, 0, 0], 
                      [0, 0, 1, 4],
                      [0, 0, 0, 1]]) 
        # T_ = np.array([[1, 0, 0, 0], 
        #             [0, 1, 0, 0], 
        #             [0, 0, 1, -4],
        #             [0, 0, 0, 1]]) 
        objeto = objeto.T
        R = T @ R_x @ R_y @ R_z 
        objeto = R @ objeto

        d= 200
        P = np.array([[1, 0, 0, 0], 
                      [0, 1, 0, 0], 
                      [0, 0, 0, -d], 
                      [0, 0, (-1/d), 0] ]) 
        projecao = P @ objeto 

        xp = projecao[0,:]/ projecao[3,:]
        yp = projecao[1,:]/ projecao[3,:]



        # desenho ##########################################################################################################
        
        screen.fill(PRETO)
        aresta = np.array([[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4], [0, 4], [1, 5], [2, 6], [3, 7]])
        i = 0
        while i < len(aresta):
            x = aresta[i]
            # print((xp[x[0]] + WIDTH//2, yp[x[0]] + HEIGHT//2))
            pygame.draw.line(screen, AZUL, (xp[x[0]] + WIDTH//2, yp[x[0]] + HEIGHT//2), (xp[x[1]] + WIDTH//2, yp[x[1]] + HEIGHT//2), 5)
            i += 1

        i = 0
        while i < len(xp):
            x = xp[i]
            y = yp[i]
            pygame.draw.circle(screen, VERM, (x +WIDTH//2, y + HEIGHT//2), 5)
            # print((x +WIDTH//2, y + HEIGHT//2))
            i += 1
