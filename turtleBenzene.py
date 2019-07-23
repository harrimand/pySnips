#!/usr/bin/env python3
# Python program to draw Rainbow Benzene using Turtle Programming 

# Available colors for the turtle pen:
# https://ecsdtech.com/8-pages/121-python-turtle-colors 

# Online Turtle: https://repl.it/languages/python_turtle

# Turtle command reference and examples:
# https://docs.python.org/3/library/turtle.html
# https://www.geeksforgeeks.org/turtle-programming-python/

sides = 3

colors = ['red', 'white', 'blue', 'green', 'orange', 'purple', 'Light Sea Green', 'yellow',  'cyan']

validSides = sides <= len(colors)

def octTube():
    for x in range(360):
        t.pencolor(colors[x%8])
        t.width(x/100 + 1)
        t.forward(x)
        t.left(44)

def hexTube():
    for x in range(360):
        t.pencolor(colors[x%6])
        t.width(x/100 + 1)
        t.forward(x)
        t.left(59)


def tube(numSides):
    for x in range(360):
        t.pencolor(colors[x % numSides])
        t.width(x/100 + 3)
        t.forward(x)
        t.left(360/numSides - 1)


if(validSides):
    import turtle
    t = turtle.Pen()
    turtle.bgcolor('black')
    tube(sides)
    turtle.exitonclick()
else:
    print("\nNot enough colors\n")


'''
if(sides == 6):
    hexTube()
else:
    octTube()
'''
# turtle.exitonclick()

