n = int(input())

def pibonacci_dp(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return pibonacci(n-2)+pibonacci(n-1)

def pibonacci(n):
    fibo = [0,1]
    for i in range(n-1):
        fibo.append(fibo[i]+fibo[i+1])
    return fibo[n]

print(pibonacci(n))
