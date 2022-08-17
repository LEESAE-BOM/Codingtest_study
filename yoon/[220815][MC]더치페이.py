# -*- coding: utf-8 -*-
import sys

N, M = map(int,sys.stdin.readline().split())
ppl = [0 for _ in range(N)]

ns = []
for i in range(M):
    ns.clear()
    C, n =  map(int, sys.stdin.readline().split())
    price = C // n
    ns = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(len(ns)):
        ppl[ns[j] - 1]+=price

for i in range(N):
    print(ppl[i], end=' ')