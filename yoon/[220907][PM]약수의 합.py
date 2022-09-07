def solution(n):
    lst = [i for i in range(1, n//2 + 1) if n % i ==0]
    return sum(lst) + n