#!/usr/bin/env python3
import math

def asdf(x):
    print('hello', x)
def rep_asdf(y):
    c=0
    while (c < y):
        asdf('name')
        c += 1
z=(input('count: '))
if (z == ""):
    z=3
z=int(z)
rep_asdf(z)
