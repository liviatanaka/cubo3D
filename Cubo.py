import numpy as np

class Cubo():
    """
    Classe que representa um cubo em um espaço tridimensional e fornece métodos para realizar rotação e projeção.
    """

    def __init__(self):
        '''
        Inicializa a classe Cubo com os vértices de um cubo unitário centrado na origem.
        '''
        self.vertices = np.array([[-1, -1, -1, 1],
                                  [ 1, -1, -1, 1],
                                  [ 1,  1, -1, 1],
                                  [-1,  1, -1, 1],
                                  [-1, -1,  1, 1],
                                  [ 1, -1,  1, 1],
                                  [ 1,  1,  1, 1],
                                  [-1,  1,  1, 1]])
        
    def matriz_rotacao_x(self, theta):
        '''
        Retorna uma matriz de rotação em torno do eixo x.

        Args:
            theta (float): ângulo de rotação em graus.

        Returns:
            R_x (numpy array): matriz de rotação em torno do eixo x.

        '''
        R_x = np.array([[1, 0, 0, 0],
                [0, np.cos(theta), -np.sin(theta), 0],
                [0, np.sin(theta), np.cos(theta), 0],
                [0, 0, 0, 1]])
        return R_x
    
    def matriz_rotacao_y(self,theta):
        '''
        Retorna uma matriz de rotação em torno do eixo y.

        Args:
            theta (float): ângulo de rotação em graus.

        Returns:
            R_y (numpy array): matriz de rotação em torno do eixo y.

        '''        
        R_y = np.array([[np.cos(theta), 0, np.sin(theta), 0],
                      [0, 1, 0, 0],
                      [-np.sin(theta), 0,  np.cos(theta), 0],
                      [0, 0, 0, 1]])
        return R_y
    
    def matriz_rotacao_z(self, theta):
        '''
        Retorna uma matriz de rotação em torno do eixo z.

        Args:
            theta (float): ângulo de rotação em graus.

        Returns:
            R_z (numpy array): matriz de rotação em torno do eixo z.

        '''
        R_z = np.array([[np.cos(theta), -np.sin(theta), 0, 0],
                      [np.sin(theta),np.cos(theta), 0 , 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])
        return R_z
        
    def matriz_translacao(self):
        '''
        Retorna uma matriz de translação.

        Returns:
            T (numpy array): matriz de translação.

        '''
        T = np.array([[1, 0, 0, 0], 
                [0, 1, 0, 0], 
                [0, 0, 1, 10],
                [0, 0, 0, 1]])
        return T

    def rotacao_cubo(self, ang):
        '''
        Aplica rotação sobre o cubo.

        Args:
            ang (float): ângulo de rotação em graus.

        Returns:
            objeto_rotacionado (numpy array): objeto rotacionado.

        '''
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
        ''' 
        Aplica projeção perspectiva sobre o cubo.

        Args:
            d (float): distância focal.
            objeto_rotacionado (numpy array): objeto rotacionado.

        Returns:
            xp (numpy array): coordenada x do ponto projetado.
            yp (numpy array): coordenada y do ponto projetado.

        '''
        P = np.array([[1, 0, 0, 0], 
                      [0, 1, 0, 0], 
                      [0, 0, 0, -d], 
                      [0, 0, (-1/d), 0] ]) 
        projecao = P @ objeto_rotacionado

        xp = projecao[0,:]/ projecao[3,:]
        yp = projecao[1,:]/ projecao[3,:]
        return xp, yp
  