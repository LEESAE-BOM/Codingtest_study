# -*- coding: utf-8 -*-
import sys
def ispossibile(number, s):
    for i in range(4):
        for j in range(i+1,4):
            if s==2*(number[i]+number[j]):

                return 1
                
number = str(sys.stdin.readline().rstrip())
number = list(map(int,number))

s = 0
for i in number:
    s+=i

if ispossibile(number,s)==1:
    print("YES")
else:
    print("NO")