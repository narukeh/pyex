#!/usr/bin/env python3
import math

def hp(w):
    l = len(w)
    hc = 0
    while hc < l:
        print(w[hc], end=' ')
        hc += 1
    print()

def vp(w):
    c = 0
    while c < len(w):
        hp(w[c:])
        c += 1

vp('Prizren')
hp('Prizren')
