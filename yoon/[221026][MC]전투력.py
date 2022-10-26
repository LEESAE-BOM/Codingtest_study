# -*- coding: utf-8 -*-
import sys

n = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().rstrip().split(' ')))
k = sorted(k)

max_k = 0
for i in range(n):
    if k[i] * (n-i) > max_k :
        max_k = k[i] * (n-i)
print(max_k)