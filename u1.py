#!/usr/bin/env python3
import math

print('____')
integers = [4, 44, 333]
# print(integers[0]/4 , integers[1]/4 , integers[2]/4 , sep='\n')
# print('gjendja aktuale e listes:')
# print(integers)
# print('____')

for i in range(len(integers)):
    integers[i] = integers[i] / 4
    print(integers[i])
print('gjendja aktuale e listes:')
print(integers)
print('____')

# integers = [4, 44, 333]
# c=0
# while c<(len(integers)):
#     integers[c] = integers[c]/4
#     print(integers[c])
#     c=c+1

# print('gjendja aktuale e listes:')
# print(integers)
# print('____')
