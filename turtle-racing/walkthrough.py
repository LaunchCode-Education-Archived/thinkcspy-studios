import turtle
import random

win = turtle.Screen()
win.bgcolor("lightblue")

# create 2 turtles
zach = turtle.Turtle()
jesse = turtle.Turtle()

# speed them up!
zach.speed(10)
jesse.speed(10)

jesse.color("turquoise")
zach.color("orange")

# make them walk randomly, loop variable represnts distance to travel forward
for distance in range(0,50,2): # generates [0,2,4,6,8,10,12,...46,48]

    # create a random angle for each turtle
    zach_angle = random.randrange(0,181)
    jesse_angle = random.randrange(0,181)

    # turn each turtle in that random direction
    zach.left(zach_angle)
    jesse.left(jesse_angle)

    # move each turtle forward by distance
    zach.forward(distance)
    jesse.forward(distance)

