# -*- coding: utf-8 -*-
import sys

n = int(sys.stdin.readline().strip())
cx, cy = map(int,sys.stdin.readline().split())
pay=[]

for _ in range(n):
    px, py = map(int,sys.stdin.readline().split())
    diff = abs(cx - px) + abs(cy - py)
    pay.append(diff*100)

print(min(pay))