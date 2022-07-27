import sys

n = int(input())
k = int(input())

if k > n:
    print("0")
    quit()
    
## sensor = [int(x) for x in input()]
sensor = list(map(int, sys.stdin.readline().split()))
sensor.sort()

diff=[]

for i in range(len(sensor) - 1):
    diff.append(sensor[i+1] - sensor [i])

diff.sort()

for _ in range(k-1):
    diff.remove(max(diff))

length = 0

for x in range(len(diff)):
    length += diff[x]
    
print(length)