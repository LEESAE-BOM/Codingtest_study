# -*- coding: utf-8 -*-
import sys

n = int(sys.stdin.readline().rstrip())
weights = list(map(int,sys.stdin.readline().rstrip().split()))
a, b = map(int, sys.stdin.readline().rstrip().split())

# print(min(weights[a-1:b]))

w = sorted(weights[a-1:b])

print(w[0])