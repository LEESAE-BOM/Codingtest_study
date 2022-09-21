def solution(arr, divisor):
    l = [a for a in arr if a%divisor==0]
    return sorted(l) if len(l) else [-1]