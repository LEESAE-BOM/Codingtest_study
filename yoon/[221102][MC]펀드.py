# -*- coding: utf-8 -*-
import sys

A, B = map(int,sys.stdin.readline().rstrip().split())
N, M = map(int,sys.stdin.readline().rstrip().split())
options = [int(input()) for _ in range(N)]
options = sorted(options, reverse=True)
selected_options = options[:M]
price = A+B*sum(selected_options)
print(price)