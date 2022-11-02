A,B = map(int,input().split())
N,M = map(int,input().split())
option=[]
for i in range(N):
    option.append(int(input()))
option.sort(reverse=True)
print(sum(option[0:M])*B+A)