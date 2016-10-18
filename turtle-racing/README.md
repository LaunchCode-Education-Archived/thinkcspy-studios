# Studio: Turtle Racing

## Concepts Used

- Using modules. Specifically, the `turtles` and `random` modules.
- Iteracting with a module's API at a naive level, where you are calling its functions and making instances of its classes without yet having actually learned explicitly about functions and classes.
- Using a for loop.
- Various solutions to a single problem.

## Walkthrough

Make two turtles trace wobbly paths as if staggering around drunk. 

Here is a [video of a previous class](https://youtu.be/xOmRXIdxwmk).

## Studio 

In this studio we are going to work step by step through the problem of racing turtles. The idea is that we want to create two or more turtles and have them race across the screen from left to right. The turtle that goes the farthest is the winner.

There are several different, and equally plausible, solutions to this problem. Let’s look at what needs to be done, and then look at some of the options for the solution. To start, let’s think about a solution to the simplest form of the problem, a race between two turtles. We’ll look at more complex races later.

When you are faced with a problem like this in computer science it is often a good idea to find a solution to a simple problem first and then figure out how to make the solution more general.

Here is a possible sequence of steps that we will need to accomplish:

1. Import the modules we need
2. Create a screen
3. Create two turtles
4. Move the turtles to their starting positions
5. Send them moving across the screen

Here is the Python code for the first 4 steps above:

```python
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

# your code goes here

wn.exitonclick()
```

Now, you have several choices for how to fill in code for step 5. Here are some possibilities to try. Try coding each of the following in the box above to see the different kinds of behavior.

Use a single call to forward for each turtle, using a random number as the distance to move.
Create a for loop, using a random number for the parameter passed to the range function. Inside the for loop move one of the turtles forward by some number of units.
Create a single for loop using something like 150 or 200 as the range parameter. Then inside the for loop move each turtle forward using a random number as the parameter to forward.
So, which of these programs is better? Which of these programs is most correct? These are excellent questions. Program 1 is certainly the simplest, but it isn’t very satisfying as far as a race is concerned. Each turtle simply moves their distance on their turn. That is not very satisfying as far as a simulated race goes. Program 2 ends up looking a lot like Program 1 when you run it. Program 3 is probably the most ‘realistic’ assuming realism is very important when we’re talking about a simulated race of virtual turtles.

You may be thinking why can’t each turtle just move forward until they cross some artificial finish line? Good question! We’ll get to the answer to this, and look at the program in a later lesson when we learn about something called the while loop.





