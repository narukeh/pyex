#!/usr/bin/env python3
import math
import turtle

bob=turtle.Turtle()
bob.speed(0)

def polygon(n, length, h=1):
    angle = 360 / n
    sub=0
    for i in range(n+h):
        bob.fd(length - sub)
        bob.lt(angle)
        sub = sub + 1
polygon(n=6, length=70, h=64)

turtle.mainloop()
