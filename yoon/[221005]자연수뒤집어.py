def solution(n):
    s = list(str(n))
    s.reverse()
    print(s)
    return list(map(int,s))