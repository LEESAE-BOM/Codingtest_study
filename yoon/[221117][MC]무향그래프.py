# -*- coding: utf-8 -*-
import sys

n, m = map(int,sys.stdin.readline().rstrip().split())
graph = [[]for _ in range(n+1)]
for i in range(m):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
    
for v in range(1, n+1):
    if len(graph[v])==0:
        print('no')
    else:
        graph[v]=sorted(graph[v])
        for n in graph[v]:
            print(n,end=' ')
        print()
    