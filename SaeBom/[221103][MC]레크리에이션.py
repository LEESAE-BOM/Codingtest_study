N = int(input())
mom = list(map(int,input().split()))
a,b = map(int,input().split())
mom = mom[a-1:b]
print(min(mom))