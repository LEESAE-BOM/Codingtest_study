# -*- coding: utf-8 -*-
import sys

n = int(sys.stdin.readline())
dic={}
for i in range(n):
    age, name = map(str, sys.stdin.readline().rstrip().split())
    age=int(age)

    # 온 순서를 key값으로 설정
    dic[i]=[age, name]

dic = sorted(dic.items(), key=lambda e: (-e[1][0],e[0]))

for i in dic:
    if i==(len(dic)-1):
        print(i[1][1], end='')
    else:
        print(i[1][1])
    
