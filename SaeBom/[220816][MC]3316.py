n = int(input())

arr = [0 for _ in range(n)]

for i in range(n):    
    arr[i] = list(map(int, input().split()))

aircon = [0 for _ in range(31)]

for i in range(n):
    for j in range(arr[i][0],arr[i][1]+1,1):
        aircon[j]+=1
    
for i in range(31):
    if max(aircon)==aircon[i]:
        print(i)
        break
