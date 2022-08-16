n = int(input())

if n == 1:
    k = int(input())
    print(0)
else:
    arr = [0 for _ in range(n)]

    for i in range(n):    
        arr[i] = list(map(int, input().split()))


    for i in range(n):
        k=0
        j=0
        while j < n:
            if arr[i][j] == 1:
                break
            if k==1:
                arr[i][j] = 0
            j+=1
            if (j == n) and (k==0):
                j=0
                k=1
        k=0
        j=0
        while j < n:
            if arr[j][i] == 1:
                break
            if k==1:
                arr[j][i] = 0
            j+=1
            if (j == n) and (k==0):
                j=0
                k=1

    sum =0
    for i in arr:
        sum+=i.count(2)
    print(sum)
    
    
