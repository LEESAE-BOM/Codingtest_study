n = int(input())
a = list(map(int, input().split()))
mean = int(sum(a)/len(a))
count = 0
plus = 0
minus = 0
for i in range(n):
    if a[i]> mean:
        plus+=a[i] - mean
    elif a[i]<mean:
        minus+= mean - a[i]
sum = minus+(plus-minus)
print(sum)
