#!/usr/bin/env python3
import math

###2.1
def prodorsum(x,y):
    if x+y<100:
        print(x+y)
    else:
        print(x*y)

prodorsum(5,5)
prodorsum(55,55)

###2.2
def is_div(x):
    return x%7 == 0

is_div(49)
is_div(48)

###2.3
def is_odd(x):
    return x%2 == 0

is_odd(10)
is_odd(11)

###2.4
def grade(x):
    if 60>x:
        print(x, 'is D')
    elif 60 <= x <= 80:
        print(x, 'is C')
    elif 80 < x <= 90:
        print(x, 'is B')
    elif 90 < x <= 100:
        print(x, 'is A')

grade(59)
grade(60)
grade(61)
grade(79)
grade(80)
grade(81)
grade(89)
grade(90)
grade(91)

###2.5
#Hello

###2.6
def bigger(z,x,c,):
    if z>x and z>c:
        print(z)
    elif x>z and x>c:
        print(x)
    elif c>z and c>x:
        print(c)

bigger(1, 2, 3)
bigger(1, 3, 2)
bigger(2, 1, 3)
bigger(2, 3, 1)
bigger(3, 1, 2)
bigger(3, 2, 1)

###3.1
def do_it(a,b,fun):
    if fun=='+':
        print(a+b)
    elif fun=='-':
        print(a-b)
    elif fun=='*':
        print(a*b)
    elif fun=='/':
        print(a/b)

do_it(9,3,'+')
do_it(9,3,'-')
do_it(9,3,'*')
do_it(9,3,'/')

###3.2
def add_some(num, step):
    if step <= 0:
        return 'step should be greater than zero.'
    if num <= 0:
        return 0
    return num + add_some(num - step, step)

# Examples
print(add_some(10, 3))  # Output: 22
print(add_some(10, -1))  # Output: 'step should be greater than zero.'
print(add_some(3, 1))  # Output: 22
