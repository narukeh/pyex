#!/usr/bin/env python3
import math
import turtle

def squares (angle=0.5):
    turtle.reset()
    L=330
    turtle.speed(10)
    turtle.penup()
    turtle.goto(-L/2,-L/2)
    turtle.pendown()
    for i in range(660):
        turtle.forward(L)
        turtle.left(90+angle)
        L=L-L*math.sin(angle*math.pi/180)
    turtle.hideturtle()

squares(2)
