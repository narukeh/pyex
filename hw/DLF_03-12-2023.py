#!/usr/bin/env python3
import math

###1
print('_'*80)
# r=float(input("Radius: "))
r=5
volume = (4/3) * math.pi * (r**3)
print("The volume of a Sphere with a radius of:", r, "is", volume)

print('_'*80)
###2
ipob=24.95
bsd=40
dd = ipob * ( bsd /100 )
apob = ipob - dd
ics=3
acs=0.75

co60b = ipob+ics + 59*( apob + acs )
print("60 books costs:", co60b, "bucks")

print('_'*80)
###3
ep = 8*60+15
tp = 7*60+12
st = 6*3600+52*60
after_st = st + ep + 3*tp + ep

s=int(after_st)
h = s // 3600
m = 60 * ((s/3600) - (s//3600))
print('Home at ', int(h), ':' , int(m))
print('_'*80)
