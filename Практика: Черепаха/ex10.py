import turtle

turtle.shape('turtle')
petals = int(turtle.textinput(u"Введите количество лепестков.", "Введите количество окружностей: "))
def flower(petals):
    for i in range(1, petals+1):
        turtle.circle(50)
        turtle.setheading(0)
        turtle.left(360/petals*(i))
flower(petals)
turtle.exitonclick()
