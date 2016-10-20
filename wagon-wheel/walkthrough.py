import turtle

def draw_line(length, angle):
    mike = turtle.Turtle()
    mike.left(angle)
    mike.forward(length / 2)
    mike.forward(-length)
    mike.forward(length / 2)

def star(nlines):
    for angle in range(0, 180, int(180/nlines)):
        draw_line(200, angle)

star(10)
