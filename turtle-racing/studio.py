import turtle              # 1.  import the modules
import random

wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4.  Move the turtles to their starting point
lance.up()
andy.goto(-100,20)
lance.goto(-100,-20)

# Approach 1

andy_dist = random.randrange(0,200)
lance_dist = random.randrange(0,200)

andy.forward(andy_dist)
lance.forward(lance_dist)

# Approach 2
"""
steps = random.randrange(25,50)

for step in range(steps):
    andy_dist = random.randrange(0,10)
    lance_dist = random.randrange(0,10)
    andy.forward(andy_dist)
    lance.forward(lance_dist)
"""

wn.exitonclick()
