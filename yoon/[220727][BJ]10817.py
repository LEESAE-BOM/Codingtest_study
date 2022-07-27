import sys
list = list(map(int, sys.stdin.readline().split()))

list.remove(max(list))
print(max(list))
