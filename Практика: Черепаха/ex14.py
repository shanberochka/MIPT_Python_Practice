import turtle
turtle.shape("turtle")

n = int(turtle.textinput(u'Введите количество вершин', 'Введите количество вершин: '))
def star(n):
    for i in range(n):
        turtle.lt(180 - (180/n))
        turtle.fd(100)
star(n)
turtle.exitonclick()
