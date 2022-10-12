def solution(n):
    answer = ''
    n = list(str(n))
    n.sort(reverse=True)
    for i in n:
        answer += i
    answer = int(answer)

    return answer