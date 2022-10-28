N = int(input())
A =[]
for i in range(N):
    A.append(int(input()))
B,C = map(int,input().split())

answer = []

for i in A:
    if i<=B:
        answer.append(1)
        continue
    else:
        k = i-B
        if k%C==0:
            answer.append(k//C+1)
        else:
            answer.append(k//C + 2)

print(sum(answer))