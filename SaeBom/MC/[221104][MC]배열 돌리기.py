N = int(input())
arr = list(map(int,input().split()))
for i in range(N):
    temp = []
    for j in range(N):
        print(arr[j],end=' ')
        if j==0:
            continue
        elif j==N-1:
            temp.append(arr[j])
            temp.append(arr[0])
        else:
            temp.append(arr[j])
    print('')
    arr=temp

