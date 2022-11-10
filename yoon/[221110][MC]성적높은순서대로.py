# -*- coding: utf-8 -*-
import sys

n = int(sys.stdin.readline())
dic={}
for i in range(n):
    name, score = map(str, sys.stdin.readline().rstrip().split())
    score=int(score)

    dic[i]=[name, score]

dic = sorted(dic.items(), key=lambda e: (e[1][1],e[1][0].lower()),reverse=True)

for i in dic:
    if i==(len(dic)-1):
        print(i[1][0],end='')
    else:
        print(i[1][0], end=' ')