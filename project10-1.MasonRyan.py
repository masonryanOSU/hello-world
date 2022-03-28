import turtle, math

def drawCircle(t, center_x, center_y, radius):
    t.penup()
    t.goto(center_x, center_y)
    t.setheading(270)
    t.forward(radius)
    t.setheading(0)
    t.pendown()
    for rotate in range(120):
        distance = 2 * math.pi * radius / 120
        t.forward(distance)
        t.left(3)


sc = turtle.Screen()

drawCircle(turtle.Turtle(), 50, -100, 100)
