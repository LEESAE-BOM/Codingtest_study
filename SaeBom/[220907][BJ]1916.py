N = int(input())
M = int(input())
graph = []
for i in range(N):
    graph.append([])

#출발 도시의 번호, 도착지의 도시 번호, 버스 비용
for i in range(M):
    start, arrive, cost = map(int,input().split())
    graph[start-1].append((arrive,cost))

start, arrive = map(int,input().split())

cost_list=[]
inf = 1000000000

for i in range(N):
    temp = []
    cols = [row[0] for row in graph[i]]
    cost = [row[1] for row in graph[i]]
    for j in range(N):
        if i==j:
            temp.append(0)
        elif j+1 in cols:
            temp.append(cost[cols.index(j+1)])
        else:
            temp.append(inf)
    cost_list.append(temp)

v = [0]*N
d = [0]*N

# 최소 거리를 가지는 정점을 반환
def getsmallindex():
    min = inf
    index = 0
    for i in range(0,N):
        if v[i]!=1 and d[i]<min:
            min = d[i]
            index=i
    return index

# 다익스트라 수행
def dijkstra(start):
    for i in range(0,N):
        d[i] = cost_list[start][i]
    v[start]=True
    for i in range(0,N-1):
        current = getsmallindex()
        v[current]=True
        for j in range(0,N):
            if v[j]!=1:
                if d[current]+cost_list[current][j] <d[j]:
                    d[j] = d[current]+cost_list[current][j]

dijkstra(start-1)
print(d[arrive-1])

