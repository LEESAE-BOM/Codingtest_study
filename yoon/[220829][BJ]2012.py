import sys

n = int(input())
pred = []
for i in range(n):
    pred.append(int(sys.stdin.readline()))
pred.sort()

sum = 0
for i in range(n):
    sum += abs(pred[i] - (i+1))
print(sum)