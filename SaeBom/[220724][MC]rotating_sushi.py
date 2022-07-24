# -*- coding: utf-8 -*-
import sys

a = sys.stdin.readline()
list = a.split() #1000 1500 2000 3000 5000
sum = int(list[0])*1000+int(list[1])*1500+int(list[2])*2000+int(list[3])*3000+int(list[4])*5000
print(sum)
