N = int(input())
road=[]

for i in range(N):
    inp_str = list(input())
    temp = []
    for j in range(N):
        if inp_str[j]=='Y':
            temp.append(j)
    road.append(temp)
print(road)

def dfs(i, j, visited):
    # 현재 노드를 방문처리
    visited[i] = True
    if i==j:
        return True
    # 현재 노드와 인접한 노드를 확인
    for k in road[i]:
        dfs(k,j, visited)
max = -999
for i in range(N):
    temp =0
    for j in range(N):
        visited = [0 for k in range(N)]
        if dfs(i,j,visited)==True:
           temp+=1
    if temp>max:
        max=temp
    if max == N-1:
        break
print(max)
