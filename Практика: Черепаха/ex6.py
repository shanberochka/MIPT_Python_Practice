import turtle

turtle.shape("turtle")
turtle.speed("slowest")
n=12
for i in range(n):
    turtle.setheading((360/n)*(i+1))
    turtle.fd(60)
    turtle.stamp()
    turtle.home()

