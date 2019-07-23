#!/usr/bin/env python3

from turtle import *
from random import randint

T = Turtle()
Tsc = T.getscreen()
Tsc.setup(800, 800)
Tsc.bgcolor("light green")

T.up()
T.setposition(-350, 350)
T.setheading(0)
T.width(2)
T.down()
T.color("blue", "yellow")
T.begin_fill()

for s in range(4):
    T.fd(700)
    T.right(90)

T.end_fill()
T.up()
T.home()
T.down()

for s in range(2000):
    Th = T.heading()
    T.setheading(Th + randint(-30, 30))
    T.fd(5)
    if (abs(T.xcor()) >= 344):
        T.setheading((180 - Th) % 360)
        T.fd(10)
    if (abs(T.ycor()) >= 344):
        T.setheading((360 - Th))
        T.fd(10)

Tsc.exitonclick()

