def solution(n):
    k=1
    answer = 0
    while(1):
        if n/k<1:
            break
        answer+=int((n%(k*10))/k)
        k*=10

    return answer
