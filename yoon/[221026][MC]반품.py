import sys

n, m = map(int,sys.stdin.readline().rstrip().split(' '))
p=[]
for i in range(n):
    tmp = int(sys.stdin.readline().rstrip())
    p.append(tmp)
p = sorted(p, reverse = True)

count = 0
for price in p:
    if m - price >= 0:
        m -= price
        count+=1
    else:
        continue
print(count)