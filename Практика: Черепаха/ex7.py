import turtle
import math

turtle.shape("turtle")
a = 3
b = 2
fi = 0
for i in range(1000):
    x = (a + b*fi)*math.cos(fi)
    y = (a + b*fi)*math.sin(fi)
    turtle.goto(x,y)
    fi+=0.1
