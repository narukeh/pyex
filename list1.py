#!/usr/bin/env python3
import math

print('____')
floats = [1.0, 2.0, 3.0]
print(floats[0]+1 , floats[1]+1 , floats[2]+1 , sep='\n')
print('gjendja aktuale e listes:')
print(floats)
print('____')

for i in range(len(floats)):
    floats[i] = floats[i] + 1
    print(floats[i])
print('gjendja aktuale e listes:')
print(floats)
print('____')

floats = [1.0, 2.0, 3.0]
c=0
while c<(len(floats)):
    floats[c]=floats[c]+1
    print(floats[c])
    c=c+1

print('gjendja aktuale e listes:')
print(floats)
print('____')
