def turn(turtle):
    if turtle.heading() == 0:
        #caso a tartaruga esteja virada para a direita
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
    else:
        #caso a tartaruga esteja virada para a esquerda
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)    