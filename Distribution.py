__author__ = 'grahamcooke'

import random as r

def roll(n):
    l = 0
    for i in range(n):
        if(r.randint(0, 1)) > 0:
            l += 1
    return n+l

for n in range(10):
    q = 1
    for n in range(10):
        q = roll(q)
    print(q)