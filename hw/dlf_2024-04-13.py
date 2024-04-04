#!/usr/bin/env python3
import math

###6.1
word=(input('Press Enter to leave the default word, or enter one now: '))
if word == "":
    word = 'bookkeeper'

cons = 0
for i in range(len(word) - 1):  # Loop through indices up to len(word) - 1
    if word[i] == word[i + 1]:  # Check for double consecutive letters
        cons += 1

if cons >= 3:
    print(word, 'has at least 3 double consecutive letters')
else:
    print(word, 'does NOT have at least 3 double consecutive letters')

###7.1
def nested_sum(t):
    c=0
    for i1 in t:
        for i2 in i1:
            c = c + i2
    return(c)

nested_sum([[1, 2], [3], [4, 5, 6]])

###7.2
def csum(t):
     c_t=[]
     c=0
     for i in t:
         c = c + i
         c_t.append(c)
     return(c_t)

csum([1,2,3,4])

###7.3
def middle(t):
    c_t=[]
    for i in range(1,len(t)-1):
        c_t.append(t[i])
    return c_t

middle([10,11,12,13,14,15,16])

###7.4
def chop(t):
    del t[0]
    del t[-1]

t = [10, 11, 12, 13, 14, 15, 16]
chop(t)
# print(t)

###7.5
def is_sorted(t):
    t_sa=sorted(t, reverse=False)
    # t_sd=sorted(t, reverse=True)
    if t == t_sa:
        return True
    else:
        return False

print(is_sorted([1,2,3,4,5]))
print(is_sorted([2,1,3,4,5]))

###7.6
def is_anagram(s1,s2):
    s1_s=sorted(s1)
    s2_s=sorted(s2)
    return s1_s==s2_s

print(is_anagram('stable','tables'))
print(is_anagram('asdf','asdv'))

###7.7
def has_duplicates(t):
    t_s=sorted(t)
    for i in range(len(t_s)-1):
        if t_s[i] == t_s[i+1]:
            return True
    return False

print(has_duplicates([1,2,3,4,2,5,6,7]))
print(has_duplicates([1,2,3,4,5,6,7]))
