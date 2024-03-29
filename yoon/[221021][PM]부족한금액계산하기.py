from math import sqrt
def solution(left, right):
    answer = 0
    for n in range(left, right + 1):
        if sqrt(n) == int(sqrt(n)):
            answer -= n
        else:
            answer += n
    return answer