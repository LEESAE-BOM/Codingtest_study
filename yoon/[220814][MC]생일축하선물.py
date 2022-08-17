# -*- coding: utf-8 -*-
import sys

n = int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
median=[]
for i in range(1, n-1):
# 슬라이싱 기억하기, 뒤에 인덱스-1 까지만 가져옴
    temp = numbers[i-1:i+2]
    median.append(sorted(temp)[1])

print(max(median))
    
