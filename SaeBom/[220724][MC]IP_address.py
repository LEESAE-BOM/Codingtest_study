# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline()

for i in range(0,len(input)-1,1):
    if input[i] == '.':
        print("IPv4")
        break
    elif input[i]== ':':
        print("IPv6")
        break
    else:
        continue
