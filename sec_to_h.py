#!/usr/bin/env python3
import math

# s = 27000
s=int(float(input("Sekondat: ")))
h = s // 3600
m = 60 * ((s/3600) - (s//3600))

print(h,"ore, e",m,"minuta")
