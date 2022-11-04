# -*- coding: utf-8 -*-
import sys

n = int(sys.stdin.readline().rstrip())

for i in range(2**n):
    num = str(format(i, 'b')).zfill(n)
    print(num)