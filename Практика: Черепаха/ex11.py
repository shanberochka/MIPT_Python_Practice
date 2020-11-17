import turtle

turtle.shape('turtle')
def butterfly():
    for i in range(1, 11):
        turtle.setheading(90)
        turtle.circle(20+5*i)
        #turtle.lt(0)
        turtle.circle(-20-5*i)
butterfly()
turtle.exitonclick()
        
