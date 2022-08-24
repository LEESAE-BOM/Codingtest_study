n = int(input())
x, y = map(int,input().split())

count = 99999

for i in range(n):
    a , b = map(int,input().split())
    d = abs(x-a) + abs(y-b)
    if count>d:
        count = d

print(count*100)
