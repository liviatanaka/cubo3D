# cubo3D

APS 4 - Álgebra Linear e Teoria da Informação - 2021.1

O "Cubo 3D" é um programa desenvolvido para a disciplina de Álgebra Linear e Teoria da Informação, ministrada pelo professor Tiago Fernandes Tavares. O modelo implementado é um modelo gráfico que consiste em um cubo no espaço tridimensional que pode ser rotacionado e projetado em uma cena bidimensional através de uma projeção perspectiva. O modelo foi implementado em Python utilizando a biblioteca Pygame para a renderização gráfica.

## Introdução

# Gif do jogo
![Cubo 3D | Gif demonstrativo]()
* **Descrição:** Gif demonstrativo do Cubo 3D
* **Link:** 

## Integrantes do grupo
* [Isabelle da Silva Santos](https://github.com/isabelleatt)
* [Livia Tanaka](https://github.com/liviatanaka)

## Descrição do projeto

# Instruções de Dowload
## Clonando um Repositório
Primeiramente, navegue para o diretório aonde você gostaria de clonar o repositório usando comandos como:
*  cd: para mudar de diretório 
* cd ../ para voltar um nível do diretório <br>

Para clonar um repositório, siga as instruções em: <br>
"https://docs.github.com/pt/repositories/creating-and-managing-repositories/cloning-a-repository"


Para clonar o repositório pelo terminal, você pode usar o seguinte comando: <br>
```
git clone https://github.com/liviatanaka/cubo3D.git
```

Agora, você poderá acessar os arquivos recém baixados com os comandos *cd* e *ls*

## Instalando o necessário
É necessário realizar algumas breves instalações para utilizar o código, isso pode ser realizada de forma simples usando o comando: <br>
**pip install pygame**

## Rodando o programa
Para rodar o programa é necessário executar o arquivo main.py, podendo o mesmo ser realizado pela ferramente no topo superior direito do Visual Studio code ou usando o seguinte comando: <br>
**python main.py**


## Descrição Matemática

O cubo é representado por uma matriz com os vértices do cubo unitário centrado na origem. As transformações que podem ser aplicadas no cubo são as rotações em torno dos eixos x, y e z e a translação no eixo z.  A projeção perspectiva é realizada através de uma matriz de projeção que transforma as coordenadas do objeto em coordenadas de tela. Essa matriz de projeção é definida no método `projecao_cubo` e é aplicada ao objeto rotacionado para obter as coordenadas de tela do objeto. A distância focal é definida pelo usuário e é usada para calcular a matriz de projeção.

As matrizes de transformação para a rotação em torno dos eixos x, y e z são construídas a partir do ângulo de rotação fornecido pelo usuário. Cada matriz de rotação é uma matriz 4x4 que é aplicada ao vetor de coordenadas do objeto por meio do produto de matrizes. A matriz de rotação é aplicada ao cubo unitário centrado na origem para obter as coordenadas do objeto rotacionado.

A matriz de translação é uma matriz 4x4 que realiza a translação do objeto em relação ao eixo z. Ela é fixa e é sempre aplicada em conjunto com as matrizes de rotação. A matriz de translação é aplicada ao cubo rotacionado para obter as coordenadas do objeto rotacionado e transladado.

A projeção perspectiva é realizada através de uma matriz de projeção que transforma as coordenadas do objeto em coordenadas de tela. Essa matriz de projeção é definida no método projecao_cubo e é aplicada ao objeto rotacionado para obter as coordenadas de tela do objeto. A distância focal é definida pelo usuário e é usada para calcular a matriz de projeção. A matriz de projeção é aplicada ao cubo rotacionado e transladado para obter as coordenadas de tela do objeto.

O modelo permite a rotação e a projeção do cubo em tempo real por meio de interações do usuário com o teclado e a tela. As interações do usuário são implementadas em um loop principal que chama o método de rotação e o método de projeção repetidamente, produzindo a ilusão de movimento do cubo em tempo real. O usuário pode interagir com o programa por meio das seguintes teclas:  <br>

| Tecla | Comando |
| --- | --- | 
| w | Rotação em torno do eixo x positivo |
| s | Rotação em torno do eixo x negativo |
| a | Rotação em torno do eixo y positivo |
| d | Rotação em torno do eixo y negativo |
| q | Rotação em torno do eixo z positivo |
| e | Rotação em torno do eixo z negativo |
| 1 | Modo que possibilita a rotação automática do cubo |
| 2 | Modo que possibilita a rotação controlada do cubo |
| Scroll para cima | Aumenta a distância focal |
| Scroll para baixo | Diminui a distância focal |




