# -*- coding: utf-8 -*-
import sys

btn = list(map(int, sys.stdin.readline().split()))

for i in range(9):
    if (i==0 and btn[i]==2) or btn[i]==1:
        print('L',end='')
        last = 'L'
    elif btn[i]==3:
        print('R',end='')
        last = 'R'
    else:
        if last == 'R':
            print('L',end='')
            last = 'L'
        else:
            print('R',end='')
            last = 'R'
    if i!=8:
        print(' ',end='')