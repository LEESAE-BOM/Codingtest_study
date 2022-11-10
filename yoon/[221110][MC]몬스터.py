import sys
sys.setrecursionlimit(100000)

M,N,K = map(int,input().split())
graph = [[1 for j in range(M)] for i in range(N)]

for i in range(K):
    x,y = map(int,input().split())
    graph[x][y]=0

def DFS(graph,i,j):
    if i<0 or i>=N or j<0 or j>=M:
        return False
    if graph[i][j]==0:
        graph[i][j]=1
        DFS(graph,i-1,j)
        DFS(graph, i , j-1)
        DFS(graph, i +1, j)
        DFS(graph, i , j+1)
        return True
        
count = 0
for i in range(N):
    for j in range(M):
        if DFS(graph,i,j)==True:
            count+=1
print(count)
