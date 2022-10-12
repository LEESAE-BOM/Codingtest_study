def solution(arr, divisor):
    answer = []
    for n in arr:
        if (n%divisor)==0:
            answer.append(n)
    if len(answer)==0:
        answer.append(-1)
    answer.sort()
    return answer

# 파이썬은 or 일 때 앞이 참이면 return 거짓이면 뒤에까지 봄,,
# def solution(arr, divisor): return sorted([n for n in arr if n % divisor == 0]) or [-1]