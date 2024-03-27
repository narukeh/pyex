#!/usr/bin/env python3
import math

# def count(fjala, shkronja):
#     c = 0
#     for letter in fjala:
#         if letter == shkronja:
#             c += 1
#     return c
# print(count('otoralingologu','o'))



# a=input('emri: ')
# b=input('mbiemri: ')
# print('hello,',b,a)

def vp(w):
    c=0
    while c < len(w):

        def hp(w):
            l=len(w)
            hc=0
            while hc<l:
                print( w[hc], end=' ')
                hc=hc+1
            print()

        if c==0:
            hp(w)
        else:
            print(w[c])
        c += 1
vp('Prizren')
