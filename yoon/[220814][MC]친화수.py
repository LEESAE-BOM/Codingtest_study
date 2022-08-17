# -*- coding: utf-8 -*-
import sys

a, b= map(int,sys.stdin.readline().split())

a_j = 0
b_j = 0

for i in range(1, int(a**(1/2))+1):   
    if a%i == 0:
        a_j+=i
        if a!=a//i and i!=a//i:
            a_j+=a//i
            
for i in range(1, int(b**(1/2))+1):   
    if b%i == 0:
        b_j+=i
        if b!=b//i and i!=b//i:
            b_j+=b//i

if a_j == b and b_j == a:
    print("YES")
else:
    print("NO")
