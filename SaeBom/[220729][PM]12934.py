import math

def solution(n):
    x=math.sqrt(n)
    if x.is_integer()==True:
        answer=(int(x)+1)**2
        return answer
    else:
        return -1
