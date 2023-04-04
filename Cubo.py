import numpy as np

class Cubo():

    def __init__(self):
        self.vertices = np.array([[-1, -1, -1, 1],
                                  [ 1, -1, -1, 1],
                                  [ 1,  1, -1, 1],
                                  [-1,  1, -1, 1],
                                  [-1, -1,  1, 1],
                                  [ 1, -1,  1, 1],
                                  [ 1,  1,  1, 1],
                                  [-1,  1,  1, 1]])
        
    def matriz_rotacao_x(self, theta):
        R_x = np.array([[1, 0, 0, 0],
                [0, np.cos(theta), -np.sin(theta), 0],
                [0, np.sin(theta), np.cos(theta), 0],
                [0, 0, 0, 1]])
        return R_x
    
    def matriz_rotacao_y(self,theta):
        R_y = np.array([[np.cos(theta), 0, np.sin(theta), 0],
                      [0, 1, 0, 0],
                      [-np.sin(theta), 0,  np.cos(theta), 0],
                      [0, 0, 0, 1]])
        return R_y
    
    def matriz_rotacao_z(self, theta):
        R_z = np.array([[np.cos(theta), -np.sin(theta), 0, 0],
                      [np.sin(theta),np.cos(theta), 0 , 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])
        return R_z
        
    def matriz_translacao(self):
        T = np.array([[1, 0, 0, 0], 
                [0, 1, 0, 0], 
                [0, 0, 1, 10],
                [0, 0, 0, 1]])
        return T

    def rotacao_cubo(self, ang):
        objeto = self.vertices.T
        theta = np.radians(ang)

        T = self.matriz_translacao()
        R_x = self.matriz_rotacao_x(theta)
        R_y = self.matriz_rotacao_y(theta)
        R_z = self.matriz_rotacao_z(theta)

        R = T @ R_x @ R_y @ R_z 
        objeto_rotacionado = R @ objeto
        return objeto_rotacionado
    
    def projecao_cubo(self, d, objeto_rotacionado):
        P = np.array([[1, 0, 0, 0], 
                      [0, 1, 0, 0], 
                      [0, 0, 0, -d], 
                      [0, 0, (-1/d), 0] ]) 
        projecao = P @ objeto_rotacionado

        xp = projecao[0,:]/ projecao[3,:]
        yp = projecao[1,:]/ projecao[3,:]
        return xp, yp
  