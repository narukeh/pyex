#!/usr/bin/env python3
import turtle

w = turtle.Screen()
t = turtle.Turtle()
t.color("purple", "magenta")
w.setup(width=800, height=600)
w.bgcolor("orange")
w.title("turtle example")

t.begin_fill()
for i in range(4):
    t.forward(50)
    t.right(90)
t.end_fill()

t.penup()
t.forward(150)
t.pendown()

t.begin_fill()
for i in range(4):
    t.forward(50)
    t.right(90)
t.end_fill()

t.penup()
t.forward(150)
t.pendown()

t.begin_fill()
for i in range(4):
    t.forward(50)
    t.right(90)
t.end_fill()


w.exitonclick()
