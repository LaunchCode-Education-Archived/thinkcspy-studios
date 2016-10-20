"""
Studio: Wagon Wheel
"""

import turtle

win = turtle.Screen()
win.bgcolor("green")

def draw_square(length, turtle):
    for side in range(4):
        turtle.forward(length)
        turtle.left(90)


def draw_grid(length, angle, turtle):
    turtle.left(angle)
    for side in range(4):
        draw_square(length, turtle)
        turtle.left(90)

def pattern(nlines):
    mike = turtle.Turtle()
    mike.speed(20)
    mike.color("blue")
    for angle in range(0, 85, int(90/nlines)):
        draw_grid(50, angle, mike)

win = turtle.Screen()
win.bgcolor("green")
pattern(4)
