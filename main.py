r"""
#Importando biblioteca para extrair as cores
import colorgram

#colocando o caminho do arquivo para uma variavel
font = r'C:\Users\felipe.mendes\Desktop\Programação\python\Curso100Days\exercicios\HistPainting\colorFont.jpg'

#usando a funcao do colorgram para extrair as cores da imagem
colors = colorgram.extract(font,15)

#instanciando uma lista para ser preenchida com os valores RGB de cada cor coletada
listColors = []

#laco para percorrer as cores achadas e listar todos os valores RGB de cada uma numa Tuple
for item in range(len(colors)):
    color = colors[item]
    colorTuple = (
        color.rgb[0],
        color.rgb[1],
        color.rgb[2]
        )
    listColors.append(colorTuple)    

#Imprime a lista para termos noção de quais cores realmente são cores
print(listColors)

"""

#variavel flag para armazenar os valores RGB das cores (que nao sejam brancas)
colorsList = [(198, 12, 32),(250, 237, 17),(39, 76, 189),(38, 217, 68), (238, 227, 5), 
(229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165)]

#importando a biblioteca turtle
from turtle import Turtle,Screen

#Importando o choice da biblioteca random
from random import choice

from traitlets import default


#instancia um objeto do tipo screen
screen = Screen()
#seta o colormode da tela para que ela suporte mais cores
screen.colormode(255)
#seta o tamanho da tela
screen.screensize(2000,2000)

print(screen.window_height())

#instancia um objeto do tipo turtle
turtle = Turtle()
#levanta a caneta para nao desenhar
turtle.penup()
#seta a velocidade da tartaruga para a mais rapida
turtle.speed("fastest")
#move a tartaruga para o canto esquerdo da tela
turtle.setposition(-300,-250)

screen.setup(width=1000, height=500, startx=None, starty=None)

#variavel flag para contar quantos movimentos a tartaruga fez 
i = 0

#importando a funcao de turn
from extraFunctions import turn

for number in range(100):
    i+=1
    #desenha um ponto
    turtle.dot(20,choice(colorsList))
    #move a tartaruga
    turtle.forward(50)
    if i%10 == 0:
        turn(turtle)


#faz com que a tela só feche quando clicarmos
screen.exitonclick()
