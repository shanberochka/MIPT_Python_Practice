import graphics as gr
import math as m
SIZE_X = 800
SIZE_Y = 800
window = gr.GraphWin("Mayatnik", SIZE_X, SIZE_Y)
length = 300  # Длина рычага
G = 0.01  # Сила притяжения
mass = 10  # Масса тела
angle = 5  # Устанавливаем начальный угол
angle_velocity = 1  # Ускорение
angle_accelaration = -G * m.sin(angle)  # Начальное ускорени
center_point = gr.Point(SIZE_X / 2, SIZE_Y / 2)  # Центр холста
coords = gr.Point(center_point.x + length * m.sin(angle),
                  center_point.y + length * m.cos(angle))  # Начальные координаты шара
# Фон
rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
rectangle.setFill('white')
rectangle.draw(window)
# Рисуем центр
center = gr.Circle(center_point, 20)
center.setFill('black')
center.draw(window)
# Рисуем шар
ball = gr.Circle(gr.Point(coords.x, coords.y), mass * 5)
ball.setFill('grey')
ball.draw(window)
def update_coords(coords):
    new_point = gr.Point(center_point.x + length * m.sin(angle),
                         center_point.y + length * m.cos(angle))
    velocity = gr.Point(new_point.x - coords.x,
                        new_point.y - coords.y)
    return velocity
def get_angle(angle, angle_accelaration, angle_velocity):
    angle_accelaration = -G * m.sin(angle)
    angle += angle_velocity
    angle_velocity += angle_accelaration
    angle_velocity *= 0.99
    return angle, angle_accelaration, angle_velocity
while True:
    angle, angle_accelaration, angle_velocity = get_angle(angle, angle_accelaration, angle_velocity)
    velocity = update_coords(ball.getCenter())
    ball.move(velocity.x, velocity.y)
    line = gr.Line(center_point, ball.getCenter())
    line.draw(window)
    gr.time.sleep(0.03)
    line.undraw()

window.close()
