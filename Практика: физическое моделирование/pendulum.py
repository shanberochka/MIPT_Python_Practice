import math
import graphics as gr


def add(point1, point2):
    return gr.Point(point1.x + point2.x, point1.y + point2.y)


def update_angle():
    return math.atan(ball_deviation / ball_height)


def update_ball_acceleration():
    return gr.Point(-(G * angle),
                    ball_height - (ball_coords.y - vertex_coords.y))


def update_ball_height():
    return (cord_length ** 2 - ball_deviation ** 2) ** 0.5

def update_ball_deviation():
    return ball_coords.x - vertex_coords.x
def draw_cord():
    elements_distance = gr.Point(ball_deviation / (cord_elements+1),
                                 ball_height / (cord_elements+1))

    for i in range(1, cord_elements+1):

        element_coords = gr.Point(elements_distance.x*i + vertex_coords.x,
                                  elements_distance.y*i + vertex_coords.y)

        globals()['element_%s' % i] = gr.Circle(element_coords, element_size)
        globals()['element_%s' % i].setFill('black')
        globals()['element_%s' % i].draw(window)


def move_cord():
    elements_velocity_distance = gr.Point(ball_velocity.x / (cord_elements+1),
                                          ball_velocity.y / (cord_elements+1))
    for i in range(1, cord_elements+1):
        globals()['element_%s' % i].move(elements_velocity_distance.x * i,
                                         elements_velocity_distance.y * i)


window = gr.GraphWin("Model", 800, 800)

G = 0.1

ball_velocity = gr.Point(0, 0)
ball_acceleration = gr.Point(0, 0)

# Sets starting coordinates of a pendulum vertex and a ball.
vertex_coords = gr.Point(400, 180)
ball_coords = gr.Point(600, 500)

ball_height = ball_coords.y - vertex_coords.y

ball_deviation = ball_coords.x - vertex_coords.x

cord_length = (ball_deviation ** 2 + ball_height ** 2) ** 0.5

vertex = gr.Circle(vertex_coords, 10)
vertex.setFill('black')
vertex.draw(window)


ball = gr.Circle(ball_coords, 30)
ball.setFill('black')
ball.draw(window)

# Sets an amount of cord elements and a size of an element.
cord_elements = 18
element_size = 5

draw_cord()

while True:

    # Updates an angle and acceleration.
    angle = update_angle()
    ball_acceleration = update_ball_acceleration()

    # Updates velocity by an addition of velocity and acceleration.
    ball_velocity = add(ball_velocity, ball_acceleration)

    # Moves a ball by "x" coordinate and "y" coordinate of velocity.
    ball.move(ball_velocity.x, ball_velocity.y)

    # Moves a cord.
    move_cord()

    # Updates ball coordinates by an addition of old ball coordinates and
    # velocity.
    ball_coords = add(ball_coords, ball_velocity)

    # Updates ball deviation by new "x" coordinate of the ball and "x"
    # coordinate of pendulum vertex.
    ball_deviation = update_ball_deviation()

    # Updates ball height.
    ball_height = update_ball_height()

    # Sets a bit of delay for comfort watching.
    gr.time.sleep(0.01)

    # Breaks the cycle if the window is manually closed.
    if window.isClosed():
        break
