def zisu(n,k):
    if n%k==0:
        return True
    return False

def solution(n):
    answer = 0
    for i in range(1,n+1):
        if zisu(n,i)==True:
            answer+=i
    return answer
