n = int(input())
a = list(map(int,input().split()))
b = sorted(a)

start = -1

for i in range(n):
    if start == -1 and a[i]!=b[i]:
        start = i
    if a[i]!=b[i]:
        last = i
            
print(last - start +1)
