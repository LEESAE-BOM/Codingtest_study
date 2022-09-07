def solution(a, b):
    answer = 0
    if a>b:
        maxn, minn = a, b
    else:
        maxn, minn = b, a
    for i in range(minn,maxn+1):
        answer+=i
    return answer