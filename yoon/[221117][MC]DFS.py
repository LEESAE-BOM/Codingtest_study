# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10000)

def DFS(graph, c, visited):
    visited.append(c)
    for w in graph[c]:
        if w not in visited:
            visited = DFS(graph, w, visited)
    return visited
    
n, m = map(int,sys.stdin.readline().rstrip().split())
graph = [[]for _ in range(n+1)]
for i in range(m):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
    
for v in range(n+1):
    graph[v]=sorted(graph[v])
    
visited=[]*(n)
visited = DFS(graph, 1, visited)

for idx, i in enumerate(visited):
    if idx!=len(visited):
        print(i,end=' ')
    else:
        print(i,end='')