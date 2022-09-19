N, M, V = map(int,input().split())

from collections import deque

graph = [[] for i in range(N+1)]

for i in range(M):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited =[0 for i in range(N+1)]

for i in range(len(graph)):
    graph[i].sort()
#print(graph,visited)

def DFS(v):
    if visited[v]==1:
        return
    else:
        visited[v]=1
    print(v,end=' ')
    for i in graph[v]:
        DFS(i)

DFS(V)
print()
visited =[0 for i in range(N+1)]
def BFS(v):
    visited[v]=1
    b = deque([v])
    while(b):
        v= b.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if visited[i]==0:
                b.append(i)
                visited[i]=1
BFS(V)



