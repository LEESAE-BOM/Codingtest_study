import sys

a, b, c, d, e = map(int,sys.stdin.readline().split(' '))

sum = a * 1000 + b * 1500 + c * 2000 + d * 3000 + e * 5000

print(sum)