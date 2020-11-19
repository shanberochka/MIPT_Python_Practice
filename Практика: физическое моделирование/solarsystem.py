import graphics as gr

SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

coords_earth = gr.Point(400, 600)
coords_moon = gr.Point(370, 600)
coords_mercury = gr.Point(400, 500)

velocity_mercury = gr.Point(2.5, 0)
acceleration_mercury = gr.Point(0, 0)

velocity_earth = gr.Point(2, 0)
acceleration_earth = gr.Point(0, 0)

velocity_moon = gr.Point(1, 0)
acceleration_moon = gr.Point(0, 0)

def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

    return new_point


def sub (point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)

    return new_point


def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('black')
    rectangle.draw(window)

    sun = gr.Circle(gr.Point(400, 400), 50)
    sun.setFill('yellow')
    sun.draw(window)


def draw_ball(coords, radius, color):
    circle = gr.Circle(coords, radius)
    circle.setFill(color)
    circle.draw(window)
    return circle


def check_coords(coords, velocity):
    if coords.x < 0 or coords.x > SIZE_X:
        velocity.x = -velocity.x

    if coords.y < 0 or coords.y > SIZE_Y:
        velocity.y = -velocity.y


def update_coords(coords, velocity):
    return add(coords, velocity)


def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


def update_acceleration(ball_coords, center_coords, G):
    diff = sub(ball_coords, center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3/2)


    return gr.Point(-diff.x*G/distance_2, -diff.y*G/distance_2)
# выносим из цикла отрисовку объектов
clear_window()

earth = draw_ball(coords_earth, 10, 'green')
moon = draw_ball(coords_moon, 2, 'blue')
mercury = draw_ball(coords_mercury, 6, 'orange')

# устареваем текущие координаты
pref_coords_earth= gr.Point(coords_earth.x, coords_earth.y)
pref_coords_moon= gr.Point(coords_moon.x, coords_moon.y)
pref_coords_mercury= gr.Point(coords_mercury.x, coords_mercury.y)
while True:
    # вычисляем новые координаты
    
    #Земля
    coords_earth = update_coords(coords_earth, velocity_earth)
    acceleration_earth = update_acceleration(coords_earth, gr.Point(400, 400), 2000)
    velocity_earth = update_velocity(velocity_earth, acceleration_earth)
    
    #Луна
    coords_moon = update_coords(coords_moon, velocity_moon)
    acceleration_moon = update_acceleration(coords_moon, coords_earth, 60)
    velocity_moon = update_velocity(velocity_moon, acceleration_moon)

    #Меркурий
    coords_mercury = update_coords(coords_mercury, velocity_mercury)
    acceleration_mercury = update_acceleration(coords_mercury, gr.Point(400, 400), 2000)
    velocity_mercury = update_velocity(velocity_mercury, acceleration_mercury)
    #check_coords(coords, velocity)

    
    #  вычисляем разницу между старыми и новыми координатами
    #Земля
    if(coords_earth.x != pref_coords_earth.x or coords_earth.y != pref_coords_earth.y):
        w= sub(coords_earth, pref_coords_earth)
        # двигаемся на эту разницу
        earth.move(w.x, w.y)
    # устареваем новые координаты
    pref_coords_earth= gr.Point(coords_earth.x, coords_earth.y)

    #  вычисляем разницу между старыми и новыми координатами
    #Луна
    if(coords_moon.x != pref_coords_moon.x or coords_moon.y != pref_coords_moon.y):
        w= sub(coords_moon, pref_coords_moon)
        # двигаемся на эту разницу
        moon.move(w.x, w.y)
    # устареваем новые координаты
    pref_coords_moon= gr.Point(coords_moon.x, coords_moon.y)

    #  вычисляем разницу между старыми и новыми координатами
    #Меркурий
    if(coords_mercury.x != pref_coords_mercury.x or coords_mercury.y != pref_coords_mercury.y):
        w= sub(coords_mercury, pref_coords_mercury)
        # двигаемся на эту разницу
        mercury.move(w.x, w.y)
    # устареваем новые координаты
    pref_coords_mercury= gr.Point(coords_mercury.x, coords_mercury.y)
    
    gr.time.sleep(0.01)
