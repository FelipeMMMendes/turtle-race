#importando as bibliotecas
from turtle import Turtle, Screen, color

#instancia objetos das classes Screen e Turtle
tela = Screen()

#faz com que a tela tenha dimensões personalizadas
tela.setup(width=500, height=400)

#faz com que apareca um prompt para que o usuario entre com a tartaruga que ele vai apostar
userChoice = tela.textinput("Escolha de tartaruga: ","Cor: ")
#armazena o valor na variavel escolhaUsuario

#variavel flag para manter a corrida acontecendo
corridaAtiva = False

#lista contendo todas as cores, para ser acessadas e usadas no 
# momento de instanciação das tartarugas
colors = ["red","orange","yellow","green","blue","purple"]

#lista contendo os nomes das tartarugas
turtleNames = ["felipe","jonas","lucas","pedrox","pingu","4K"]

#lista para armazenar as tartarugas instanciadas
turtles = []

#variaveis flag para colocar as tartarugas em suas devidas posicoes
x=-230
y=-100

#variavel flag para controlar a posicao da cor
colorId = 0

#variavel flag para guardar as informacoes da tartaruga vencedora
turtleWinner = Turtle()
turtleWinner.hideturtle()

for name in turtleNames:
    name = Turtle(shape="turtle")
    name.color(colors[colorId])
    name.penup()
    
    y += 25
    colorId += 1

    name.goto(x=x,y=y)
    turtles.append(name)


#importando a funcao para escolher numeros aleatorios
from random import randrange

#ativando a corrida
corridaAtiva=True

#laco que vai manter as tartarugas correndo
while corridaAtiva:
    for turtle in turtles:

        #condicao para checar se a tartaruga ja chegou ao destino ou nao
        if turtle.xcor() > 125:
            corridaAtiva = False
            turtleWinner = turtle
            print(f"The winner was {turtleWinner.color()[0]}")


        #laco que fica percorrendo todas as tartarugas e faz todas andarem um pouco
        turtle.forward(randrange(0, 11))



if corridaAtiva == False:
    if turtleWinner.color()[0] == userChoice:
        print("You win!")
    else:
        print("You lose!")    

tela.exitonclick()