n = int(input())

input_list = []
graph = [[] for i in range(n)]

for i in range(n):
    input_list.append(list(map(int,input().split())))
    for j in range(n):
        if input_list[i][j]==1:
            graph[i].append(j)

answer_graph = [[0 for j in range(n)] for i in range(n)]

def DFS(i,j,visited,start,k):
    if i==j:
        if k != 0:
            answer_graph[start][j]=1
    k+=1
    for p in graph[i]:
        if visited[p]!=1:
            visited[p] = 1
            DFS(p,j,visited,start,k)

for i in range(n):
    for j in range(n):
        visited = [0 for i in range(n)]
        DFS(i,j,visited,i,0)
for i in range(n):
    for j in range(n):
        print(answer_graph[i][j],end=' ')
    print('')