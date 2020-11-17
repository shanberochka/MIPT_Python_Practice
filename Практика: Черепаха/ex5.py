import turtle

turtle.shape('turtle')
k=1
turtle.pencolor("black")
while(k<=10):
    for i in range(4):
        turtle.fd(k*20)
        turtle.lt(90)
    turtle.pencolor("white")
    turtle.goto(-10*k, -10*k)
    turtle.pencolor("black")
    k+=1
    
    
    
