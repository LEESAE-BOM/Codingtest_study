N,M = map(int,input().split())
people =[[] for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    people[a].append(b)
    people[b].append(a)

jiin = people[1].copy()

for i in people[1]:
    for j in people[i]:
        jiin.append(j)
answer=len(set(jiin))
if answer==0:
    print(1)
else:
    print(answer-1)