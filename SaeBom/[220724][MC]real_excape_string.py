# -*- coding: utf-8 -*-
# 틀림,2353, 추후 확인 
import sys

a = sys.stdin.readline()
a=a.replace("\\","\\\\").replace("'","\\'").replace('"','\\"')

print(a)
