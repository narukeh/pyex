#!/usr/bin/env python3
import turtle

t = turtle.Turtle()
t.speed(0)
t.color("purple", "magenta")
w = turtle.Screen()
w.setup(width=800, height=600)
w.bgcolor("orange")
w.title("turtle example")

def flower():
    t.begin_fill()
    for i in range(36):
        t.forward(300)
        t.left(170)
    t.end_fill()

def star(segments=5, size=50, angle=216.0):
    t.begin_fill()
    for i in range(segments):
        t.forward(size)
        for i in range(segments):
            t.forward(size/5)
            for i in range(segments):
                t.forward(size/15)
                t.left(angle)
            t.left(angle)
        t.left(angle)
    t.end_fill()

def hardcode5():
    t.begin_fill()
    for i in range(5):
        t.forward(150)
        t.left(216)
    t.end_fill()

def hardcode7():
    t.begin_fill()
    for i in range(7):
        t.forward(150)
        t.left(154.25)
    t.end_fill()


#####Calling

t.penup()
t.goto(-370, 130)
t.pendown()
flower()

t.penup()
t.goto(-380, -40)
t.pendown()
hardcode5()

t.penup()
t.goto(-380, -230)
t.pendown()
hardcode7()

t.penup()
t.goto(70, 170)
t.pendown()
star(5, 200, 216)

t.penup()
t.goto(70, -170)
t.pendown()
star(7, 200, 154.25)

w.exitonclick()
