# -*- coding: utf-8 -*-
import sys

N = int(sys.stdin.readline().rstrip())
card=[0]

for i in range(1, N + 1):
    b = str(sys.stdin.readline().rstrip())

    if b == 'U':
        card.append(i)
    elif b =='D':
        card.insert(0, i)
    print(card)
    
for j in card:
    print(j, end=' ')