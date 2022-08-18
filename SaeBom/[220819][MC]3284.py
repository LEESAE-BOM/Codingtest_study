N = int(input())

arr=[]
arr.insert(0, 0)
for i in range(1,N+1,1):
    a=input()
    if a =='D':
        arr.insert(0, i)
    else:
        arr.append(i)

for i in range(N+1):
    print(arr[i],end=' ')
