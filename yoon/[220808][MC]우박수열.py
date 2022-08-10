# -*- coding: utf-8 -*-
import sys

a_i = int(sys.stdin.readline())

while(1):
    print(a_i,end=' ')  
    if a_i%2:
        a_i = 3 * a_i + 1
    else:
        a_i = a_i // 2
    if a_i == 1:
        print(a_i)
        break
